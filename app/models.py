from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings


# СЕО статичных страниц
class SEO(models.Model):
    path = models.CharField(name='path', verbose_name='Адрес страницы', max_length=32, unique=True,
                            choices=settings.PAGES
                            )
    title = models.CharField(name='title', verbose_name='Титульник страницы', max_length=128)
    keywords = models.CharField(name='keywords', verbose_name='Ключевые слова', max_length=1024)
    description = models.CharField(name='description', verbose_name='Описание', max_length=2048)

    class Meta:
        verbose_name = 'СЕО страницы'
        verbose_name_plural = 'СЕО страниц'

    def __str__(self):
        return str(self.title)


# заявки
class Offers(models.Model):

    name = models.CharField(name="name", max_length=128)
    email = models.EmailField(name='email', unique=True)
    form = models.CharField(name="form", max_length=128)

    class Meta:
        verbose_name = 'Offer'
        verbose_name_plural = 'Offers'

    def __str__(self):
        return str(self.form)


# программы
class ProgramOffers(models.Model):

    program = models.CharField(name="program", max_length=128)
    name = models.CharField(name="name", max_length=128)
    phone = models.BigIntegerField(name="phone")

    class Meta:
        verbose_name = 'ProgramOffer'
        verbose_name_plural = 'ProgramOffers'

    def __str__(self):
        return str(self.program)


# отзывы
class Feeds(models.Model):

    img_detail = models.ImageField(upload_to='feeds/', verbose_name='Изображение на странице отзывов')
    img_detail_alt = models.CharField(name='img_detail_alt', max_length=128, verbose_name='Изображение на странице отзывов (Alt)')
    img_main = models.ImageField(upload_to='feeds/', verbose_name='Изображение на главной странице')
    img_main_alt = models.CharField(name='img_main_alt', max_length=128, verbose_name='Изображение на главной странице (Alt)')
    title = models.CharField(name="title", max_length=128, verbose_name='Заголовок')
    description_short = models.TextField(name="description_short", verbose_name='Описание короткое')  # preview short
    description_long = models.TextField(name="description_long", verbose_name='Описание полное')  # long
    video_review = models.URLField(name='video_review', verbose_name='Видео')

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'

    def get_absolute_url(self):
        return reverse('index:feed_list', args=[self.id])

    def __str__(self):
        return str(self.title)


# тренеры
class Trainers(models.Model):

    title = models.CharField(name="title", max_length=128)
    description = models.TextField(name="description")
    img = models.ImageField(upload_to='coach_detail/')

    class Meta:
        verbose_name = 'Trainer'
        verbose_name_plural = 'Trainers'

    def get_absolute_url(self):
        return reverse('index:coaches_detail', args=[self.id])



    def __str__(self):
        return str(self.title)


class Education(models.Model):
    coach = models.ForeignKey(Trainers, on_delete=models.SET_NULL, null=True)
    start = models.IntegerField(name='start_ed')
    end = models.IntegerField(name='end_ed')
    ed_title = models.CharField(name='ed_title', max_length=256)

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'

    def __str__(self):
        return str(self.coach.title)


class Experience(models.Model):
    coach = models.ForeignKey(Trainers, on_delete=models.SET_NULL, null=True)
    start_exp = models.IntegerField(name='start_exp')
    title_exp = models.CharField(name='title_exp', max_length=256)

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'

    def __str__(self):
        return str(self.coach.title)


class WayWork(models.Model):
    coach = models.ForeignKey(Trainers, on_delete=models.SET_NULL, null=True)
    way = models.CharField(name='way', max_length=64)

    class Meta:
        verbose_name = 'WayWork'
        verbose_name_plural = 'WayWork'

    def __str__(self):
        return str(self.coach.title)


# игры
class Games(models.Model):

    title = models.CharField(name="title", max_length=128)
    title_short = models.CharField(name="title_short", max_length=64, null=True)
    img = models.ImageField(upload_to='games/')
    price = models.DecimalField(name='price', max_digits=9, decimal_places=2)
    description_short = models.TextField(name="description_short")
    couch = models.ForeignKey(Trainers, on_delete=models.SET_NULL, null=True)
    date_day = models.IntegerField(name='date_day', null=True)
    date_month = models.IntegerField(name='date_month', null=True)
    date_year = models.IntegerField(name='date_year', null=True)
    long = models.CharField(name='long', max_length=64, null=True)
    description = RichTextUploadingField(null=True)

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('index:games_detail', args=[self.id])


# Расписание
class WayCouch(models.Model):

    way_t = models.CharField(name='way_t', max_length=128)

    class Meta:
        verbose_name = 'Направление коуча'
        verbose_name_plural = 'Направления коучинга'

    def __str__(self):
        return str(self.way_t)


class Timetables(models.Model):

    date_day = models.IntegerField(name='date_day')
    month = models.CharField(name='date_month', max_length=64)
    date_full = models.DateField(name='date_full')
    start = models.TimeField(name='time_start')
    end = models.TimeField(name='time_end')
    long = models.CharField(name='long', max_length=64)
    title = models.CharField(name='title', max_length=128)
    description_short = models.TextField(name='description_short')
    way = models.ForeignKey(WayCouch, on_delete=models.CASCADE)
    price = models.CharField(name='price', max_length=16)

    class Meta:
        verbose_name = 'Timetable'
        verbose_name_plural = 'Timetables'

    def __str__(self):
        return str(self.title)


# Новости
class News(models.Model):
    img = models.ImageField(upload_to='news/', verbose_name='Изображение новости')
    img_alt = models.CharField(name='img_alt', verbose_name='alt изображение', max_length=32)
    date = models.DateField(name='date', verbose_name='Дата')
    title = models.CharField(name='title', verbose_name='Загаловок', max_length=128)
    description = models.CharField(name='description', verbose_name='Описание', max_length=256)
    keywords_seo = models.CharField(name='keywords_seo', verbose_name='Ключевые слова для СЕО', max_length=1024)
    description_seo = models.CharField(name='description_seo', verbose_name='Описание для СЕО', max_length=2048)

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return 'Новость {}'.format(self.title)

