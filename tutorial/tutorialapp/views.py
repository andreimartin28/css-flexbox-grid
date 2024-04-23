from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,
                  'tutorialapp/index.html')


def flex(request):
    return render(request,
                  'tutorialapp/flex.html')


def grid(request):
    return render(request,
                  'tutorialapp/grid.html')


def gridd(request):
    return render(request,
                  'tutorialapp/gridd.html')


def grid_3(request):
    return render(request,
                  'tutorialapp/grid_3.html')


def grid_4(request):
    return render(request,
                  'tutorialapp/grid_4.html')
