from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import (
    Wish,
    Subscription,
    Bills,
    FriendlyLoan
)
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)


class WishListView(LoginRequiredMixin, ListView):
    model = Wish
    template_name = 'WishList.html'
    context_object_name = 'wishes'
    ordering = ['-date']

    def get_queryset(self):
        user_id = self.request.user.id
        return Wish.objects.filter(author_id=user_id).order_by('-date')


class SubscriptionsListView(LoginRequiredMixin, ListView):
    model = Subscription
    template_name = "SubscriptionList.html"
    context_object_name = 'subscriptions'
    ordering = ['-date']

    def get_queryset(self):
        user_id = self.request.user.id
        return Subscription.objects.filter(author_id=user_id).order_by('-date')


class BillsListView(LoginRequiredMixin, ListView):
    model = Bills
    template_name = "BillsList.html"
    context_object_name = 'bills'
    ordering = ['-date']

    def get_queryset(self):
        user_id = self.request.user.id
        return Bills.objects.filter(author_id=user_id).order_by('-date')


class FriendlyLoanListView(LoginRequiredMixin, ListView):
    model = FriendlyLoan
    template_name = "FriendlyLoanList.html"
    context_object_name = 'loans'
    ordering = ['-date']

    def get_queryset(self):
        user_id = self.request.user.id
        return FriendlyLoan.objects.filter(author_id=user_id).order_by('-date')


class WishCreateView(LoginRequiredMixin, CreateView):
    model = Wish
    template_name = 'WishAdd.html'
    fields = ['name', 'price']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class WishUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Wish
    template_name = 'WishUpdate.html'
    fields = ['name', 'price']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        wish = self.get_object()
        if self.request.user == wish.author:
            return True
        return False


class WishDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Wish
    template_name = 'WishDelete.html'
    success_url = '/wishlist'

    def test_func(self):
        wish = self.get_object()
        if self.request.user == wish.author:
            return True
        return False


class SubscriptionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Subscription
    template_name = 'SubscriptionDelete.html'
    success_url = '/'

    def test_func(self):
        wish = self.get_object()
        if self.request.user == wish.author:
            return True
        return False


class BillDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Bills
    template_name = 'BillDelete.html'
    success_url = '/'

    def test_func(self):
        wish = self.get_object()
        if self.request.user == wish.author:
            return True
        return False



def bill_delete_view(request, id):
    if request.method == 'POST':
        bill = Bills.objects.get(pk=id)


    return None

class LoanDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = FriendlyLoan
    template_name = 'FriendlyLoanDelete.html'
    success_url = '/friendly_loans'

    def test_func(self):
        wish = self.get_object()
        if self.request.user == wish.author:
            return True
        return False