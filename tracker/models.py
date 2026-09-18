from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    Name=models.CharField(max_length=50)
    class Meta:
        verbose_name_plural="Categories"

    def __str__(self):
        return self.Name

class Expense(models.Model):
    transaction_types =(
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
    )
    User=models.ForeignKey(User, on_delete=models.CASCADE)
    Title=models.CharField(max_length=200)
    Amount=models.DecimalField(max_digits=10, decimal_places=2)
    Category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    Transaction_type=models.CharField(max_length=10, choices=transaction_types, default='EXPENSE')
    Date=models.DateField()
    Created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Title} - ₹{self.Amount}"