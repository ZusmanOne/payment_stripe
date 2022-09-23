import stripe
from django.conf import settings
from .models import Item
from django.views.generic import TemplateView
from .serializers import ItemSerializer
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics


stripe.api_key = settings.SECRET_STRIPE_KEY


class ProductList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


@api_view(['GET', 'POST'])
def build_checkout_session(request, pk, *args, **kwargs):
    product = Item.objects.get(id=pk)
    YOUR_DOMAIN = "http://127.0.0.1:8000"  # change in production
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': product.price,
                    'product_data': {
                        'name': product.name
                    },
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=YOUR_DOMAIN + '/success/',
        cancel_url=YOUR_DOMAIN + '/cancel/',
    )
    return Response({
        'id': checkout_session.id
    })


@api_view(['GET'])
def get_session_id(request, pk):
    session = build_checkout_session(pk=pk)
    return Response({
        'id': session.id
    })


class ItemDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'item_detail.html'

    def get(self, request, pk):
        product = get_object_or_404(Item, pk=pk)
        serializer = ItemSerializer(product)
        return Response({'serializer': serializer, 'product': product, "STRIPE_PUBLIC_KEY": settings.PUBLIC_STRIPE_KEY})


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"
