import io
import os

from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()

# These labels must be amongst recognized labels
REQUIRED_LABELS = set(['identity document', 'face', 'text'])
REQUIRED_USER_FIELDS = ['first_name', 'last_name']

def validate_labels(ic_image_uri):
    response = client.label_detection({'source': {'image_uri': ic_image_uri}})
    labels = set([label.description for label in response.label_annotations])

    return REQUIRED_LABELS < labels


def validate_texts(user, ic_image_uri):
    response = client.text_detection({'source': {'image_uri': ic_image_uri}})
    text = response.full_text_annotation.text.lower()

    for field in REQUIRED_USER_FIELDS:
        if not user[field].lower() in text: return False

    return True

def validate_identity_card(user, ic_image_uri):
    return validate_labels(ic_image_uri) and validate_texts(user, ic_image_uri)
