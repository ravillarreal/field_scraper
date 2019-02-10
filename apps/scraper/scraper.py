import requests
from bs4 import BeautifulSoup
from apps.scraper.models import Element, Tag, Value, Attribute


def get_fields():
    url = 'https://google.com'

    response = requests.get(url)
    soup = BeautifulSoup(response.content)

    for item in soup.find_all('input'):
        tag, created = Tag.objects.get_or_create(
            name=item.name,
            defaults={"name": item.name}
        )
        element, created = Element.objects.update_or_create(
            text=item.text,
            tag=tag,
            parent=None
        )
        for key, value in item.attrs.items():
            att_obj, created = Attribute.objects.get_or_create(
                name=key
            )
            Value.objects.update_or_create(
                element=element,
                attribute=att_obj,
                value=value
            )
