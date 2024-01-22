from django.db import models
from ckeditor.fields import RichTextField
from add.models import Category


class Posts(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="photos/blogs/%y/%m/%d")
    thumbnail_alt_text = models.CharField(
        max_length=150, blank=True, verbose_name="Thumbnail Alt Text"
    )
    author_name = models.CharField(max_length=50, verbose_name="Author Name")
    post = RichTextField()
    published_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Published Date"
    )
    show_on_slider = models.BooleanField(default=False, verbose_name="Show on Slider")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Comments(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    email = models.EmailField(verbose_name="Email Address")
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Timestamp")
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False, verbose_name="Approved")

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"Comment by {self.first_name} {self.last_name} on {self.post.title}"
