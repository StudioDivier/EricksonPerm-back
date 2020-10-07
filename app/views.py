from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import MainForm
from .services import database_form


def index(request):
    """
    Отрисовка главной страницы
        методы POST для формы1
    :param request:
    :return: render index.html
    """
    if request.method == 'POST':
        form = MainForm(request.POST)
        status = True
        if form.is_valid():
            data = form.cleaned_data
            try:
                form_place = 'index/form1'
                database_form.add_offer_to_db(name=data['name'], email=data['email'], form=form_place)
            except Exception('Ощибка записи в базу данных'):
                status = False
                return render(request, 'test.html', {"name": data['name']})

            return HttpResponse(render(request, 'test.html', {"name": data['name']}))

    else:
        form = MainForm()

    return render(request, 'main/_index.html', {'form': form})
