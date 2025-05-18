from django.urls import path
from .views import khabarListCreate , khabarDetail

urlpatterns = [
    path('tazakhabars/', khabarListCreate.as_view(), name='taza-list'),
    path('tazakhabars/<str:khabar_id>/', khabarDetail.as_view(),name='khabar-detail'),
]
