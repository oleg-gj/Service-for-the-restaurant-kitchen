from django.urls import path

from kitchen import views
from kitchen.views import CookListView, CookDetailView

urlpatterns = [
    path("", views.index, name="index"),
    path("cooks/",CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/",CookDetailView.as_view(), name="cook-detail"),
]

app_name = "kitchen"
