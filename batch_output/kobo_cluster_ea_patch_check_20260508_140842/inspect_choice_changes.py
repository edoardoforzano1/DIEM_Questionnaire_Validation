import openpyxl, json
from pathlib import Path
report = Path(r"""C:\git\DIEM_Questionnaire_Validation\batch_output\kobo_cluster_ea_patch_check_20260508_140842\kobo_output\report_kobo_en_AFG_R501_20260508.xlsx""")
wb = openpyxl.load_workbook(report, data_only=True, read_only=True)
ws = wb['Choice Changes']
header=None
rows=[]
for row in ws.iter_rows(values_only=True):
    vals=["" if v is None else str(v).strip() for v in row]
    if 'Issue type' in vals and 'Q Name' in vals and 'list_name' in vals:
        header={v:i for i,v in enumerate(vals) if v}
        continue
    if header and any(vals):
        it=vals[header['Issue type']]
        if it=='No issues in this category' or it=='':
            continue
        rec={k:(vals[i] if i < len(vals) else '') for k,i in header.items()}
        rows.append(rec)

cluster_ea=[r for r in rows if r.get('Q Name','').lower()=='cluster' and r.get('list_name','').lower()=='ea']
summary=[r for r in cluster_ea if r.get('Issue type')=='cluster_ea_choice_changes_summary']
raw=[r for r in cluster_ea if r.get('Issue type') in {'added_option','removed_option','option_label_mismatch'}]
print(json.dumps({
  'report': str(report),
  'total_rows': len(rows),
  'cluster_ea_total_rows': len(cluster_ea),
  'cluster_ea_summary_rows': len(summary),
  'cluster_ea_detail_rows': len(raw),
  'cluster_ea_summary_sample': summary[0] if summary else None
}, ensure_ascii=False, indent=2))
