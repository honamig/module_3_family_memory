from django.shortcuts import render

def home(request):
    albums = [
        {"title": "Family Trip", "year": 2024},
        {"title": "Piano Recital", "year": 2018},
        {"title": "Christmas", "year": 2023}
    ]

    error_message = ""
    success_message = ""
    form_title = ""
    form_year = ""

    # Check if the user submitted the form
    if request.method == "POST":
        form_title = request.POST.get("album_title", "").strip()
        form_year = request.POST.get("album_year", "").strip()

        # Title validation
        if not form_title:
            error_message = "Please enter an album title."

        elif len(form_title) > 50:
            error_message = "The title must be 50 characters or fewer."

        # Year validation
        elif not form_year.isdigit():
            error_message = "Please enter a valid year."

        elif not 1900 <= int(form_year) <= 2026:
            error_message = "Please enter a year between 1900 and 2026."

        # Add the album if all inputs are valid
        else:
            new_album = {
                "title": form_title,
                "year": int(form_year)
            }

            albums.append(new_album)
            success_message = "Album added successfully!"

            form_title = ""
            form_year = ""

    context = {
        "page_title": "Family Memories",
        "welcome_message": "Welcome to family photo album",
        "albums": albums,
        "error_message": error_message,
        "success_message": success_message,
        "form_title": form_title,
        "form_year": form_year
    }

    print("Request method:", request.method)
    print("Error message:", error_message)

    return render(request, "albums/home.html", context)