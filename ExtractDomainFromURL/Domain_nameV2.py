def domain_name(url):

    url = url.replace("https://", "")
    url = url.replace("http://", "")
    url = url.replace("www.", "")

    return url[0:url.find(".")]
