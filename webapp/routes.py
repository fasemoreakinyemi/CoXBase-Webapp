def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=1)
    config.add_route('home', '/')
    config.add_route('No_entry', '/result/noentry/{item}')
    config.add_route('api', '/api')
    config.add_route('api_filter', '/api/{column}/{filter}/{filter_value}')
    config.add_route('api_column', '/api/{column}')
    config.add_route('dashboard', '/dashboard')
    config.add_route('mlvaquery', '/mlvaquery')
    config.add_route('api_map', '/api_map/{column}/{state}')

