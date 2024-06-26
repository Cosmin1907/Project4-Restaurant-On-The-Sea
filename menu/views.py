from django.views.generic import TemplateView

# Create your views here.

class MenuPage(TemplateView):
    template_name = 'menu/menu.html'