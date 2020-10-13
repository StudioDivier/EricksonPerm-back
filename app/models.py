from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Offers(models.Model):

    name = models.CharField(name="name", max_length=128)
    email = models.EmailField(name='email', unique=True)
    form = models.CharField(name="form", max_length=128)

    class Meta:
        verbose_name = 'Offer'
        verbose_name_plural = 'Offers'

    def __str__(self):
        return str(self.form)


class ProgramOffers(models.Model):

    program = models.CharField(name="program", max_length=128)
    name = models.CharField(name="name", max_length=128)
    phone = models.BigIntegerField(name="phone")

    class Meta:
        verbose_name = 'ProgramOffer'
        verbose_name_plural = 'ProgramOffers'

    def __str__(self):
        return str(self.program)


class Feeds(models.Model):

    img = models.ImageField(upload_to='feeds/')
    title = models.CharField(name="title", max_length=128)
    description_short = models.TextField(name="description_short")  # preview short
    description_long = models.TextField(name="description_long")  # long
    video_review = models.URLField(name='video_review')

    class Meta:
        verbose_name = 'Feed'
        verbose_name_plural = 'Feeds'

    def get_absolute_url(self):
        return reverse('index:feed_list', args=[self.id])


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


class Timetables(models.Model):

    date_day = models.IntegerField(name='date_day')
    month = models.CharField(name='date_month', max_length=64)
    start = models.TimeField(name='time_start')
    end = models.TimeField(name='time_end')
    long = models.CharField(name='long', max_length=64)
    title = models.CharField(name='title', max_length=128)
    description_short = models.TextField(name='description_short')
    way = models.CharField(name='way', max_length=128, null=True)

    class Meta:
        verbose_name = 'Timetable'
        verbose_name_plural = 'Timetables'

    def __str__(self):
        return str(self.title)



