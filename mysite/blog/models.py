from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):  # Fixed ".Model" to ".Model()"
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )  # Added closing parenthesis for STATUS_CHOICES

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")  # Fixed double quote and spacing
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:  # Fixed "Class" to "class"
        ordering = ('-publish',)  # Fixed spacing

    def __str__(self):  # Fixed "_str_" to "__str__"
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year,
                                                 self.publish.month,
                                                 self.publish.day,
                                                 self.slug])
