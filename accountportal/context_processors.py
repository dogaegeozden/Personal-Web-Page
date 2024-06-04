# MODELS
from .models import (
    LoginPageMetaDescription,
    LogoutPageMetaDescription,
    PasswordResetCompletePageMetaDescription,
    PasswordResetConfirmPageMetaDescription,
    PasswordResetDonePageMetaDescription,
    PasswordResetFormPageMetaDescription,
)


# CONTEXT PROCESSORS

def account_portal_meta_description_processor(request):
    """A context processor function which makes account portal meta descriptions accessible in all pages."""

    all_login_page_meta_descriptions = LoginPageMetaDescription.objects.all()
    all_logout_page_meta_descriptions = LogoutPageMetaDescription.objects.all()
    all_password_reset_complete_meta_description = PasswordResetCompletePageMetaDescription.objects.all()
    all_password_reset_confirm_meta_description = PasswordResetConfirmPageMetaDescription.objects.all()
    all_password_reset_done_page_meta_description = PasswordResetConfirmPageMetaDescription.objects.all()
    all_password_reset_form_page_meta_description = PasswordResetFormPageMetaDescription.objects.all()

    context = {

        'all_login_page_meta_descriptions': all_login_page_meta_descriptions,
        'all_logout_page_meta_descriptions': all_logout_page_meta_descriptions,
        'all_password_reset_complete_meta_description': all_password_reset_complete_meta_description,
        'all_password_reset_confirm_meta_description': all_password_reset_confirm_meta_description,
        'all_password_reset_done_page_meta_description': all_password_reset_done_page_meta_description,
        'all_password_reset_form_page_meta_description': all_password_reset_form_page_meta_description,

    }

    return context