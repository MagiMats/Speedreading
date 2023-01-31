import fitz
import os

from django.conf import settings
from json import dumps


def parse_text(pdf_path):
    path = os.path.join(settings.MEDIA_ROOT, str(pdf_path).replace(' ', '_'))
    pdf = fitz.open(path)
    text = ''
    array_text = []

    for index, page in enumerate(pdf):
        #text += page.get_text()
        array_text.append(page.get_text())

    for i,text in enumerate(array_text):
        text = repr(text)
        text = text.replace('\\t', ' ')
        text = text.replace('\\n', ' ')
        array_text[i] = text

    arrayJSON = dumps(array_text)
    return arrayJSON

