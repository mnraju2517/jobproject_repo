from django.shortcuts import render
from testapp.models import *

# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

def hydjobs1(request):
    jobs_list=hydjobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',context=my_dict)

def bangjobs1(request):
    return render(request,'testapp/bangjobs.html')

def chennaijobs1(request):
    return render(request,'testapp/chennaijobs.html')

def punejobs1(request):
    return render(request,'testapp/punejobs.html')
