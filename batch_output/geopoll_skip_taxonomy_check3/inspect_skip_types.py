import openpyxl, json
from collections import Counter
from pathlib import Path
p=Path(r"""C:/git/DIEM_Questionnaire_Validation/batch_output/geopoll_skip_taxonomy_check3/geopoll_output/report_geopoll_ar_YEM_R603_20260508.xlsx""")
wb=openpyxl.load_workbook(p,data_only=True,read_only=True)
ws=wb['Questionnaire Structure']
header=None
c=Counter()
for row in ws.iter_rows(values_only=True):
    vals=["" if v is None else str(v).strip() for v in row]
    if 'Issue type' in vals and 'Severity' in vals:
        header={v:i for i,v in enumerate(vals) if v}
        continue
    if header and any(vals):
        it=vals[header.get('Issue type',-1)] if header.get('Issue type',-1)>=0 else ''
        sv=vals[header.get('Severity',-1)].lower() if header.get('Severity',-1)>=0 else ''
        if it and it!='No issues in this category':
            c[(it,sv)]+=1
print(json.dumps({f'{k[0]}|{k[1]}':v for k,v in c.items()}, indent=2, ensure_ascii=False))
