def dict2url(data: dict):
    url = data.pop('url',None) + '?'
    for k,v in data.items():
        url += k + '=' + v + '&'
    return url