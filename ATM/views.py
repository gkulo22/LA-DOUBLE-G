from django.shortcuts import render
from django.http import JsonResponse
from .models import ATM

def atm_locators(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        my_id = request.POST.get('id')

        atm = ATM.objects.get(id=my_id)
        atm_dict = atm.to_dict()

        denominations = {
            5: atm_dict['5'],
            10: atm_dict['10'],
            20: atm_dict['20'],
            50: atm_dict['50'],
            100: atm_dict['100'],
            200: atm_dict['200'],
        }

        numbers = []

        for num, quantity in denominations.items():
            print([num] * quantity)
            numbers.extend([num] * quantity)

        print(numbers)

        if can_find_subset_sum(denominations, int(amount)):
            return JsonResponse({'status': 'success', 'message': 'Amount is available.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Insufficient funds.'})

    return render(request, 'AtmLocations.html')


def can_find_subset_sum(m, target):
    # Get available denominations and their counts
    coins = list(m.keys())
    counts = list(m.values())

    # Create a DP array where dp[j] means "is sum j achievable"
    dp = [False] * (target + 1)
    dp[0] = True  # Base case: sum of 0 is always achievable with no coins

    # Iterate over each coin and its count
    for coin, count in zip(coins, counts):
        # Create a temporary copy of the dp array to avoid using the same coin multiple times
        temp_dp = dp[:]
        for current_sum in range(target + 1):
            if dp[current_sum]:
                # Try adding the coin up to 'count' times without exceeding 'target'
                for k in range(1, count + 1):
                    new_sum = current_sum + k * coin
                    if new_sum <= target:
                        temp_dp[new_sum] = True
                    else:
                        break
        dp = temp_dp

    return dp[target]
