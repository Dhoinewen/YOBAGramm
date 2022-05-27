from django.urls import path, include
from rest_framework import routers

from .views import YobaAPIList


router = routers.SimpleRouter()
router.register(r'post', YobaAPIList)

urlpatterns = [
    path('', include(router.urls)),
    # path('list', PostAPIList.as_view()),
    # path('list/<int:pk>/', PostAPIUpdate.as_view()),
    # path('list/post/<int:pk>/', PostAPIDetailView.as_view()),
    # path('comments', CommentsAPIView.as_view()),
    # path('comments/<int:pk>/', CommentsAPIView.as_view()),
]