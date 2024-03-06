from django.shortcuts import render, redirect 
from .forms import AccountForm, TransactionForm 

# Create your views here.
# this function will render the home page when requested 
def home(request):
    return render(request, 'checkbook/index.html')

# this function will render the Create New Account page when requested
def create_account(request):
    return render(request, 'checkbook/CreateNewAccount.html')

# this function will render the Balance Sheet page when requested
def balance(request):
    return render(request, 'checkbook/BalanceSheet.html')

# This function will render the Transaction page when requested
def transaction(request):
    return render(request, 'checkbook/AddTransaction.html')


# This function will render the Create New Account page when requested
def create_account(request):
    print('Inside the create account method in views file')
    form = AccountForm(data=request.POST or None) # Retrieve the account form
    # Checks if request method is POST 
    if request.method == 'POST':
        if form.is_valid(): # Check to see if the submitted form is valid and if so, saves the form
            form.save() # Saves new account 
            return redirect('index') # Returns user back to the home page
    content = {'form': form} # Saves content to the template as a dictionary
    # adds content of form to the page
    return render(request, 'checkbook/CreateNewAccount.html', content)

# This function will render the Transaction page when requested 
def transaction(request):
    form = TransactionForm(data=request.POST or None) # Retrieve the transaction form
    # Checks if request method is POST
    if request.method == 'POST':
        if request.is_valid(): # Check to see if the submitted form is valid and if so, saves the form
            form.save() # Saves new transaction form
            return redirect('index') # Returns user back to the home page
    # Pass content to the template in a dictionary 
    content = {'form': form}
    # Adds content of form to the page 
    return render(request, 'checkbook/AddTransaction.html', content)