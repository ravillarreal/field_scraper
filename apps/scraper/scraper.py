import requests
from bs4 import BeautifulSoup
from apps.scraper.models import Element, Tag, Value, Attribute


def get_fields():
    url = 'http://www.chileautos.cl'
    user_agent = {'User-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
    response = requests.get(url, headers=user_agent)
    soup = BeautifulSoup(response.content)

    for item in soup.select('form input'):
        tag, created = Tag.objects.get_or_create(
            name=item.name,
        )
        element = Element.objects.create(
            text=item.text,
            tag=tag
        )
        for key, value in item.attrs.items():
            att_obj, created = Attribute.objects.get_or_create(
                name=key
            )
            Value.objects.update_or_create(
                element=element,
                attribute=att_obj,
                defaults={"value": value}
            )
    else:
        return False
