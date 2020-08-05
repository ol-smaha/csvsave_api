from django.db import models


class Order(models.Model):
    created_date = models.DateField()
    product = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.product} - {self.created_date}'


class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birth_date = models.DateField()
    registration_date = models.DateField()
    order = models.OneToOneField(Order,
                                 blank=True,
                                 null=True,
                                 on_delete=models.SET_NULL)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name

