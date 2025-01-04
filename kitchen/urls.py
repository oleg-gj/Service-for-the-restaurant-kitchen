from django.urls import path

from kitchen import views
from kitchen.views import (
    CookListView,
    CookDetailView,
    CookCreateView,
    CookUpdateView
)


urlpatterns = [
    path("", views.index, name="index"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path(
        "cooks/<int:pk>/update/",
        CookUpdateView.as_view(),
        name="cook-update"
    ),
]

app_name = "kitchen"
