from django.db import models


class UserInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.CharField(max_length=8)
    mobile_number = models.CharField(max_length=11)
    email = models.EmailField()

    def __str__(self):
        return self.email


class Category(models.Model):
    name = models.CharField(max_length=200)


class Books(models.Model):
    book_name = models.CharField(max_length=100)
    book_description = models.TextField()
    book_price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{0} - {1}'.format(self.book_name, self.book_price)


class UserBook(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} - {1}'.format(self.user.email, self.book.book_name)


class UserAccess(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=11)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

