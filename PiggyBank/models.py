from django.db import models
from django.contrib.auth.models import User
import math

class PiggyBank(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='piggybank')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username}'s PiggyBank - Balance: {self.balance}"

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # The actual transaction amount
    rounded_up_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.rounded_up_amount = math.ceil(self.amount)  # Round up the amount to the nearest integer
        super().save(*args, **kwargs)
        self.update_piggybank()  # Update piggy bank balance after saving the transaction

    def update_piggybank(self):
        # Calculate the difference between the rounded-up amount and the actual amount
        piggy_amount = self.rounded_up_amount - self.amount
        # Get or create a PiggyBank for the user
        piggybank, created = PiggyBank.objects.get_or_create(user=self.user)
        # Update the PiggyBank balance
        piggybank.balance += piggy_amount
        piggybank.save()

    def __str__(self):
        return f"Transaction of {self.amount} by {self.user.username} (Rounded up to {self.rounded_up_amount})"