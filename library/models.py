from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)
    birth_date = models.DateField(null=True, blank=True)  # Aceitar valores nulos
    publication_date = models.DateTimeField(null=True, blank=True)  # Aceitar valores nulos


    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=250, unique=True)
    category = models.ForeignKey(Category, related_name="books", on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name='books')  # Relacionamento muitos para muitos
    publication_date = models.DateTimeField()
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
