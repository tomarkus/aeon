from django.template.defaultfilters import slugify

from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-id',)

    @models.permalink
    def get_absolute_url(self):
        return ('post_detail', (), {
            'slug': self.slug,
            'pk': self.pk,
        })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title