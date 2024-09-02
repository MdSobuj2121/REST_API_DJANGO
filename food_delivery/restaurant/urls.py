from django.urls import path
from .views import RegisterUserView, LoginUserView, RestaurantListView, CategoryListView, MenuItemListView, ModifierListView, OrderCreateView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('restaurants/', RestaurantListView.as_view(), name='restaurants'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('menu-items/', MenuItemListView.as_view(), name='menu-items'),
    path('modifiers/', ModifierListView.as_view(), name='modifiers'),
    path('orders/', OrderCreateView.as_view(), name='orders'),
]
