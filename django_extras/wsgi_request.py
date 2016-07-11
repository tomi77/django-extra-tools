PRIVATE_IPS_PREFIX = ('10.', '172.', '192.', )


def get_client_ip(request):
    """
    Get the client IP from the request
    """
    # set the default value of the ip to be the REMOTE_ADDR if available
    # else None
    ip = request.META.get('REMOTE_ADDR')
    # try to get the first non-proxy ip (not a private ip) from the
    # HTTP_X_FORWARDED_FOR
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        proxies = x_forwarded_for.split(',')
        # remove the private ips from the beginning
        while len(proxies) > 0 and proxies[0].startswith(PRIVATE_IPS_PREFIX):
            proxies.pop(0)
        # take the first ip which is not a private one (of a proxy)
        if len(proxies) > 0:
            ip = proxies[0]

    return ip
