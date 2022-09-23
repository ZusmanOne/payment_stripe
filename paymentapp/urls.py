from django.urls import path
from .views import (ProductList,
                    SuccessView,
                    CancelView,
                    ItemDetail,
                    build_checkout_session,)


urlpatterns = [
    path('', ProductList.as_view(), name='product-list'),
    path('item/<int:pk>/', ItemDetail.as_view(), name='item-detail'),
    path('buy/<pk>/', build_checkout_session, name='create-checkout-session'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),

]
