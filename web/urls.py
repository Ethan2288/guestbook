from django.urls import path
from .views import  *

urlpatters =[
    path('', MessageList.as_view(), name='msg_list'),
    path('<int:pk>/', MessageDetail.as_view(), name='msg_view'),
    path('create/', MessageCreate.as_view(), name='msg_create'),
]