import openpyxl
from pathlib import Path
report=Path(r"""C:\git\DIEM_Questionnaire_Validation\batch_output\kobo_cluster_ea_patch_check_20260508_140842\kobo_output\report_kobo_en_AFG_R501_20260508.xlsx""")
wb=openpyxl.load_workbook(report,data_only=True,read_only=True)
ws=wb['Summary']
for row in ws.iter_rows(values_only=True):
    vals=["" if v is None else str(v) for v in row]
    if any('Cluster/EA choice changes summary' in v for v in vals):
        print(vals)
