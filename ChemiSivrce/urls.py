from django.urls import path
import views as views

urlpatterns = [
    path('wishlist', views.wishlist_view, name='wishlist'),
    path('subscriptions', views.subscriptions_view, name='subscriptions'),
    path('friendlyloans', views.friendly_loans_view, name='friendly_loans'),
]