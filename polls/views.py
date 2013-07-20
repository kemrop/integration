# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from polls.models import Poll
def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[0:3]
    template = loader.get_template('index.html')
    context = RequestContext(request, {'latest_poll_list': latest_poll_list})
    return HttpResponse(template.render(context))

def detail(request, poll_id):
    """

    :param request:
    :param poll_id:
    :return:
    """
    return HttpResponse('You\'re looking at the results of poll %s' % poll_id)