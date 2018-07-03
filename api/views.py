from . import models
from django.http import HttpResponse
import json

# Create your views here.
def list(request):
    data = models.articles.objects.all().toJON()
    return HttpResponse(data, content_type="application/json")

def detail(request):
    videourl = ''
    return HttpResponse(json.dumps(videourl), content_type="application/json")