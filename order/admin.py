import csv
import io
from datetime import datetime

from django import forms
from django.urls import path
from django.contrib import admin
from django.shortcuts import redirect, render

from .models import Order, User


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'created_date', 'user']


class UserAdmin(admin.ModelAdmin):
    change_list_template = 'custom/user_changelist.html'
    list_display = ['first_name', 'last_name',
                    'birth_date', 'registration_date', 'has_order']

    def has_order(self, obj):
        if obj.order:
            return True
        return False

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-users-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES['csv_file']
            csv_file.seek(0)
            reader = csv.DictReader(io.StringIO(csv_file.read().decode('utf-8')))

            for row in reader:
                user_kw = {
                    'first_name': row.get('FirstName'),
                    'last_name': row.get('LastName'),
                    'birth_date': datetime.strptime(row.get('BirthDate'), '%Y/%m/%d'),
                    'registration_date': datetime.strptime(row.get('RegistrationDate'), '%Y/%m/%d'),
                }
                try:
                    User.objects.create(**user_kw)
                except Exception as e:
                    self.message_user(request, f"Some users were not created. Error: {e}")

            self.message_user(request, "Users from csv file has been imported")
            return redirect("..")

        form = CsvImportForm()
        ctx = {"form": form}
        return render(request, "custom/csv_form.html", ctx)


admin.site.register(Order, OrderAdmin)
admin.site.register(User, UserAdmin)
