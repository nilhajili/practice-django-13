from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login
from .forms import ReviewForm
from django.contrib.auth.forms import UserCreationForm

from .models import Product, Review

def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("product_list")

    else:
        form = UserCreationForm()

    return render(
        request,
        "registration/register.html",
        {"form": form}
    )
def product_list(request):
    products = Product.objects.all()

    return render(
        request,
        "products/product_list.html",
        {"products": products}
    )


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    reviews = product.reviews.all().order_by("-created_at")
    review_form = ReviewForm()

    return render(
        request,
        "products/product_detail.html",
        {
            "product": product,
            "reviews": reviews,
            "review_form": review_form
        }
    )


@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()

            return redirect("product_detail", product.id)

    return redirect("product_detail", product.id)


@login_required
def edit_review(request, pk):

    review = get_object_or_404(Review, pk=pk)

    if review.user != request.user:
        return redirect("product_detail", pk=review.product.pk)

    if request.method == "POST":

        review.text = request.POST.get("text")
        review.rating = request.POST.get("rating")

        review.save()

        return redirect(
            "product_detail",
            pk=review.product.pk
        )

    return render(
        request,
        "products/review_edit.html",
        {"review": review}
    )


@login_required
def delete_review(request, pk):

    review = get_object_or_404(Review, pk=pk)

    if review.user != request.user:
        return redirect("product_detail", pk=review.product.pk)

    if request.method == "POST":

        product_id = review.product.pk

        review.delete()

        return redirect(
            "product_detail",
            pk=product_id
        )

    return redirect(
        "product_detail",
        pk=review.product.pk
    )