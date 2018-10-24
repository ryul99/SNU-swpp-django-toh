from django.http import HttpResponse

def index(request):
    if 'visit_count' not in request.session:
        request.session['visit_count'] = 1
    else:
        request.session['visit_count'] += 1
    return HttpResponse('Hello, world! You visited {} times.\n'
                        .format(request.session['visit_count']))
def id(request, id=''):
    return HttpResponse(str(id))
def name(request, name=''):
    return HttpResponse(name)
# Create your views here.
