from ..models import Feeds

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