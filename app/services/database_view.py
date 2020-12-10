from django.conf import settings

from ..models import Feeds
from .. import models


def feed_list():
    feed = Feeds.objects.all()
    json: list = []
    for i in range(len(feed)):
        data = {
            'img': feed[i].img,
            'title': feed[i].title,
            'description': feed[i].description
        }
        json.append(data)


def meta(page):
    try:
        meta = {}
        meta_data = models.SEO.objects.get(path=page)
        meta['description'] = meta_data.description
        meta['keywords'] = meta_data.keywords
        meta['title'] = meta_data.title

        return meta

    except models.SEO.DoesNotExist:
        return False


def get_meta(page):
    meta_data = meta(page=page)
    if not meta_data:
        data = settings.PAGES
        for item in range(len(data)):
            if data[item][0] == page:
                word = str(data[item][1])
        description = 'description of page {}'.format(word)
        keywords = 'keywords for page {}'.format(word)
        title = 'EricksonPerm - {}'.format(word)
    else:
        description = meta_data.get('description')
        keywords = meta_data.get('keywords')
        title = meta_data.get('title')

    return description, keywords, title
