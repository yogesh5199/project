from django.shortcuts import render

# Create your views here.
def about_page(request):
    context= {
        "title":"About page",
        "content":"welcome to the About page"
    }
    return render(request,'base/about_page.html',context)