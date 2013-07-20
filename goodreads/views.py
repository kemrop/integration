# Create your views here.
__author__ = 'markrop'
from django.http import HttpResponse
from django.template import RequestContext, loader
from goodreads.models import GoodReadsApi
def index(request):
    return HttpResponse(GoodReadsApi.html)
    #return HttpResponse('You just called the goodreads view')