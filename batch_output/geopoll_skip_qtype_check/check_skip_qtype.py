import openpyxl, json
from collections import Counter, defaultdict
from pathlib import Path
p=Path(r"""C:/git/DIEM_Questionnaire_Validation/batch_output/geopoll_skip_qtype_check/geopoll_output/report_geopoll_ar_YEM_R605_20260508.xlsx""")
wb=openpyxl.load_workbook(p,data_only=True,read_only=True)

ws=wb['Questionnaire Structure']
header=None
issue_by_q=defaultdict(list)
counts=Counter()
for row in ws.iter_rows(values_only=True):
    vals=["" if v is None else str(v).strip() for v in row]
    if 'Issue type' in vals and 'Severity' in vals and 'Q Name' in vals:
        header={v:i for i,v in enumerate(vals) if v}
        continue
    if header and any(vals):
        it=vals[header['Issue type']]
        q=vals[header['Q Name']]
        sv=vals[header['Severity']].lower()
        if not it or it=='No issues in this category':
            continue
        counts[(it,sv)] += 1
        issue_by_q[q].append((it,sv))

dup_q_with_high_and_info=[]
for q, items in issue_by_q.items():
    has_high = any(sv=='high' for _,sv in items)
    has_info_change = any((it in {'skipPattern_changes','default_skip_modified','skipPattern_range_mismatch'} and sv=='info') for it,sv in items)
    if has_high and has_info_change:
        dup_q_with_high_and_info.append(q)

qtype=Counter()
for (it,sv),n in counts.items():
    if it=='qtype_changed':
        qtype[sv]+=n

print(json.dumps({
  'skip_counts': {f'{k[0]}|{k[1]}':v for k,v in counts.items() if k[0].startswith('skip') or k[0]=='default_skip_modified'},
  'qnames_with_high_and_info_skip_dup': dup_q_with_high_and_info,
  'qtype_severity_counts': dict(qtype)
}, ensure_ascii=False, indent=2))
