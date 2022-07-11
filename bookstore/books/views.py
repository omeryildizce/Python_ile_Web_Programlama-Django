from django.shortcuts import render
from django.http import Http404, HttpResponse 
from django.template import loader
from .models import Author
# Create your views here.

def index(request):
    return HttpResponse("Anasayfa")

def authors(request):
    # template = loader.get_template('authors.html')
    context = {
        "authors_list" : Author.objects.all()
    }
    # return HttpResponse(template.render(context, request))
    # alternatif
    return render(request, "authors.html", context)
def books(request):
    return HttpResponse("Kitaplar")

def autorDetails(request, authorId):
    try:
        context = {
            "author_detail" : Author.objects.get(pk=authorId)
        } 
    except Author.DoesNotExist:
        raise Http404("Yazar bulunamadı")
    return render(request, "authorDetail.html", context)

