import sys
from pathlib import Path
import polars as pl
script_path = Path(r"c:\git\DIEM_Questionnaire_Validation\scripts\kobo_validator.py")
g = {"__file__": str(script_path), "__name__": "__main__"}
code = script_path.read_text(encoding='utf-8')
try:
    exec(compile(code, str(script_path), 'exec'), g)
except Exception:
    pass
sys.stdout = sys.__stdout__
a = g['all_issues']
focus = ['choice_label_mismatch','added_choice','removed_choice','option_index_drift','option_name_dictionary_replaced','removed_option_causes_index_drift']
print(a.filter(pl.col('issue_type').is_in(focus)).group_by('issue_type').agg(pl.len().alias('n')).sort('issue_type'))
root_keys = a.filter(pl.col('issue_type').is_in(['removed_option_causes_index_drift','option_name_dictionary_replaced'])).select(['Q Name','list_name']).unique()
print('root_keys', root_keys.height)
print(root_keys.sort(['Q Name','list_name']))
lm_on_root = a.join(root_keys, on=['Q Name','list_name'], how='inner').filter(pl.col('issue_type')=='choice_label_mismatch')
print('label mismatch on root keys', lm_on_root.height)
print('added severities', a.filter(pl.col('issue_type')=='added_choice').select('severity').unique())
