from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    return render(request,'jinja_print.html',context={'name':'Ashu','age':2})

def conditional(request):
    d={'a':5210,'b':300,'c':400}
    return render(request,'conditional.html',context=d)
