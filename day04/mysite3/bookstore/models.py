from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField("书名", max_length=50, default='', unique=True)
    pub = models.CharField("出版社", max_length=100, default='')
    price = models.DecimalField('定价', max_digits=7, decimal_places=2,
                                default=0.0)
    market_price = models.DecimalField("零售价", max_digits=7, decimal_places=2, default=0.0)
    info = models.CharField("描述", max_length=100, default='')


    class Meta:
        # 默认表名为app名_类名
        db_table = 'book'


class Author(models.Model):
    name = models.CharField("名字", max_length=11)
    age = models.IntegerField("年龄", default=1)
    email = models.EmailField("邮箱", null=True)

    class Meta:
        db_table = 'author'
