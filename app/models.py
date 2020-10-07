from django.db import models
from django.conf import settings


class Offers(models.Model):

    name = models.CharField(name="name", max_length=128)
    email = models.EmailField(name='email')
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

    img = models.FilePathField(name="img", path=settings.MEDIA_URL)
    title = models.CharField(name="title", max_length=128)
    description = models.TextField(name="description")

    class Meta:
        verbose_name = 'Feed'
        verbose_name_plural = 'Feeds'


class Telephone(models.Model):

    phone = models.BigIntegerField(name="phone")
    name = models.CharField(name="name", max_length=128)

    class Meta:
        verbose_name = 'Telephone'
        verbose_name_plural = 'Telephones'


class Staff(models.Model):

    img = models.FilePathField(name="img", path=settings.MEDIA_URL)
    fio = models.CharField(name="fio", max_length=128)
    content = models.CharField(name="name", max_length=128)
    phone = models.BigIntegerField(name="phone")
    email = models.EmailField(name='email')

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staffs'


class InfoCompany(models.Model):

    phone = models.ForeignKey(Telephone, on_delete=models.CASCADE)
    email = models.EmailField(name='email')
    adress = models.CharField(name='adress', max_length=256)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    vk = models.URLField(name='vk')
    fb = models.URLField(name='fb')
    inst = models.URLField(name='inst')

    class Meta:
        verbose_name = 'InfoCompany'
        verbose_name_plural = 'InfoCompanies'

