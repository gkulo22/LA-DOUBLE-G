from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Transaction, PiggyBank

@login_required
def piggybank_view(request):
    piggybank, created = PiggyBank.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Handle the creation of a transaction (rounding up and saving change)
        if 'create_transaction' in request.POST:
            amount = request.POST.get('amount')

            try:
                amount = float(amount)
                if amount > 0:
                    # Calculate the change (round to the next integer and subtract the original amount)
                    change = round(amount) - amount

                    # Create and save the transaction
                    Transaction.objects.create(user=request.user, amount=amount)

                    # Update the piggy bank balance
                    piggybank.balance += change
                    piggybank.save()

                    messages.success(request,
                                     f'Transaction of {amount} created, and {change} saved to your PiggyBank!')
                    return redirect('piggybank_view')
                else:
                    messages.error(request, 'Amount must be greater than 0')
            except ValueError:
                messages.error(request, 'Invalid amount entered')

        # Handle disabling the piggy bank
        elif 'disable_piggybank' in request.POST:
            piggybank.delete()
            messages.success(request, 'Your PiggyBank has been disabled.')
            return redirect('piggybank_view')

        # Handle transferring money to the main bank account
        elif 'transfer_money' in request.POST:
            transfer_amount = piggybank.balance
            # Assuming main bank account logic is implemented elsewhere
            piggybank.balance = 0
            piggybank.save()

            # Here, you would add logic for transferring to the user's bank account
            # For simplicity, we're just displaying a success message
            messages.success(request, f'{transfer_amount} has been transferred to your main bank account.')

    return render(request, 'PiggyBank.html', {'piggybank': piggybank, 'created': created})