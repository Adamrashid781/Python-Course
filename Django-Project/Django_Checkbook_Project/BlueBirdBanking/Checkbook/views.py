from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm 
from .models import Account, Transaction

# Create your views here.
# this function will render the home page when requested 
def home(request):
    form = TransactionForm(data=request.POST or None) # Retrieve the transaction form
    # Checks if request method is POST
    if request.method == 'POST':
        pk = request.POST['account'] # if the form is submitted, retrieve  which account the user wants to view 
        return balance(request, pk) # Call balance function to render that accounts balance sheet page
    content = {'form': form} # Pass content to the template in a dictionary
    # Adds content of form to page 
    return render(request, 'checkbook/index.html', content)

# this function will render the Create New Account page when requested
def create_account(request):
    return render(request, 'checkbook/CreateNewAccount.html')

# this function will render the Balance Sheet page when requested
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk) # retrieve the requested account using its primary key
    transactions = Transaction.Transactions.filter(account=pk) # retrieve all of the transactions for the requested account
    current_total = account.initial_deposit # Create account total variable, starting with initial deposite value
    table_contents = {} # Create dictionary into which transactions will be placed 
    for t in transactions: # Loop through transactions and determine which is a deposite or withdrawal
        if t.type == 'Deposit':
            current_total += t.amount # If transaction is a deposit, add the amount to the account total
            table_contents.update({t: current_total}) # add transaction and total to the dictionary 
        else: 
            current_total -= t.amount # If transaction is a withdrawal, subtract the amount from the account total
            table_contents.update({t: current_total}) # add transaction and total to the dictionary
        
        # Pass account, account total balance, and transaction information to the template 
        content = {'account':account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)

# This function will render the Transaction page when requested
def transaction(request):
    if request.method == 'POST':
        if form.is_valid(): # Check to see if the submitted form is valid and if so, saves the form
            pk = request.POST['account'] # Retrieve which account the transaction was for
            form.save() # Saves new transaction form
            return balance(request, pk) # Renders balance of the accounts Balance sheet
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
        if form.is_valid(): # Check to see if the submitted form is valid and if so, saves the form
            form.save() # Saves new transaction form
            return redirect('index') # Returns user back to the home page
    # Pass content to the template in a dictionary 
    content = {'form': form}
    # Adds content of form to the page 
    return render(request, 'checkbook/AddTransaction.html', content)