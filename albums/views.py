from django.shortcuts import render, redirect
from .models import Album
from .forms import PhotoForm


def home(request):
    error_message = ""
    form_title = ""
    form_year = ""

    # Create an empty photo upload form
    photo_form = PhotoForm()

    # Handle form submissions
    if request.method == "POST":

        # Create a new album
        if "create_album" in request.POST:
            form_title = request.POST.get("album_title", "").strip()
            form_year = request.POST.get("album_year", "").strip()

            # Validate album title
            if not form_title:
                error_message = "Please enter an album title."

            elif len(form_title) > 50:
                error_message = "The title must be 50 characters or fewer."

            # Validate year
            elif not form_year.isdigit():
                error_message = "Please enter a valid year."

            elif not 1900 <= int(form_year) <= 2026:
                error_message = "Please enter a year between 1900 and 2026."

            # Save the album to SQLite
            else:
                Album.objects.create(
                    title=form_title,
                    year=int(form_year)
                )
                return redirect("home")

        # Upload a photo
        elif "upload_photo" in request.POST:
            photo_form = PhotoForm(request.POST, request.FILES)

            if photo_form.is_valid():
                photo_form.save()
                return redirect("home")

    # Get albums and their photos from SQLite
    albums = Album.objects.prefetch_related("photos").all()

    context = {
        "page_title": "Family Memories",
        "welcome_message": "Welcome to family photo album",
        "albums": albums,
        "error_message": error_message,
        "form_title": form_title,
        "form_year": form_year,
        "photo_form": photo_form
    }

    return render(request, "albums/home.html", context)