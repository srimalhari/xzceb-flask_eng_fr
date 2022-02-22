import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


def english_to_french(english_text):

    """This function get an english string as input and translate it french. 
    Returns the french text."""

    englishtranslation = language_translator.translate(text=english_text, model_id='en-fr')
    translation=englishtranslation.get_result()
    french_text = translation['translations'][0]['translation']
    return french_text


def french_to_english(french_text):

    """This function get an french string as input and translate it english. 
    Returns the english text."""

    frenchtranslation = language_translator.translate(text=french_text, model_id='fr-en')
    translation=frenchtranslation.get_result()
    english_text = translation['translations'][0]['translation']
    return english_text

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version_It = '2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=version_It, authenticator=authenticator)
language_translator.set_service_url(url)
