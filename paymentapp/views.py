from django.shortcuts import render, redirect
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
from django.http import JsonResponse
from django.views import View

stripe.api_key = settings.SECRET_STRIPE_KEY


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# class CreateCheckoutSessionView(View): # для jsina шаблон с ЖС
#     def post(self, request, *args, **kwargs):
#         product_id = self.kwargs["pk"]
#         product = Item.objects.get(id=product_id)
#         YOUR_DOMAIN = "http://127.0.0.1:8000"
#         checkout_session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             line_items=[
#                 {
#                     'price_data': {
#                         'currency': 'usd',
#                         'unit_amount': product.price,
#                         'product_data': {
#                             'name': product.name
#                         },
#                     },
#                     'quantity': 1,
#                 },
#             ],
#             metadata={
#                 "product_id": product.id
#             },
#             mode='payment',
#             success_url=YOUR_DOMAIN + '/success/',
#             cancel_url=YOUR_DOMAIN + '/cancel/',
#         )
#         return JsonResponse({
#             'id': checkout_session.id
#         })

@api_view(['GET','POST'])
def build_checkout_session(request,pk,*args, **kwargs):
    price = Item.objects.get(id=pk)
    YOUR_DOMAIN = "http://127.0.0.1:8000"  # change in production
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': price.price,
                    'product_data': {
                        'name': price.name
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
def get_session_id(request,pk):
    session = build_checkout_session(pk=pk)
    return Response({
        'id': session.id
    })


class ProductLandingPageView(TemplateView):
    template_name = "landing.html"

    def get_context_data(self, **kwargs):
        product = Item.objects.get(pk=self.kwargs['pk'])
        context = super(ProductLandingPageView, self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "STRIPE_PUBLIC_KEY": settings.PUBLIC_STRIPE_KEY
        })
        print(context)
        return context


class ItemDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'item_detail.html'

    def get(self, request, pk):
        product = get_object_or_404(Item, pk=pk)
        serializer = ItemSerializer(product)
        return Response({'serializer': serializer, 'product': product,"STRIPE_PUBLIC_KEY": settings.PUBLIC_STRIPE_KEY})

class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"
