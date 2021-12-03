from django.contrib import admin
from .models import AddBooks, IssueBook, Returnbook

# Register your models here.
admin.site.register(IssueBook)
admin.site.register(AddBooks)
admin.site.register(Returnbook)
