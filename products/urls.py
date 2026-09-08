from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),

    path(
        "product/<int:pk>/",
        views.product_detail,
        name="product_detail"
    ),

    path(
        "product/<int:product_id>/review/",
        views.add_review,
        name="add_review"
    ),

    path(
        "review/<int:pk>/edit/",
        views.edit_review,
        name="review_edit"
    ),

    path(
        "review/<int:pk>/delete/",
        views.delete_review,
        name="review_delete"
    ),

    path(
        "register/",
        views.register,
        name="register"
    ),
]