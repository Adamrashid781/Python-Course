from django.db import models

# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=60, default="", blank=True, null=False)
    last_name = models.CharField(max_length=60, default="", blank=True, null=False)
    initial_deposit = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    
    # Creates model manager
    object = models.Manager()
    
    # Displays the object output values in the form of a string 
    def __str__(self):
        display_account = '{0.first_name}: {0.last_name}'
        return display_account.format(self)

TransactionTypes = [('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')]

class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=10, choices=TransactionTypes)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    # Defines the model manager for Transactions
    Transactions = models.Manager()
    