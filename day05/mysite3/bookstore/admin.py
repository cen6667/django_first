from django.contrib import admin
from .models import Book, Author
# Register your models here.


class BookManager(admin.ModelAdmin):
    # 字段显示哪些字段的列
    list_display = ['id', 'title', 'pub', 'price']
    # 控制list_display中的字段，哪些可以链接到修改页
    list_display_links = ['title']
    # 过滤器
    list_filter = ['pub']
    # 搜索框[模糊查询]
    search_fields = ['title']
    # 添加可在列表页编辑的字段
    list_editable = ['price']


class AuthorManager(admin.ModelAdmin):
    # 字段显示哪些字段的列
    list_display = ['id', 'name', 'age']


admin.site.register(Author, AuthorManager)
admin.site.register(Book, BookManager)
