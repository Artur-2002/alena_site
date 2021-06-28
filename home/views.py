from django.shortcuts import render
from .models import Product, Makeup_img, Wedding_img, Hair_img

# Create your views here.

def home(request):
	return render(request, 'home/home.html')


def portfolio(request):
	return render(request, 'home/portfolio.html')


def contacts(request):
	return render(request, 'home/contacts.html')


def prices(request):
	id1 = Product.objects.get(id=1)
	id2 = Product.objects.get(id=2)
	id3 = Product.objects.get(id=3)
	id4 = Product.objects.get(id=4)
	id5 = Product.objects.get(id=5)
	id6 = Product.objects.get(id=6)
	id7 = Product.objects.get(id=7)
	id8 = Product.objects.get(id=8)
	id9 = Product.objects.get(id=9)
	id10 = Product.objects.get(id=10)
	id11 = Product.objects.get(id=11)
	id12 = Product.objects.get(id=12)
	id13 = Product.objects.get(id=13)
	id14 = Product.objects.get(id=14)
	id15 = Product.objects.get(id=15)
	id16 = Product.objects.get(id=16)
	id17 = Product.objects.get(id=17)
	context = {'id1': id1, 'id2': id2, 'id3': id3, 'id4': id4, 'id5': id5, 'id6': id6, 'id7': id7, 'id8': id8, 'id9': id9, 'id10': id10, 'id11': id11, 'id12': id12, 'id13': id13, 'id14': id14, 'id15': id15, 'id16': id16, 'id17': id17}
	return render(request, 'home/prices.html', context)


def video(request):
	return render(request, 'home/video.html')


def makeup(request):
	makeups = Makeup_img.objects.all()
	return render(request, 'home/makeup.html', {'makeups': makeups})


def wedding(request):
	weddings = Wedding_img.objects.all()
	return render(request, 'home/wedding.html', {'weddings': weddings})


def hair(request):
	hairs = Hair_img.objects.all()
	return render(request, 'home/hair.html', {'hairs': hairs})


def view_404(request, exception):
	return render(request, 'home/404.html')








