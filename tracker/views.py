from django.shortcuts import render,redirect
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    expenses=Expense.objects.all().order_by('-Date')

    Total_income=Expense.objects.filter(Transaction_type='INCOME').aggregate(Sum('Amount'))['Amount__sum'] or 0
    Total_expense=Expense.objects.filter(Transaction_type='EXPENSE').aggregate(Sum('Amount'))['Amount__sum'] or 0
    Balance=Total_income - Total_expense

    context={
        'expenses':expenses,
        'Total_income':Total_income,
        'Total_expense':Total_expense,
        'Balance':Balance

    }
    return render(request, 'tracker/home.html', context)

def add_expense (request):
    if request.method =='POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.User = request.user if request.user.is_authenticated else User.objects.first()
            expense.save()
            return redirect('home')
    else:
            form = ExpenseForm()

    return render(request, 'tracker/add_expense.html', {'form':form})