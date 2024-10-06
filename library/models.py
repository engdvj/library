from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    publication_date = models.DateField()
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
