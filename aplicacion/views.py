from django.shortcuts import render

def literatura(request):
    return render(request, "aplicacion/literatura.html")
