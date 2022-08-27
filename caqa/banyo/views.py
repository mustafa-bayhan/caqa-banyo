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
import random

# Create your views here.
def home(request):
    context=dict()
    query2=request.GET.get('search')
    if query2:
        return HttpResponseRedirect('/products?search={}'.format(query2))
    context['allproducts']=Ürün.objects.all().distinct()[:4]
    context['allref']=Referanslar.objects.all()
    context['most_sell']=Ürün.objects.all().order_by('-görüntüleme','-id').distinct()[:4]
    return render(request,'home.html',context)

def about(request):
    context2=dict()
    query2=request.GET.get('search')
    if query2:
        return HttpResponseRedirect('/products?search={}'.format(query2))
    
    about=Hakkimizda.objects.all()
    if len(about)!=0:
        context2['about']=about[0]
    
    
    return render(request,'about.html',context2)

def products(request):
    context3=dict()
    allproducts=Ürün.objects.all()
    if request.GET.get('search'):
        allproducts=allproducts.filter(Q(kategori__isim__contains=request.GET.get('search')) | Q(alt_kategori__isim__contains=request.GET.get('search')) | Q(isim__contains=request.GET.get('search')) | Q(özellikler__contains=request.GET.get('search')) | Q(montaj_sekli__isim__contains=request.GET.get('search')))
         
    if request.GET.get('q'):
        
        allproducts=allproducts.filter(Q(kategori__isim__iexact=request.GET.get('q')))
        
    if request.GET.get('q2'):
        
        allproducts=allproducts.filter(Q(alt_kategori__isim__iexact=request.GET.get('q2')))
        
    if request.GET.get('q3'):
        
        allproducts=allproducts.filter(Q(renk__renk_ismi__iexact=request.GET.get('q3')))
        
        
    if request.GET.get('q4'):
        
        allproducts=allproducts.filter(Q(montaj_sekli__isim__iexact=request.GET.get('q4')))
        
    colors = []
    cat = []
    şekil = []
    altcat = []
    for product in allproducts:
        cat.append(product.kategori.isim)
        şekil.append(product.montaj_sekli.isim)
        altcat.append(product.alt_kategori.isim)
    
    
    for color in Renkler.objects.all():
        if len(allproducts.filter(Q(renk__renk_ismi__iexact=color.renk_ismi)))!=0:
            colors.append(color.renk_ismi)
    
    paginator = Paginator(allproducts, 12) # bir sayfada kaç tane görünmesi gerek

    page_num = request.GET.get('page')
    page=paginator.get_page(page_num)
    
    context3['count']=paginator.count
    context3['page'] = page  
    page_number=page.number

    if page_number !=None:
        fark=int(paginator.num_pages) - int(page_number)
       
        if fark >= 2:
            context3['last'] = ('last')
            if fark > 2:
                context3['last_three'] = ('last_three')
                
            
        if int(page_number) >= 3:
            context3['first'] = ('first')
            
            if int(page_number) > 3:
                context3['three_dot'] = ('three_dot')
            
    else:

        
        if paginator.num_pages-1 >= 2:
            context3['last_true'] = ('last')
            if paginator.num_pages-1 >2:
                
                context3['last_three'] = ('last_three')
  
            
    context3['colors']= set(colors)   
    context3['cat']= set(cat)
    context3['sekil']= set(şekil)
    context3['altcat']= set(altcat)
    context3['allproducts']= allproducts
        
    return render(request,'product.html',context3)

def catalog(request):
    context4=dict()
    query2=request.GET.get('search')
    if query2:
        return HttpResponseRedirect('/products?search={}'.format(query2))
    katalogs =Katalog.objects.all()
    if len(katalogs)!=0:
        context4['catalog']= katalogs[0]
    return render(request,'catalog.html',context4)

def references(request):
    context5=dict()
    query2=request.GET.get('search')
    if query2:
        return HttpResponseRedirect('/products?search={}'.format(query2))
    context5['allref']=Referanslar.objects.all()
    return render(request,'reference.html',context5)



def contact(request):
    context6=dict()
    query2=request.GET.get('search')
    if query2:
        return HttpResponseRedirect('/products?search={}'.format(query2))
    if request.method=="POST":
        
        username=request.POST.get('name')
        mail=request.POST.get('email')
        number=request.POST.get('tel')
        comment=request.POST.get('message')
        result = int(request.POST.get('a')) + int(request.POST.get('b'))
        if result == int(request.POST.get('result')):
        
            make_comment = Mesajlar.objects.create(musteri_ismi=username,mail=mail, telefon=number, mesaj=comment)
            make_comment.save()
            
        else:
            a = random.randint(1,100)
            b = random.randint(1,100)
            context6['a']=a
            context6['b']=b
            context6['username']=username
            context6['email']=mail
            context6['tel']=number
            context6['message']=comment
            context6['error'] = 'İşlem sonucu yanlış. Lütfen sonucu doğru giriniz!'
            return render(request,'contact.html',context6)
            
            
    a = random.randint(1,100)
    b = random.randint(1,100)
    context6['a']=a
    context6['b']=b
    return render(request,'contact.html',context6)

def product_detail(request, slug):
    context7=dict()
    query2=request.GET.get('search')
    if query2:
        return HttpResponseRedirect('/products?search={}'.format(query2))
    the_product=get_object_or_404(Ürün, slug=slug)
    context7['the_product']=the_product
    görüntüleme = the_product.görüntüleme
    görüntüleme += 1
    degıs = Ürün.objects.filter(slug=slug).update(görüntüleme=görüntüleme)
    similar = Ürün.objects.filter(Q(alt_kategori__isim = the_product.alt_kategori.isim),~Q(slug = the_product.slug))
    if len(similar)!=0:
        context7['similar_products']=random.sample(list(similar), min(4, len(similar)))
    else:
        products=Ürün.objects.filter(~Q(slug = the_product.slug))
        context7['similar_products']= random.sample(list(products), min(4, len(products)))
   
    return render(request,'product-detail.html',context7)




def handle_not_found(request, exception):
    context7={}
    query2=request.GET.get('search')
    if query2:
        return HttpResponseRedirect('/products?search={}'.format(query2))
    
    return render(request, '404.html',context7)