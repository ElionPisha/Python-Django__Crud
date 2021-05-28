from django.shortcuts import render, redirect

from app.models import Books, UserInfo, UserBook, UserAccess


def index(request):
    if request.method == 'GET':
        books = Books.objects.all()
        user_info = UserInfo.objects.all()
        user_book = UserBook.objects.all()
        return render(request, 'index.html', {'books_data': books,
                                              'users_data': user_info,
                                              'user_book_data': user_book})


def add_book(request):
    if request.method == 'GET':
        return render(request, 'add_books.html')
    elif request.method == 'POST':
        book_name = request.POST.get('book_name', None)
        book_description = request.POST.get('book_desc', None)
        book_price = request.POST.get('book_price', None)

        if book_name and book_price and book_description:
            Books.objects.create(book_name=book_name, book_price=book_price, book_description=book_description)
            # b = Books(
            #     book_name=book_name,
            #     book_price=book_price,
            #     book_description=book_description
            # )
            #
            # b.save()

        return redirect('index')


def delete_book(request, book):
    b = Books.objects.filter(id=book)

    if b.exists():
        b.delete()

    return redirect('index')


def edit_book(request, book):
    if request.method == 'GET':
        b = Books.objects.get(id=book)
        return render(request, 'edit_books.html', {'book': b})

    elif request.method == 'POST':
        book_name = request.POST.get('book_name', None)
        book_description = request.POST.get('book_desc', None)
        book_price = request.POST.get('book_price', None)
        b = Books.objects.get(id=book)

        b.book_name = book_name
        b.book_description = book_description
        b.book_price = book_price
        b.save()

    return redirect('index')


def UserAccess(request):
    if request.method == 'GET':
        books = Books.objects.all()
        user_info = UserInfo.objects.all()
        user_book = UserBook.objects.all()
        return render(request, 'user.html', {'books_data': books,
                                             'users_data': user_info,
                                             'user_book_data': user_book})
    elif request.method == 'POST':
        book_name = request.POST.get('book_name', None)
        book_description = request.POST.get('book_desc', None)
        book_price = request.POST.get('book_price', None)

    return redirect('user.html')