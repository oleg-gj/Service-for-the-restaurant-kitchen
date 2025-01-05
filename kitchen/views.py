from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.models import Cook, Dish, DishType


def index(request):
    """View function for the home page of the site."""
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dishes_type = DishType.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dishes_type": num_dishes_type,
        "num_visits": num_visits + 1,
    }

    return render(request, "kitchen/index.html", context=context)


class CookListView(generic.ListView):
    model = Cook


class CookDetailView(generic.DetailView):
    model = Cook
    queryset = Cook.objects.prefetch_related("dishes")


class CookCreateView(generic.CreateView):
    model = Cook
    fields = "__all__"
    success_url = reverse_lazy("kitchen:cook-list")
    template_name = "kitchen/cook_form.html"


class CookUpdateView(generic.UpdateView):
    model = Cook
    fields = "__all__"
    success_url = reverse_lazy("kitchen:cook-list")
    template_name = "kitchen/cook_form.html"


class CookDeleteView(generic.DeleteView):
    model = Cook
    template_name = "kitchen/cook_delete.html"
    success_url = reverse_lazy("kitchen:cook-list")

class DishListView(generic.ListView):
    model = Dish

class DishDetailView(generic.DetailView):
    model = Dish
    queryset = (
        Dish.objects.prefetch_related("cooks").select_related("dish_type")
    )
