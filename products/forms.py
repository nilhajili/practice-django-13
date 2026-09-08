
from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["text", "rating"]

        widgets = {
            "text": forms.Textarea(attrs={
                "rows": 5,
                "placeholder": "Write your review...",
                "class": "w-full px-4 py-3 border border-gray-300 "
                         "rounded-xl focus:outline-none "
                         "focus:ring-2 focus:ring-blue-500 "
                         "resize-none",
            }),

            "rating": forms.NumberInput(attrs={
                "min": 1,
                "max": 5,
                "placeholder": "1 - 5",
                "class": "w-full px-4 py-3 border border-gray-300 "
                         "rounded-xl focus:outline-none "
                         "focus:ring-2 focus:ring-blue-500",
            }),
        }
