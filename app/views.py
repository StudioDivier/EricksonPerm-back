import re

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import MainForm
from .services import database_form, database_view
from . import models
from .models import Feeds, Games, Trainers
from .models import Experience, WayWork, Education, Timetables


def index(request):
    """
    Отрисовка главной страницы
        методы POST для формы1
    :param request:
    :return: render index.html
    """

    description, keywords, title = database_view.get_meta(page=request.path)
    feeds = models.Feeds.objects.all().order_by('id')

    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form_place = 'index/form1'
            status = database_form.add_offer_to_db(name=data['name'], email=data['email'], form=form_place)
            form_status = True
            return render(request, 'main/_index.html',
                                       {'form': form, "name": data['name'], 'form_status': form_status,
                                        "status": status, "feeds": feeds})

    else:
        form_status = False
        form = MainForm()
        return render(request, 'main/_index.html', {'form': form, 'form_status': form_status, 'title': title,
                                                     'description': description, 'keywords': keywords, "feeds": feeds})


def programs(request):
    """
    Отрисовка главной страницы
        методы POST для формы1
    :param request:
    :return: render index.html
    """
    description, keywords, title = database_view.get_meta(page=request.path)

    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form_place = 'programs/form1'
            status = database_form.add_offer_to_db(name=data['name'], email=data['email'], form=form_place)
            form_status = True
            return render(request, 'programs/_index.html',
                                       {'form': form, "name": data['name'], 'form_status': form_status,
                                        "status": status, 'title': title, 'description': description,
                                        'keywords': keywords})

    else:
        form_status = False
        form = MainForm()
        return render(request, 'programs/_index.html', {'form': form, 'form_status': form_status, 'title': title,
                                                        'description': description, 'keywords': keywords})


def news(request):
    """
    Отрисовка главной страницы
        методы POST для формы1
    :param request:
    :return: render index.html
    """
    description, keywords, title = database_view.get_meta(page=request.path)

    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form_place = 'news/form1'
            status = database_form.add_offer_to_db(name=data['name'], email=data['email'], form=form_place)
            form_status = True
            return render(request, 'news/_index.html',
                                       {'form': form, "name": data['name'], 'form_status': form_status,
                                        "status": status, 'title': title, 'description': description,
                                        'keywords': keywords})

    else:
        form_status = False
        form = MainForm()
        return render(request, 'news/_index.html', {'form': form, 'form_status': form_status, 'title': title,
                                                        'description': description, 'keywords': keywords})


def feed_list(request):
    """

    :param request:
    :return:
    """
    description, keywords, title = database_view.get_meta(page=request.path)

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
        return render(request, 'feed_list/_index.html', {'feeds': feeds, 'form': form, 'form_status': form_status, 'title': title,
                                                     'description': description, 'keywords': keywords})


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
    description, keywords, title = database_view.get_meta(page=request.path)

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
        return render(request, 'contacts/_index.html', {'form': form, 'form_status': form_status, 'title': title,
                                                     'description': description, 'keywords': keywords})


def about(request):
    """

    :param request:
    :return:
    """
    description, keywords, title = database_view.get_meta(page=request.path)

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
        return render(request, 'about/_index.html', {'form': form, 'form_status': form_status, 'title': title,
                                                     'description':description, 'keywords': keywords})


def coaching(request):
    """

    :param request:
    :return:
    """
    description, keywords, title = database_view.get_meta(page=request.path)

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
        return render(request, 'coaching/_index.html', {'form': form, 'form_status': form_status, 'title': title,
                                                     'description':description, 'keywords': keywords})


def coaches(request):
    """

    :param request:
    :return:
    """
    description, keywords, title = database_view.get_meta(page=request.path)

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
                                                       'coach_list': coach_list, 'title': title,
                                                     'description':description, 'keywords': keywords})


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
    description, keywords, title = database_view.get_meta(page=request.path)

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
                                                     'game_list': game_list, 'title': title,
                                                     'description':description, 'keywords': keywords})


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
    description, keywords, title = database_view.get_meta(page=request.path)

    prog = Timetables.objects.all()
    way_t = models.WayCouch.objects.all()
    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form_place = 'timetable/form1'
            status = database_form.add_offer_to_db(name=data['name'], email=data['email'], form=form_place)
            form_status = True
            return render(request, 'timetable/_index.html',
                          {'form': form, "name": data['name'], 'form_status': form_status, "status": status,
                           'prog': prog, 'way_t': way_t})
    else:
        form_status = False
        form = MainForm()
        return render(request, 'timetable/_index.html', {'form': form, 'form_status': form_status, 'prog': prog,
                                                         'way_t': way_t, 'title': title,
                                                     'description':description, 'keywords': keywords})


def timetable_filter(request):
    """

    :param request:
    :return:
    """
    description, keywords, title = database_view.get_meta(page=request.path)

    data_from = tuple(request.GET.get('from').split('.'))
    data_to = tuple(request.GET.get('to').split('.'))
    response = []

    if request.GET.get('way_id') != None:
        s = str(request)
        print(s)
        s1 = re.findall(r'way_id=\d+', s)
        for i in range(len(s1)):
            s1[i] = s[i].replace('way_id=', '')
        for data_way in range(len(s1)):
            prog_type = Timetables.objects.filter(way_id=data_way).values()

            for item in prog_type:
                date = tuple(str(item['date_full']).split('-')[::-1])
                if (data_from <= date <= data_to) and (item['way_id'] == data_way):
                    response.append(item)
                else:
                    continue
    else:
        prog_type = Timetables.objects.all().values()
        for item in prog_type:
            date = tuple(str(item['date_full']).split('-')[::-1])
            if (data_from <= date <= data_to):
                response.append(item)
            else:
                continue

    if len(response) == 0:
        data = True
    else:
        data = False

    way_t = models.WayCouch.objects.all()
    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form_place = 'timetable/form1'
            status = database_form.add_offer_to_db(name=data['name'], email=data['email'], form=form_place)
            form_status = True
            return render(request, 'timetable/_index.html',
                          {'form': form, "name": data['name'], 'form_status': form_status, "status": status,
                           'prog': response, 'way_t': way_t})
    else:
        form_status = False
        form = MainForm()
        return render(request, 'timetable/_index.html', {'form': form, 'form_status': form_status, 'prog': response,
                                                         'way_t': way_t, 'title': title,
                                                        'description':description, 'keywords': keywords, 'data': data})


