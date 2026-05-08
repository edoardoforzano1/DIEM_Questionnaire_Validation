import openpyxl, json
from collections import Counter
from pathlib import Path
p=Path(r"""C:/git/DIEM_Questionnaire_Validation/batch_output/geopoll_skip_taxonomy_check/geopoll_output/report_geopoll_ar_YEM_R601_20260508.xlsx""")
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
        if it and it!='No issues in this category':
            c[it]+=1
print(json.dumps(dict(c), indent=2, ensure_ascii=False))
