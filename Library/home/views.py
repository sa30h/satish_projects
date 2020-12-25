from django.shortcuts import render,HttpResponse
from home.models import Book

# Create your views here.
def index(request):
    if (request=="POST"):
        bookname=request.POST.get("bookname")
        author=request.POST.get("author")
        booktype=request.POST.get("author")
        # fiction=request.POST.get("fiction")
        # programming=request.POST.get("programming")
        # cooking=request.POST.get("cooking")
        
        
        # if fiction is checked:
        #     chek="fiction"
        #     return chek
        # elif programming is checked:
        #     chek="programming"
        #     return chek
        # elif cooking is checked:
        #     chek="cooking"
        #     return chek
        # booktype=chek
        book=Book(bookname=bookname,author=author,booktype=booktype)
        book.save()
    return render(request,'index.html')

def services(request):

        
    return render(request,'services.html')
