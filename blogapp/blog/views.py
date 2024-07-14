from django.shortcuts import render
from django.http.response import HttpResponse

def index(request):
	return render(request, 'blog/index.html')

def blogs(request):
	return render(request, 'blog/blogs.html')

def blog_details(request, id):
	return render(request, 'blog/blogs_details.html', {
		"id" : id
	})

