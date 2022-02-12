from django.shortcuts import render
from .models import Book
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect


def all_book(request):
    # all_book = Book.objects.all()
    all_book = Book.objects.filter(is_active=True)
    #  locals()把函数内部所有局部变量传进去
    return render(request, 'bookstore/all_book.html', locals())


def update_book(request, book_id):
    # bookstore/update_book/1
    try:
        book = Book.objects.get(id=book_id, is_active=True)
    except Exception as e:
        print('--update book error is %s' % e)
        return HttpResponse('The book is not existed')

    if request.method == 'GET':
        return render(request, 'bookstore/update_book.html', locals())
    elif request.method == 'POST':
        book.price = request.POST.get('price')

        book.market_price = request.POST.get('market_price')

        book.save()

        return HttpResponseRedirect('/bookstore/all_book')


def delete_book(request):
    # 通过获取查询字符串 book_id 拿到要删除的book的id
    book_id = request.GET.get('book_id')
    if not book_id:
        return HttpResponse('----请求异常')
    try:
        book = Book.objects.get(id=book_id, is_active=True)
    except Exception as e:
        print('---delete book get error %s ---' % e)
        return HttpResponse('---The book is error---')
    # 将其is_active 改成False
    book.is_active = False
    book.save()
    # 302跳转至all_book
    return HttpResponseRedirect('/bookstore/all_book')


