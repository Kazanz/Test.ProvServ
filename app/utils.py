def get_ip(request):
    """Returns string of clients IP Adress."""
    x_forwarded_for = request.environ.get('HTTP_X_FORWARDED_FOR')
    x_real_ip = request.environ.get('HTTP_X_REAL_IP')
    remote_addr = request.environ.get('REMOTE_ADDR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    elif x_real_ip:
        ip = x_real_ip
    else:
        ip = remote_addr
    return ip
