from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import MainForm
from .services import database_form
from .models import Feeds, Games, Trainers
from .models import Experience, WayWork, Education, Timetables


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


def programs(request):
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
            form_place = 'programs/form1'
            status = database_form.add_offer_to_db(name=data['name'], email=data['email'], form=form_place)
            form_status = True
            return render(request, 'programs/_index.html',
                                       {'form': form, "name": data['name'], 'form_status': form_status, "status": status})

    else:
        form_status = False
        form = MainForm()
        return render(request, 'programs/_index.html', {'form': form, 'form_status': form_status})


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


def coaching(request):
    """

    :param request:
    :return:
    """
    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form_place = 'coaching/form1'
            status = database_form.add_offer_to_db(name=data['name'], email=data['email'], form=form_place)
            form_status = True
            return render(request, 'coaching/_index.html',
                          {'form': form, "name": data['name'], 'form_status': form_status, "status": status})
    else:
        form_status = False
        form = MainForm()
        return render(request, 'coaching/_index.html', {'form': form, 'form_status': form_status})


def coaches(request):
    """

    :param request:
    :return:
    """
    coach_list = Trainers.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(coach_list, 4)
    try:
        coach_list = paginator.page(page)
    except PageNotAnInteger:
        coach_list = paginator.page(1)
    except EmptyPage:
        coach_list = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form_place = 'coaches/form1'
            status = database_form.add_offer_to_db(name=data['name'], email=data['email'], form=form_place)
            form_status = True
            return render(request, 'coaches/_index.html',
                          {'form': form, "name": data['name'], 'form_status': form_status, "status": status})
    else:
        form_status = False
        form = MainForm()
        return render(request, 'coaches/_index.html', {'form': form, 'form_status': form_status,
                                                       'coach_list': coach_list})


def coaches_detail(request, id):
    """

    :param request:
    :param id:
    :return:
    """
    coach = get_object_or_404(Trainers, id=id)
    ed = Education.objects.filter(coach=id)
    exp = Experience.objects.filter(coach=id)
    way = WayWork.objects.filter(coach=id)

    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form_place = 'coaches_detail/form1'
            status = database_form.add_offer_to_db(name=data['name'], email=data['email'], form=form_place)
            form_status = True
            return render(request, 'coaches_detail/_index.html',
                          {'form': form, "name": data['name'], 'form_status': form_status, "status": status})
    else:
        form_status = False
        form = MainForm()
    return render(request, 'coaches_detail/_index.html', {'form': form, 'coach': coach,
                                                          'ed': ed, 'exp': exp, 'way': way})


def games(request):
    """

    :param request:
    :return:
    """
    game_list = Games.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(game_list, 10)
    try:
        game_list = paginator.page(page)
    except PageNotAnInteger:
        game_list = paginator.page(1)
    except EmptyPage:
        game_list = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form_place = 'games/form1'
            status = database_form.add_offer_to_db(name=data['name'], email=data['email'], form=form_place)
            form_status = True

            return render(request, 'games/_index.html',
                          {'form': form, "name": data['name'], 'form_status': form_status, "status": status})
    else:
        form_status = False
        form = MainForm()
        return render(request, 'games/_index.html', {'form': form, 'form_status': form_status,
                                                     'game_list': game_list})


def games_detail(request, id):
    """

    :param request:
    :return:
    """
    game = get_object_or_404(Games, id=id)
    couch = get_object_or_404(Trainers, title=game.couch)

    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form_place = 'game/form1'
            status = database_form.add_offer_to_db(name=data['name'], email=data['email'], form=form_place)
            form_status = True
            return render(request, 'game/_index.html',
                          {'form': form, "name": data['name'], 'form_status': form_status, "status": status})
    else:
        form_status = False
        form = MainForm()
    return render(request, 'game/_index.html', {'form': form, 'game': game, 'couch': couch})


def timetable(request):
    """

    :param request:
    :return:
    """
    prog = Timetables.objects.all()
    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form_place = 'timetable/form1'
            status = database_form.add_offer_to_db(name=data['name'], email=data['email'], form=form_place)
            form_status = True
            return render(request, 'timetable/_index.html',
                          {'form': form, "name": data['name'], 'form_status': form_status, "status": status, 'prog': prog})
    else:
        form_status = False
        form = MainForm()
        return render(request, 'timetable/_index.html', {'form': form, 'form_status': form_status, 'prog': prog })
