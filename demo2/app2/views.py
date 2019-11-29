from django.shortcuts import render

# Create your views here.
def Index(request):
    d1={101:{"name":"ravi","sal":1250000},
        120:{"name":"annu","sal":1215365}}
    return render(request,"index.html",{"d":d1})