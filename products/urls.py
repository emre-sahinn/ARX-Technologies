from django.urls import path
from . import views


urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:product_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:product_id>/results/', views.results, name='results'),
    # ex: /polls/5/order/
    path('<int:product_id>/order/', views.order, name='order'),

    path('<int:product_id>/payment/', views.payment, name='payment'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),
]
