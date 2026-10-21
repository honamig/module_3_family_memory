from django.shortcuts import render

# Create your views here.
def home(request):
    albums = [
        {
            "title": "Family Trip",
                "year": 2024
        },
        {
            "title": "Piano Recital",
            "year": 2018
        },
        {
            "title": "Christmas",
            "year": 2023
        }
    ]
    context = {
        "page_title": "Family Memories",
        "welcome_message": "Welcome to family photo album",
        "albums": albums
    }

    return render(request, "albums/home.html", context)