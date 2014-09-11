from django.shortcuts import render
from blog.models import blog as blog_model
from django.shortcuts import render_to_response
# Create your views here.
def blog(request):
    blog_post = blog_model.objects.all()
    return render_to_response('blog/blog.html',{'posts':blog_post})