from django.shortcuts import render

def Error404View(request, exception):
    return render(request, "error_404_not_found.html")
