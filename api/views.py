from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def sightings(request):

    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass


@csrf_exempt
def sighting(request, sighting_id):

    if request.method == 'GET':
        pass


@csrf_exempt
def sighting_photos(request, sighting_id):

    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass


@csrf_exempt
def sighting_expert_comments(request, sighting_id):

    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass


@csrf_exempt
def sighting_expert_comment(request, sighting_id, expert_comment_id):

    if request.method == 'GET':
        pass


@csrf_exempt
def sighting_questions(request, sighting_id):

    if request.method == 'GET':
        pass


@csrf_exempt
def sighting_question(request, sighting_id):

    if request.method == 'GET':
        pass
    elif request.method == 'PATCH':
        pass


@csrf_exempt
def locations(request, sighting_id):

    if request.method == 'GET':
        pass
    elif request.method == 'HEAD':
        pass
