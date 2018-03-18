# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import Post, User
from django.contrib import messages

# Create your views here.
def add_tweet(req):
    data = req.POST['tweet']
    post = Post()
    post.ptext = data
    post.save()
    return HttpResponseRedirect('/')

def show_tweets(req):
    all_posts = Post.objects.all()
    context = {'all' : all_posts, 'title' : 'My Tweets'}
    return render(req, 'index.html', context=context)

def create_user(req):
    if req.method == 'GET':
        context = {'title' : 'New User Registration'}
        return render(req, 'register.html', context=context)
    user = User()
    user.username     = req.POST['uname']
    user.first_name   = req.POST['fname']
    user.last_name    = req.POST['lname']
    user.email        = req.POST['email']
    user.password     = req.POST['password']
    user.save()
    messages.add_message(req, messages.SUCCESS, 'User registerd successfully')
    return HttpResponseRedirect('/')

def login_user(req):
    if req.method == 'GET':
        context = {'title' : 'Login'}
        return render(req, 'login.html', context=context)

    user = User.objects.filter(username=req.POST['uname'])
    print user
    print type(user)
    if user:
        if user[0].password == req.POST['password']:
            return HttpResponseRedirect('/')
        else:
            messages.add_message(req, messages.ERROR, 'Username or password does not match')
            return HttpResponseRedirect('/login/')
    else:
        messages.add_message(req, messages.ERROR, 'Username not found')
        return HttpResponseRedirect('/login/')