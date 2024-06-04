def get_ip(request):
    """A function that gets visitor's ip address"""

    # Get the visitor's ip address with reverse proxy support(Get the visitor's ip address eventhough if there is a reverse proxy such a Nginx between the client and django.)
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:

        ip = x_forwarded_for.split(',')[0]

    # Get the visitory's ip address with direct access only
    else:

        ip = request.META.get('REMOTE_ADDR')
        
    return ip
