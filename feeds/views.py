from django.shortcuts import render
from .models import Feed
from django.shortcuts import redirect

# Create your views here.
def index(request):
    if request.method == 'GET':
        feeds = Feed.objects.all()
        return render(request, 'feeds/index.html', {'feeds': feeds})
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Feed.objects.create(title=title, content=content)
        return redirect('/feeds')

def new(request):
    return render(request, 'feeds/new.html')

def show(request, id):
    if request.method == 'GET':
        feed = Feed.objects.get(id=id)
        return render(request, 'feeds/show.html', {'feed': feed})

def update(request, id):
    if request.method == 'GET':
        feed = Feed.objects.get(id=id)
        return render(request, 'feeds/update.html', {'feed': feed})
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Feed.objects.filter(id=id).update(title=title, content=content)
        return redirect('/feeds')

def delete(request, id):
    Feed.objects.get(id=id).delete()
    return redirect('/feeds')
