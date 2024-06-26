trigger_file = '.HiMarko'

xia2_pipelines = ['default', 'user', 'ice', 'real_space_indexing']
dials_pipelines = ['max_lattices']
all_pipelines = xia2_pipelines + dials_pipelines

xia2_output_file = 'xia2.txt'

report_path_env_var = 'AUTOED_REPORT_PATH'

report_dir = 'autoed_report'
report_html_file = 'autoed_overview.html'
database_json_file = 'autoed_database.json'        # Keeps processing summaries
xia2_html_report_dir = 'xia2_html'                 # Keeps xia2 html reports
