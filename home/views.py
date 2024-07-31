from django.views.generic import TemplateView


# Create your views here.
class HomePage(TemplateView):
    """
    View to render the home page.
    """
    template_name = 'home/index.html'


