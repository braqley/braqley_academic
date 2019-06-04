from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ResearchPageView(TemplateView):
    template_name = 'research.html'

class CoursesPageView(TemplateView):
    template_name = 'courses.html'

class MiscPageView(TemplateView):
    template_name = 'misc.html'