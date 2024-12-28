
from django.urls import path
from Home import views

urlpatterns = [
    path('get-Note/', views.Note_View, name="get-Note"),
    path('Note/', views.Note_View_Class.as_view(), name="Note"),
    path('get-Transaction/', views.Transaction_View, name="get-Transaction"),
    path('Transaction/', views.Transaction_View_Class.as_view(), name="Transaction"),
]