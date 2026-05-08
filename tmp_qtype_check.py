import openpyxl, json
from collections import Counter
from pathlib import Path
wb=openpyxl.load_workbook(Path(r"""C:/git/DIEM_Questionnaire_Validation/batch_output/geopoll_qtype_high_check/geopoll_output/report_geopoll_en_COD_R606_20260508.xlsx"""),data_only=True,read_only=True)
ws=wb['Questionnaire Structure']
header=None
c=Counter()
for row in ws.iter_rows(values_only=True):
    vals=["" if v is None else str(v).strip() for v in row]
    if 'Issue type' in vals and 'Severity' in vals:
        header={v:i for i,v in enumerate(vals) if v}
        continue
    if header and any(vals):
        it=vals[header.get('Issue type',-1)]
        sv=vals[header.get('Severity',-1)].lower()
        if it=='qtype_changed':
            c[sv]+=1
print(json.dumps(dict(c),indent=2))