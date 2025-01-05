from django.urls import path

from kitchen import views
from kitchen.views import (
    CookListView,
    CookDetailView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView, DishListView, DishDetailView,
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
    path(
        "cooks/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete"
    ),
    path("dishes/",DishListView.as_view(), name="dish-list"),
    path(
        "dishes/<int:pk>/",
        DishDetailView.as_view(),
        name="dish-detail"
    ),

]

app_name = "kitchen"
