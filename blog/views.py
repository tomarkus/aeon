from django.views.generic.base import TemplateView

class Index(TemplateView):
    template_name = 'index.html'
index = Index.as_view()

class About(TemplateView):
    template_name = 'about.html'
about = About.as_view()

class Music(TemplateView):
    template_name = 'music.html'
music = Music.as_view()

class Contact(TemplateView):
    template_name = 'contact.html'
contact = Contact.as_view()
