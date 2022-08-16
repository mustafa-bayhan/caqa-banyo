from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.views.generic.edit import UpdateView
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.db.models import F
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    context=dict()
    
    return render(request,'index.html',context)
