from django.shortcuts import render
def simple(request):
    return  render( request, 'index.html',{})