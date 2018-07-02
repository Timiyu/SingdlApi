from django.http import HttpResponse
import json

# Create your views here.
def list(request):
    data = {'name': 'dddddd'}
    return HttpResponse(json.dumps(data), content_type="application/json")

def detail(request):
    videourl = ''
    return HttpResponse(json.dumps(videourl), content_type="application/json")