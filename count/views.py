from django.shortcuts import render, get_object_or_404,redirect
from .models import Text
from django.utils import timezone
# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def result(request,text_id):
    t=get_object_or_404(Text, pk=text_id)
    text_detail = str(get_object_or_404(Text, pk=text_id))
    #text=request.GET['body']
    words=text_detail.split()
    word_dictionary={}

    for word in words:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1
    return render(request,'result.html',{'text':t,'full':text_detail,'total':len(words),'dictionary':word_dictionary.items()})

def history(request):
    texts=Text.objects 
    return render(request,'history.html',{'texts':texts})

def create(request):
    text=Text()
    text.body=request.GET['body']
    text.pub_date = timezone.datetime.now()
    text.save()
    return redirect('/result/'+str(text.id))