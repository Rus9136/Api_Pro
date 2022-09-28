from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Категория")
        verbose_name_plural = ("Категории")


class Income(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sum = models.IntegerField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)
    choices_cat = [('EF', 'Eврофарма'), ('CF', 'Центр софт'), ('DO', 'Доп доходы')]
    cat = models.CharField(max_length=255, choices=choices_cat, default=None)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("Доход")
        verbose_name_plural = ("Доходы")


class Expenses(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sum = models.IntegerField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)
    comment = models.CharField(max_length=255, blank=True, null=True)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("Расход")
        verbose_name_plural = ("Расходы")


