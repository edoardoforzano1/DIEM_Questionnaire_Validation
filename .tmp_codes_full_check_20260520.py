import re, yaml, openpyxl
from pathlib import Path
PAT = re.compile(r'(?m)^\s*(\d+)\)\s*(.*?)(?=^\s*\d+\)|\Z)', re.DOTALL)

cfg = yaml.safe_load(Path('configuration/validation_config.yaml').read_text(encoding='utf-8'))
cur_path = Path(cfg['working_dir']) / cfg['questionnaire_file']
lang = str(cfg['language']).lower()
repo = Path(cfg['templates_dir'])

cand = [p for p in repo.glob('*.xlsx') if 'geopoll' in p.name.lower() and f'_{lang}_' in p.name.lower() and 'template' in p.name.lower()]

def date_key(p):
    m = re.search(r'template_(\d{8})', p.name)
    return int(m.group(1)) if m else 0
cand.sort(key=lambda p: (date_key(p), p.stat().st_mtime), reverse=True)
ref_path = cand[0]

print('CURRENT:', cur_path)
print('REFERENCE:', ref_path)

def load_codes(path):
    wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
    ws = wb['survey'] if 'survey' in wb.sheetnames else wb[wb.sheetnames[0]]
    hdr = [ws.cell(3,c).value for c in range(1,90)]
    idx = {str(v).strip():c for c,v in enumerate(hdr, start=1) if v is not None}
    qcol = idx.get('Q Name'); ccol = idx.get('Codes')
    out = {}
    for r in range(4, ws.max_row+1):
        q = str(ws.cell(r,qcol).value or '').strip() if qcol else ''
        t = str(ws.cell(r,ccol).value or '') if ccol else ''
        if not q:
            continue
        entries=[]
        for m in PAT.finditer(t):
            entries.append((int(m.group(1)), ' '.join(m.group(2).split())))
        if entries:
            out[q]=entries
    return out

cur = load_codes(cur_path)
ref = load_codes(ref_path)
print('Parsed code questions current/ref:', len(cur), len(ref))

common = set(cur) & set(ref)
removed_rows = []
for q in sorted(common):
    cnums = {n for n,_ in cur.get(q,[])}
    rnums = {n for n,_ in ref.get(q,[])}
    miss = sorted(rnums - cnums)
    if miss:
        removed_rows.append((q, len(miss), miss[:10]))

print('Questions with removed code nums:', len(removed_rows))
for rec in removed_rows[:20]:
    print('  ', rec)

# strong case: q has reference codes but no current codes
no_cur = sorted([q for q in ref.keys() if q not in cur])
print('Questions with ref codes but zero current parsed codes:', len(no_cur))
for q in no_cur[:20]:
    print('  ', q, 'ref_count=', len(ref[q]))

for q in ['confl_agri_imp','confl_foodsec_imp','income_sec_comp','income_third','assistance_provider']:
    print('Q', q, 'cur=', len(cur.get(q,[])), 'ref=', len(ref.get(q,[])))
    if ref.get(q):
        print('  ref head', ref[q][:4])
    if cur.get(q):
        print('  cur head', cur[q][:4])
