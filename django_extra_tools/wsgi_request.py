from django_extra_tools.conf import settings


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
        proxies = [proxy for proxy in proxies
                   if not proxy.startswith(settings.PRIVATE_IPS_PREFIX)]
        # take the first ip which is not a private one (of a proxy)
        if len(proxies) > 0:
            ip = proxies[0]

    return ip
