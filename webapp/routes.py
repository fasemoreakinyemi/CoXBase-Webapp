def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=0)
    # landing page
    config.add_route('home', '/')
    # no entry
    config.add_route('No_entry', '/result/noentry/{item}')
    # api
    config.add_route('api', '/api')
    config.add_route('api_dashboard_year', '/api_country/{ID}')
    config.add_route('api_dashboard_host', '/api_host/{ID}')
    config.add_route('api_dashboard_province', '/api_province/{ID}')
    config.add_route('api_dashboard_genotype', '/api_genotype/{ID}')
    config.add_route('api_filter', '/api/{column}/{filter}/{filter_value}')
    config.add_route('api_column', '/api/{column}')
    config.add_route('dashboard', '/dashboard')
    config.add_route('dashboard_coxviewer', '/dashboard/{ID}')
    # query
    config.add_route('mlvaquery', '/query/mlva')
    config.add_route('mstquery', '/query/mst')
    # primer
    config.add_route('primerquery', '/query/primer')
    config.add_route('primerquery_results', '/primer_results/*selection')
    # insilico analysis submission page
    config.add_route('mlvaanalysis', '/analysis/mlva')
    config.add_route('mstanalysis', '/analysis/mst')
    config.add_route('is1111analysis', '/analysis/is1111')
    config.add_route('adaanalysis', '/analysis/adaA')
    config.add_route('combined', '/analysis/combined')
    config.add_route('SNPHanalysis', '/analysis/SNP/hornstra')
    # insilico form submission
    config.add_route('mlvaresult', '/result/mlva')
    config.add_route('mstresult', '/result/mst')
    config.add_route('is1111result', '/result/is1111')
    config.add_route('adaresult', '/result/adaA')
    config.add_route('combinedresult', '/result/combined')
    config.add_route('SNPHresult', '/result/SNP/hornstra')
    # insilico analysis result page
    config.add_route('resMLVA', '/result/mlva/{ID}')
    config.add_route('resMST', '/result/mst/{ID}')
    config.add_route('resis1111', '/result/is1111/{ID}')
    config.add_route('resadaA', '/result/adaA/{ID}')
    config.add_route('resCombined', '/result/combined/{ID}')
    config.add_route('resHornstra', '/result/SNP/hornstra/{ID}')
    # submission
    config.add_route('subMLVA', '/submissions/mlva/{ID}')
    config.add_route('subMST', '/submissions/mst/{ID}')
    config.add_route('subForm', '/submissions/form')
    config.add_route('subBulkForm', '/submissions/bulkform')
    config.add_route('subFormPrev', '/submissions/form/preview/{ID}')
    config.add_route('usersubmission', '/submissions')
    config.add_route('s_submission', '/submissions/single')
    config.add_route('b_submission', '/submissions/bulk')
    # phylogenetics
    config.add_route('phlMLVA', '/phyloanalysis/mlva/{ID}')
    config.add_route('phlMST', '/phyloanalysis/mst/{ID}')
    # coxviewer
    config.add_route('coxviewer', '/coxviewer')
    config.add_route('api_coxviewer', '/coxviewer_api')
    config.add_route('api_coxviewer2', '/coxviewer_api/{ID}')
    config.add_route('coxviewer_table', '/coxviewer_table/{ID}')
    # eview
    config.add_route('entry_view_mlva', '/eview/mlva/{ID}')
    config.add_route('entry_view_mlva_6', '/eview/mlva/tilburg/{ID}')
    config.add_route('entry_view_mst', '/eview/mst/{ID}')
    # typing query api
    #fp frangoulidis panel
    #tp tilburg panel
    config.add_route('fp_query_api', '/fp_query/{ms01}/{ms03}/{ms20}/{ms21}/{ms22}/{ms23}/{ms24}/{ms26}/{ms27}/{ms28}/{ms30}/{ms31}/{ms33}/{ms34}/{distance}')
    config.add_route('tp_query_api', '/tp_query/{ms23}/{ms24}/{ms27}/{ms28}/{ms33}/{ms34}/{distance}')
    config.add_route('mst_query_api', '/mst_query/{COX2}/{COX5}/{COX18}/{COX20}/{COX22}/{COX37}/{COX51}/{COX56}/{COX57}/{COX61}/{distance}')
    # maps api
    config.add_route('api_map', '/api_map/{column}/{state}')
    config.add_route('api_mlva_map', '/api_mlva_map/{ID}')
    config.add_route('api_mlva_tilburg_map', '/api_mlva_tilburg_map/{ID}')
    config.add_route('api_mst_map', '/api_mst_map/{ID}')
    # mlva panel api
    config.add_route('api_query3', '/api_query/{ms24}/{ms28}/{ms33}')
    config.add_route('api_query6', '/api_query/{ms23}/{ms24}/{ms27}{ms28}/{ms33}/{ms34}')
    config.add_route('api_query141', '/api_query/{ms01}/{ms03}/{ms07}/{ms20}/{ms21}/{ms22}/{ms24}/{ms26}/{ms27}/{ms28}/{ms30}/{ms31}/{ms33}/{ms34}')
    config.add_route('api_query15', '/api_query/{ms01}/{ms03}/{ms07}/{ms12}/{ms20}/{ms21}/{ms22}/{ms24}/{ms26}/{ms27}/{ms28}/{ms30}/{ms31}/{ms33}/{ms34}')
    config.add_route('api_query16', '/api_query/{ms01}/{ms03}/{ms07}/{ms12}/{ms20}/{ms21}/{ms22}/{ms24}/{ms26}/{ms27}/{ms28}/{ms30}/{ms31}/{ms33}/{ms34}/{ms36}')
    # sequence viewer
    config.add_route('sequenceviewer', '/sequenceviewer')
    # login signup logout
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('signup', '/signup')
    config.add_route('register', '/register')
    # help pages
    config.add_route('help', '/help')
    # retrieve 
    config.add_route('retrieve_submission', '/retrieve')
    config.add_route('retrieve_form', '/submit_retrieve')
    # mst blast
    config.add_route('blaster', '/blastn/{ID}/{spacer}')
    config.add_route('blast_api', '/blast_api/{ID}/{spacer}')
    # isolate discovery
    config.add_route('isolate_query', '/query/isolates')
    config.add_route('isolate_query_api', '/query/isolates/{cont}/{combo}')
    config.add_route('isolate_query_fc', '/query/isolates/faceted')
    config.add_route('isolate_fc_api', '/query/isolate/fc/api')
    # tree page analysis
    config.add_route('phyd3_tree', '/tree/phyd3/{ID}')
    config.add_route('phyd3_tree_api', '/tree/phyd3/API/{ID}')
    config.add_route('mlva_tree', '/tree/mlva/analysis/{ent}')
    config.add_route('mst_tree', '/tree/mst/analysis/{ent}')
    # tree viewer
    config.add_route('mlva_tree_2', '/tree/mlva')
    config.add_route('mlva_tree_3', '/tree/mlva_query')
    config.add_route('mst_tree_2', '/tree/mst/{ent}')
    config.add_route('mlva_result_tree', '/tree/mlva/{ID}')
    # miscellaneous
    config.add_route('news_api_homepage', '/newsAPI')
    config.add_route('news_api', '/newsAPI/{lang}/{search}')
    # multi marker analysis
    config.add_route('multi_marker', '/multimarker')
    config.add_route('multi_marker_result', '/result/multimarker')
    # antibiotic prediction page
    config.add_route('arg_pred', '/analysis/arg-prediction')
    # antibiotic fasta submision 
    config.add_route('arg_pred_api', '/result/arg-prediction')
    # antibiotic fasta task status
    config.add_route('res_arg_pred', '/status/arg-prediction/{ID}')
    # antibiotic fasta task page 
    config.add_route('res_arg_pred_page', '/result-status/arg-prediction/{ID}')


