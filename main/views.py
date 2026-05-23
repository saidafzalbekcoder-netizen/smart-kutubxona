from django.shortcuts import render, get_object_or_404
from .models import Muallif, Kitob

# ================================================================
#   1-TOPSHIRIQ.  Bosh sahifa
# ================================================================
def bosh_sahifa(request):
    return render(request, 'main/bosh_sahifa.html')


# ================================================================
#   2-TOPSHIRIQ.  Context bilan ma'lumot uzatish (string)
# ================================================================
def salom(request):
    kontekst = {'ism': 'Ali'}
    return render(request, 'main/salom.html', kontekst)


# ================================================================
#   3-TOPSHIRIQ.  Obyektni context'da uzatish
# ================================================================
def muallif_view(request):
    muallif = Muallif.objects.first()
    return render(request, 'main/muallif.html', {'muallif': muallif})


# ================================================================
#   4-TOPSHIRIQ.  Ro'yxat ({% for %} bilan)
# ================================================================
def kitoblar_royxati(request):
    kitoblar = Kitob.objects.all()
    return render(request, 'main/kitoblar.html', {'kitoblar': kitoblar})


# ================================================================
#   5-TOPSHIRIQ.  Filtrlar bilan ishlash
# ================================================================
def filtrlar(request):
    kontekst = {
        'matn': 'salom dunyo',
        'son': 5,
        'ism': ''
    }
    return render(request, 'main/filtrlar.html', kontekst)


# ================================================================
#   6-TOPSHIRIQ.  {% if %} va {% for %} birga
# ================================================================
def shartlar(request):
    kitoblar = Kitob.objects.all()
    return render(request, 'main/shartlar.html', {'kitoblar': kitoblar})


# ================================================================
#   7-TOPSHIRIQ.  URL parametri va {% url %} tegi
# ================================================================
def muallif_detail(request, muallif_id):
    muallif = get_object_or_404(Muallif, pk=muallif_id)
    return render(request, 'main/muallif_detail.html', {'muallif': muallif})


# ================================================================
#   8-TOPSHIRIQ.  {% url %} tegi bilan navigatsiya
# ================================================================
def kitob_detail(request, kitob_id):
    kitob = get_object_or_404(Kitob, pk=kitob_id)
    return render(request, 'main/kitob_detail.html', {'kitob': kitob})


# ================================================================
#   9-TOPSHIRIQ.  {% static %} tegi (statik fayllar)
# ================================================================
def static_test(request):
    return render(request, 'main/static_test.html', {'sarlavha': 'Statik Fayllar Testi'})


# ================================================================
#  10-TOPSHIRIQ.  {% extends %} va {% block %} (DRY printsipi)
# ================================================================
def home_page(request):
    return render(request, 'main/home.html')


def haqida_page(request):
    return render(request, 'main/haqida.html')