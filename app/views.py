from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import MainForm
from .services import database_form
from .models import Feeds


def index(request):
    """
    Отрисовка главной страницы
        методы POST для формы1
    :param request:
    :return: render index.html
    """
    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form_place = 'index/form1'
            status = database_form.add_offer_to_db(name=data['name'], email=data['email'], form=form_place)
            form_status = True
            return render(request, 'main/_index.html',
                                       {'form': form, "name": data['name'], 'form_status': form_status, "status": status})

    else:
        form_status = False
        form = MainForm()
        return render(request, 'main/_index.html', {'form': form, 'form_status': form_status})


def feed_list(request):
    """

    :param request:
    :return:
    """
    feeds = Feeds.objects.all()
    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form_place = 'feed-list/form1'
            status = database_form.add_offer_to_db(name=data['name'], email=data['email'], form=form_place)
            form_status = True
            return render(request, 'feed_list/_index.html',
                          {'feeds': feeds, 'form': form, "name": data['name'], 'form_status': form_status, "status": status})
    else:
        form_status = False
        form = MainForm()
        return render(request, 'feed_list/_index.html', {'feeds': feeds, 'form': form, 'form_status': form_status})


def feed_detail(request, id):
    """

    :param request:
    :param id:
    :return:
    """
    review = get_object_or_404(Feeds, id=id)

    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form_place = 'reviews-detailed/form1'
            status = database_form.add_offer_to_db(name=data['name'], email=data['email'], form=form_place)
            form_status = True
            return render(request, 'reviews-detailed/reviews-detailed.html',
                          {'form': form, "name": data['name'], 'form_status': form_status, "status": status})
    else:
        form_status = False
        form = MainForm()
    return render(request, 'reviews-detailed/reviews-detailed.html', {'form': form, 'review': review})


def contacts(request):
    """

    :param request:
    :return:
    """
    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form_place = 'contacts/form1'
            status = database_form.add_offer_to_db(name=data['name'], email=data['email'], form=form_place)
            form_status = True
            return render(request, 'contacts/_index.html',
                          {'form': form, "name": data['name'], 'form_status': form_status, "status": status})
    else:
        form_status = False
        form = MainForm()
        return render(request, 'contacts/_index.html', {'form': form, 'form_status': form_status})


def about(request):
    """

    :param request:
    :return:
    """
    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form_place = 'about/form1'
            status = database_form.add_offer_to_db(name=data['name'], email=data['email'], form=form_place)
            form_status = True
            return render(request, 'about/_index.html',
                          {'form': form, "name": data['name'], 'form_status': form_status, "status": status})
    else:
        form_status = False
        form = MainForm()
        return render(request, 'about/_index.html', {'form': form, 'form_status': form_status})