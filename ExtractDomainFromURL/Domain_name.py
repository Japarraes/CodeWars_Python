def domain_name(url):

    domain = url

    # Find if "https://"
    url_list = domain.split("https://")
    if (len(url_list) > 1):
        domain = url_list[1]
    
    # Find if "http://"
    url_list = domain.split("http://")
    if (len(url_list) > 1):
        domain = url_list[1]
        
    # Find if "www."
    url_list = domain.split("www.")
    if (len(url_list) > 1):
        domain = url_list[1]

    # Find if "."
    url_list = domain.split(".")
    domain = url_list[0]
    
    return domain
