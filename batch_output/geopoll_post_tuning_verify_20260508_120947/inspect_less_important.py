import openpyxl
from pathlib import Path
p=Path(r"""C:\\git\\DIEM_Questionnaire_Validation\\batch_output\\geopoll_post_tuning_verify_20260508_120947\\geopoll_output\\report_geopoll_ar_YEM_R303_20260508.xlsx""")
wb=openpyxl.load_workbook(p,data_only=True,read_only=True)
ws=wb['Question Changes']
header=None
printed=0
for row in ws.iter_rows(values_only=True):
    vals=["" if v is None else str(v) for v in row]
    if 'Issue type' in vals and 'Field' in vals and 'Severity' in vals:
        header={v:i for i,v in enumerate(vals) if v}
        continue
    if header and any(vals):
        it=vals[header['Issue type']]
        if it in {'conditional_changed','randomize_changed','programming_instructions_changed','core_questions_only_changed'}:
            field=vals[header['Field']]
            sev=vals[header['Severity']]
            lscope=vals[header['Language scope']] if 'Language scope' in header else ''
            print(it,'|',field,'|',sev,'|',lscope)
            printed += 1
            if printed>=12:
                break
