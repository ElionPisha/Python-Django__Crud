from django.contrib import admin

# Register your models here.
from app.models import UserInfo, Books, UserBook, Category, UserAccess

admin.site.register(UserInfo)
admin.site.register(Books)
admin.site.register(UserBook)
admin.site.register(Category)
admin.site.register(UserAccess)
