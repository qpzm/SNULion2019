from django.shortcuts import render
from .models import Feed, FeedComment, Like, Follow
from django.contrib.auth.models import User
from django.shortcuts import redirect


# Create your views here.
def index(request):
    if request.method == 'GET':
        feeds = Feed.objects.all()
        return render(request, 'feeds/index.html', {'feeds': feeds})
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Feed.objects.create(title=title,
                            content=content,
                            author=User.objects.get(id=request.user.id))
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


def create_comment(request, id):
    content = request.POST['content']
    FeedComment.objects.create(feed_id=id,
                               content=content,
                               author=User.objects.get(id=request.user.id))
    return redirect('/feeds')


def delete_comment(request, id, cid):
    comment = FeedComment.objects.get(id=cid)
    comment.delete()
    return redirect('/feeds')


def feed_like(request, pk):
    feed = Feed.objects.get(id=pk)
    likes = feed.like_set.filter(user_id=request.user.id)
    if likes.count() > 0:
        feed.like_set.get(user_id=request.user.id).delete()
    else:
        Like.objects.create(user_id=request.user.id, feed_id=feed.id)
    return redirect('/feeds')


def follow_manager(request, pk):
    # Note! Follow between Profiles not User
    sender_id = request.user.profile.id
    follows = Follow.objects.filter(sender_id=sender_id, receiver_id=pk)
    if follows.count() == 0:
        Follow.objects.create(sender_id=sender_id, receiver_id=pk)
    else:
        follows.delete()
    return redirect('/feeds')
