import re, openpyxl, yaml
from pathlib import Path
pat = re.compile(r'(?m)^\s*(\d+)\)\s*(.*?)(?=^\s*\d+\)|\Z)', re.DOTALL)

cfg = yaml.safe_load(Path('configuration/validation_config.yaml').read_text(encoding='utf-8'))
qpath = Path(cfg['working_dir']) / cfg['questionnaire_file']
lang = str(cfg['language']).lower()
repo = Path(cfg['templates_dir'])

cand = [p for p in repo.glob('*.xlsx') if 'geopoll' in p.name.lower() and f'_{lang}_' in p.name.lower() and 'template' in p.name.lower()]

def d(p):
    m = re.search(r'template_(\d{8})', p.name)
    return int(m.group(1)) if m else 0
cand.sort(key=lambda p: (d(p), p.stat().st_mtime), reverse=True)
ref = cand[0]
print('current:', qpath)
print('reference:', ref)

def codes_map(path):
    wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
    ws = wb['survey'] if 'survey' in wb.sheetnames else wb[wb.sheetnames[0]]
    hdr = [ws.cell(3,c).value for c in range(1,80)]
    idx = {str(v).strip():c for c,v in enumerate(hdr, start=1) if v is not None}
    qcol = idx.get('Q Name'); ccol = idx.get('Codes'); mcol = idx.get('Mandatory')
    out = {}
    for r in range(4, ws.max_row+1):
        q = str(ws.cell(r,qcol).value or '').strip() if qcol else ''
        t = str(ws.cell(r,ccol).value or '') if ccol else ''
        m = str(ws.cell(r,mcol).value or '').strip() if mcol else ''
        if not q:
            continue
        ent = []
        for mm in pat.finditer(t):
            ent.append((int(mm.group(1)), ' '.join(mm.group(2).split())))
        if ent:
            out[q] = {'items': ent, 'mandatory': m}
    return out

cur = codes_map(qpath)
refm = codes_map(ref)
print('q with parsed codes current/ref:', len(cur), len(refm))

added_q = sorted(set(cur)-set(refm))
removed_q = sorted(set(refm)-set(cur))
print('q only current:', len(added_q), added_q[:5])
print('q only ref:', len(removed_q), removed_q[:5])

common = sorted(set(cur)&set(refm))
add=rem=tok=drift=0
for q in common:
    c = cur[q]['items']; r = refm[q]['items']
    cnum = {n:t for n,t in c}; rnum = {n:t for n,t in r}
    for n in sorted(set(cnum)-set(rnum)): add += 1
    for n in sorted(set(rnum)-set(cnum)): rem += 1
    for n in sorted(set(cnum)&set(rnum)):
        if cnum[n].strip().lower()!=rnum[n].strip().lower(): tok += 1
    cinv = {t.strip().lower(): n for n,t in c}
    rinv = {t.strip().lower(): n for n,t in r}
    for t in set(cinv)&set(rinv):
        if cinv[t]!=rinv[t]: drift += 1
print('raw deltas: added',add,'removed',rem,'token_mismatch',tok,'position_drift',drift)

# simulate forced change on one coded question
q = next(iter(common)) if common else None
if q:
    nums = [n for n,_ in cur[q]['items']]
    print('simulate on q:',q,'first num:',nums[0] if nums else None)
    sim_added = 1 if nums else 0
    print('simulated codes_added would be >=', sim_added)
