from django.urls import path
from django.views.generic.edit import CreateView 
from .views import RecipeDeleteView, RecipeDetailView, RecipeListView, RecipeCreateView, RecipeUpdateView

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe_list'),
    path("<int:pk>/", RecipeDetailView.as_view(), name='recipe_detail'),
#     path("create/", RecipeCreateView.as_view(), name="_create"),
#     path('<int:pk>/update/', RecipeUpdateView.as_view(), name='_update'),
#     path('<int:pk>/delete/', RecipeDeleteView.as_view(), name='_delete'),
]
