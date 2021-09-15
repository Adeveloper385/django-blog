from django.db import models
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField

class Category(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Category Name',max_length = 50, null = False, blank = False)
    state = models.BooleanField('Activate/Deactivate', default = True)
    created_at = models.DateField('Created at', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Author(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField("Author's Name",max_length = 255, null = False, blank = False)
    last_name = models.CharField("Author's Last Name",max_length = 255, null = False, blank = False)
    facebook = models.URLField('Facebook', null = True, blank = True)
    twitter = models.URLField('Twitter', null = True, blank = True)
    instagram = models.URLField('Instagram', null = True, blank = True)
    web = models.URLField('Web', null = True, blank = True)
    email = models.EmailField('Email', blank = False, null = False)
    state = models.BooleanField('Is Active', default = True)
    created_at = models.DateField('Created at', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return f"{self.name} {self.last_name}"

class Post(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField('Title', max_length = 100, null = False, blank = False)
    slug = models.CharField('Slug', max_length = 100, null = False, blank = False)
    description = models.CharField('Description', max_length = 255, null = False, blank = False)
    content = RichTextField('Content')
    image = models.URLField('Image', blank = False, null = False)
    author = models.ForeignKey(Author, on_delete=CASCADE)
    category = models.ForeignKey(Category, on_delete=CASCADE)
    state = models.BooleanField('Active/Disabled', default=True)
    created_at = models.DateField('Created at', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
