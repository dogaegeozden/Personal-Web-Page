from pages.models import GlobalSocialMediaButtonClick

def social_media_button_click_processor(request, id, ip, user_agent, platform_choice, page_url):

    if request.POST.get("id") == id:

        GlobalSocialMediaButtonClick.objects.create(ip_address=ip, user_agent=user_agent, platform_choice=platform_choice, page_url=page_url)
