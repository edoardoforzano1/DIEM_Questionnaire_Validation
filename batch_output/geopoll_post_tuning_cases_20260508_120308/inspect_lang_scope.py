import openpyxl, json
from pathlib import Path
p=Path(r"""C:\\git\\DIEM_Questionnaire_Validation\\batch_output\\geopoll_post_tuning_cases_20260508_120308\\geopoll_output\\report_geopoll_en_COD_R201_20260508.xlsx""")
wb=openpyxl.load_workbook(p,data_only=True,read_only=True)
ws=wb['Question Changes']
header=None
for r in ws.iter_rows(values_only=True):
    vals=["" if v is None else str(v) for v in r]
    if 'Issue type' in vals and 'Language scope' in vals:
        header={v:i for i,v in enumerate(vals) if v}
        print('HEADER',header)
        continue
    if header and any(vals):
        it=vals[header.get('Issue type',-1)] if header.get('Issue type',-1)>=0 else ''
        ls=vals[header.get('Language scope',-1)] if header.get('Language scope',-1)>=0 else ''
        if ls and ls not in ('N/A','EN','No issues in this category'):
            rec={k: vals[i] if i < len(vals) else '' for k,i in header.items()}
            print(json.dumps(rec, ensure_ascii=False))
