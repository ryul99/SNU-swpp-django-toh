from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, world!')
def id(request, id=''):
    return HttpResponse(str(id))
def name(request, name=''):
    return HttpResponse(name)
# Create your views here.