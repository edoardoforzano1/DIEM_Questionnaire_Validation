import re, yaml, openpyxl
from pathlib import Path
cfg = yaml.safe_load(Path('configuration/validation_config.yaml').read_text(encoding='utf-8'))
cur_path = Path(cfg['working_dir']) / cfg['questionnaire_file']
lang = str(cfg['language']).lower()
repo = Path(cfg['templates_dir'])
cand=[p for p in repo.glob('*.xlsx') if 'geopoll' in p.name.lower() and f'_{lang}_' in p.name.lower() and 'template' in p.name.lower()]

def d(p):
    m=re.search(r'template_(\d{8})', p.name)
    return int(m.group(1)) if m else 0
cand.sort(key=lambda p:(d(p), p.stat().st_mtime), reverse=True)
ref_path=cand[0]

def qset(path):
    wb=openpyxl.load_workbook(path, data_only=True, read_only=True)
    ws=wb['survey'] if 'survey' in wb.sheetnames else wb[wb.sheetnames[0]]
    hdr=[ws.cell(3,c).value for c in range(1,90)]
    idx={str(v).strip():c for c,v in enumerate(hdr, start=1) if v is not None}
    qcol=idx.get('Q Name')
    out=set()
    for r in range(4, ws.max_row+1):
        q=str(ws.cell(r,qcol).value or '').strip()
        if q: out.add(q)
    return out
cur=qset(cur_path); ref=qset(ref_path)
for q in ['confl_agri_imp','confl_foodsec_imp','income_sec_comp','income_third','assistance_provider','covid','ls_all']:
    print(q, 'current=', q in cur, 'reference=', q in ref)
