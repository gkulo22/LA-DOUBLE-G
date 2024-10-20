from django.urls import path
from .views import (
    WishListView,
    SubscriptionsListView,
    BillsListView,
    FriendlyLoanListView,
    WishCreateView,
    WishUpdateView,
    WishDeleteView,
    SubscriptionDeleteView,
    LoanDeleteView,
    BillDeleteView,
    bill_delete_view,
)

urlpatterns = [
    path('wishlist', WishListView.as_view(), name='wishlist'),
    path('subscriptions', SubscriptionsListView.as_view(), name='subscriptions'),
    path('friendlyloans', FriendlyLoanListView.as_view(), name='friendly_loans'),
    path('bills', BillsListView.as_view(), name='bills'),
    path('newwish', WishCreateView.as_view(), name='wish_create'),
    path('wishlist/<int:pk>/update', WishUpdateView.as_view(), name='wish_update'),
    path('wishlist/<int:pk>/delete', WishDeleteView.as_view(), name='wish_delete'),
    path('subscriptions/<int:pk>/delete', SubscriptionDeleteView.as_view(), name='subscription_delete'),
    path('bills/<int:pk>/delete', BillDeleteView.as_view(), name='bill_delete'),
    # path('bills/<int:pk>/delete', bill_delete_view, name='bill_delete'),
    path('friendlyloans/<int:pk>/delete', LoanDeleteView.as_view(), name='loan_delete'),
]