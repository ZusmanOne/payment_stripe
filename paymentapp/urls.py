from django.urls import path
from .views import (
                    ProductLandingPageView,
                    SuccessView,
                    CancelView,
                    get_session_id,
                    ItemDetail,
                    build_checkout_session,
                    # ProductViewSet,
                    # CreateCheckoutSessionView
)
#from rest_framework.routers import SimpleRouter
#
# router = SimpleRouter()
# router.register('products', ProductViewSet, basename='products')
# urlpatterns = router.urls


from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    # path('buy/<pk>/', get_session_id, name='create-session'),
    # path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('<int:pk>/', csrf_exempt(ProductLandingPageView.as_view()), name='landing'),
    path('item/<int:pk>/', ItemDetail.as_view(), name='item-detail'),
    path('buy/<pk>/', build_checkout_session, name='create-checkout-session'),

]
