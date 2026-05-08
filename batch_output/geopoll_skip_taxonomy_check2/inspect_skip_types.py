import openpyxl, json
from collections import Counter
from pathlib import Path
p=Path(r"""C:/git/DIEM_Questionnaire_Validation/batch_output/geopoll_skip_taxonomy_check2/geopoll_output/report_geopoll_ar_YEM_R602_20260508.xlsx""")
wb=openpyxl.load_workbook(p,data_only=True,read_only=True)
ws=wb['Questionnaire Structure']
header=None
c=Counter()
sev=Counter()
for row in ws.iter_rows(values_only=True):
    vals=["" if v is None else str(v).strip() for v in row]
    if 'Issue type' in vals and 'Severity' in vals:
        header={v:i for i,v in enumerate(vals) if v}
        continue
    if header and any(vals):
        it=vals[header.get('Issue type',-1)] if header.get('Issue type',-1)>=0 else ''
        sv=vals[header.get('Severity',-1)].lower() if header.get('Severity',-1)>=0 else ''
        if it and it!='No issues in this category':
            c[it]+=1
            if sv in {'high','medium','info'}:
                sev[(it,sv)] += 1
print(json.dumps({'counts':dict(c), 'severity': {f'{k[0]}|{k[1]}':v for k,v in sev.items()}}, indent=2, ensure_ascii=False))
