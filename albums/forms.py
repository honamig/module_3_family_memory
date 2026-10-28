from django import forms
from .models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["album", "title", "image"]

    def clean_image(self):
        image = self.cleaned_data["image"]

        # Limit image size to 5 MB
        if image.size > 5 * 1024 * 1024:
            raise forms.ValidationError(
                "The image must be smaller than 5 MB."
            )

        return image