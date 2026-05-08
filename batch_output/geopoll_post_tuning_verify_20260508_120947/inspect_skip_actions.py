import openpyxl
from pathlib import Path
p=Path(r"""C:\\git\\DIEM_Questionnaire_Validation\\batch_output\\geopoll_post_tuning_verify_20260508_120947\\geopoll_output\\report_geopoll_ar_YEM_R303_20260508.xlsx""")
wb=openpyxl.load_workbook(p,data_only=True,read_only=True)
ws=wb['Questionnaire Structure']
header=None
printed=0
for row in ws.iter_rows(values_only=True):
    vals=["" if v is None else str(v) for v in row]
    if 'Issue type' in vals and 'Action' in vals and 'Severity' in vals:
        header={v:i for i,v in enumerate(vals) if v}
        continue
    if header and any(vals):
        it=vals[header['Issue type']]
        sev=vals[header['Severity']].lower() if header['Severity']<len(vals) else ''
        action=vals[header['Action']]
        if sev in ('medium','info') and it:
            print(it,'|',sev,'|',action)
            printed+=1
            if printed>=12:
                break
