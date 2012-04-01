from django.views.generic import TemplateView, ListView, DetailView
from aeon.blog import models

class PostList(ListView):
    model = models.Post
    template_name = 'index.html'
    paginate_by = 4

    def get(self, *args, **kwargs):
        return super(PostList, self).get(*args, **kwargs)

index = PostList.as_view()

class PostDetail(DetailView):
    model = models.Post
    template_name = 'post_detail.html'

post_detail = PostDetail.as_view()

class About(TemplateView):
    template_name = 'about.html'
about = About.as_view()

class Music(TemplateView):
    template_name = 'music.html'
music = Music.as_view()

class Contact(TemplateView):
    template_name = 'contact.html'
contact = Contact.as_view()
