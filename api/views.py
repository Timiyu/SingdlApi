from django.http import HttpResponse
import json

# Create your views here.
def list(request):
    data ={}
    return HttpResponse(json.dumps(data), content_type="application/json")