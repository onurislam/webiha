from django.shortcuts import render, get_object_or_404, redirect
from .forms import IHAForm
from .models import IHA
from django.db.models import Q


def index(request):
    # Giriş kontrol!
    if not request.user.is_authenticated:
        return redirect('/accounts/')
    else:
        return render(request, "panel/index.html")


def List(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/')
    else:
        ihalists = IHA.objects.all()
        query = request.GET.get('q')
        if query:
            # Liste üzerinde arama yapmasını sağlar
            ihalists = ihalists.filter(
                Q(title__icontains=query) |
                Q(model__icontains=query) |
                Q(category__icontains=query) |
                Q(weight__icontains=query)
            )

        context = {
            "data": ihalists
        }
        return render(request, "panel/IhaList.html", context)


def Add(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/')
    else:
        if request.method == "POST":
            form = IHAForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                form.save()
        else:
            form = IHAForm()

        context = {'form': form}
        return render(request, "panel/IhaAdd.html", context)


def Update(request, id):
    if not request.user.is_authenticated:
        return redirect('/accounts/')
    else:
        ihaData = get_object_or_404(IHA, id=id)
        if request.method == "POST":
            form = IHAForm(request.POST or None, request.FILES or None, instance=ihaData)
            if form.is_valid():
                form.save()
        return render(request, "panel/IhaUpdate.html", {"iha": ihaData})


def Delete(request, id):

    if not request.user.is_authenticated:
        return redirect('/accounts/')
    else:
        iha = get_object_or_404(IHA, id=id)
        iha.delete()

        ihalists = IHA.objects.all()
        context = {
            "data": ihalists
        }
        return render(request, "panel/IhaList.html", context)
