def get_user_agent(request):
    """A function that gets the visitor's user agent"""

    userAgent = request.META['HTTP_USER_AGENT']

    return userAgent
