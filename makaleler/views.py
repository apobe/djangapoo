from django.shortcuts import render,redirect,reverse,get_object_or_404


from .models import makale,commentt
from django.contrib import messages
from .form import article1
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def dashboard(request):
    articles=makale.objects.filter(author=request.user)
    return render(request,"dashboard.html",{"articles":articles})
@login_required(login_url="user:login")
def addarticle(request):
    form=article1(request.POST or None)
    if form.is_valid():
        makale1=form.save(commit=False)#şuanlık kayıt etmiyoruz çünkü site bize bir kullanıcı yani yazar da isityor sonra onu da ekliyoruz 
        makale1.author=request.user
        makale1.save()
        messages.success(request,"Makaleniz Kaydedildi !")
        return redirect("index")
    return render(request,"addarticle.html",{"form":form})
@login_required(login_url="user:login")#decarator gibi istediğin sayfaya gitmemek için
def update(request,id):
    article=makale.objects.get(id=id)#article = deki articleı kafana göre değiştiremezsin
    form=article1(request.POST or None,instance=article)#güncellemek için
    if form.is_valid():
        article=form.save(commit=False)
        form.author=request.user
        article.save()
        messages.success(request,"Başarıyla Güncellendi !")
        return redirect("index")
    return render(request,"update.html",{"form":form})
@login_required(login_url="user:login")
def delete(request,id):
    article=makale.objects.get(id =id)
    article.delete()
    messages.success(request,"Makaleniz Başarıyla Silindi")
    return redirect("makaleler:dashboard")
def detay(request,id):
    articles=get_object_or_404(makale,id=id)
    comments=articles.comments.all()
    return render(request,"detay.html",{"article":articles,"comments":comments})
def makaleler(request):
    keyword=request.GET.get("keyword")
    if keyword:
        articles=makale.objects.filter(title__contains=keyword)
        return render(request,"makaleler.html",{"articles":articles})
    articles=makale.objects.all()
    return render(request,"makaleler.html",{"articles":articles})
def commnet(request,id):
    article=makale.objects.get(id=id)
    if request.method =="POST":
        commentauthor=request.POST.get("commentauthor")
        commentcontent=request.POST.get("commentcontent")#web sayfasından isim aldık
        newcommet=commentt(commentcontent=commentcontent,commentauthor=commentauthor)
        newcommet.article=article
        newcommet.save()
    return redirect(reverse("makaleler:detay",kwargs={"id":id}))#id için kwars yazdık