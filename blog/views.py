from django.shortcuts import render
from .models import Post

# posts=[
#     {
#         'author':'Nandita',
#         'title':'Blog_post1',
#         'content':'First post content',
#         'date_posted':'September 3, 2020',
#     },
#     {
#         'author':'Richard Hendricks',
#         'title':'Blog_postA',
#         'content':'A post content',
#         'date_posted':'September 23, 2020',
#     },
# ];
#from django.http import HttpResponse

# def home(request):
#     return HttpResponse('<h1>Blog home</h1>')
def home(request):
    # context={
    #     'posts':posts,
    # }
    context={
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})