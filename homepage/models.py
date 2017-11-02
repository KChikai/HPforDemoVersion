from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


class New(models.Model):
    date = models.DateField()
    text_ja = models.TextField(max_length=400, blank=True)
    text_en = models.TextField(max_length=400, blank=True)
    image = models.ImageField(upload_to="./images", blank=True)


@python_2_unicode_compatible
class Paper(models.Model):
    title = models.CharField(max_length=100)  # 論文名
    year = models.DecimalField(max_digits=4, decimal_places=0)  # 発行年
    colloquium = models.CharField(max_length=100)  # 学会名
    abstract = models.CharField(max_length=500, null=True)  # アブスト
    volume = models.CharField(max_length=100, null=True)  # 巻数
    number = models.PositiveIntegerField(null=True)  # 号数
    # ページ、文献種類

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(max_length=100)
    papers = models.ManyToManyField(Paper)

    def __str__(self):
        return self.name