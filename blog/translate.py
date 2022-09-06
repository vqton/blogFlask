import requests
from flask_babel import Babel, _


def translate(text, source_language, dest_language):

    subscription_key = "ec04acf9f7f54096b7c12cc0da052073"
    location = "southeastasia"
    auth = {
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Ocp-Apim-Subscription-Region": location,
    }
    r = requests.post(
        "https://api.cognitive.microsofttranslator.com"
        "/translate?api-version=3.0&from={}&to={}".format(
            source_language, dest_language
        ),
        headers=auth,
        json=[{"Text": text}],
    )
    if r.status_code != 200:
        return _("Error: the translation service failed.")
    return r.json()[0]["translations"][0]["text"]
