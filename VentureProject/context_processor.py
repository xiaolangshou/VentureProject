def get_remote_addr(request):
    return {'remote_addr': request.META['REMOTE_ADDR']}
