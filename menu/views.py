from django.views.generic import TemplateView


# Create your views here.
class MenuPage(TemplateView):
    """
    View to render the menu page.
    """
    template_name = 'menu/menu.html'