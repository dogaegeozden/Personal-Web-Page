from pages.models import GlobalDocumentClickCoordinate

def document_click_coordinate_processor(request, id, ip, user_agent, screen_width, screen_height, x_coordinate, y_coordinate, page_url):

    if request.POST.get("id") == "document_click_coordinate_request":

        GlobalDocumentClickCoordinate.objects.create(ip_address=ip, user_agent=user_agent, screen_width=screen_width, screen_height=screen_height, x_coordinate=x_coordinate, y_coordinate=y_coordinate, page_url=page_url)
