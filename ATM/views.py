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

        if subset_sum_exists(numbers, int(amount)):
            return JsonResponse({'status': 'success', 'message': 'Amount is available.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Insufficient funds.'})

    return render(request, 'AtmLocations.html')


def subset_sum_exists(numbers, target, index=0):
    if target == 0:
        return True

    if target < 0 or index >= len(numbers) or len(numbers) == 0 or target < numbers[index]:
        return False

    include = subset_sum_exists(numbers, target - numbers[index], index + 1)
    exclude = subset_sum_exists(numbers, target, index + 1)

    return include or exclude
