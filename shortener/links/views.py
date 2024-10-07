from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Link
from .forms import LinkForm


def create_link(request):
    form = LinkForm(request.POST or None)
    short_url = None
    original_url = None
    if form.is_valid():
        link = form.save()
        short_url = request.build_absolute_uri('/') + link.short_url
        original_url = link.original_url
    return render(request, 'links/create_link.html', {
        'form': form,
        'short_url': short_url,
        'original_url': original_url
    })


def link_list(request):
    links = Link.objects.all()
    return render(request, 'links/link_list.html', {'links': links})


def redirect_link(request, short_url):
    link = get_object_or_404(Link, short_url=short_url)
    return HttpResponseRedirect(link.original_url)
