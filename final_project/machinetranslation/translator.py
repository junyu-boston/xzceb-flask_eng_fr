"""Module to translate between English and French
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

# Start an IBM LanguageTranslatorV3 instance
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(authenticator=authenticator, version="2022-04-28")

language_translator.set_service_url(url)

def english_to_french(english_text):
    """Translate english to French
    Input: English text (str)
    Output: French text (str)
    """
    if english_text == "":
        return ""
    tr_results = language_translator.translate(text=english_text, model_id="en-fr").get_result()
    french_text = tr_results['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """Translate French to English
    Input: French text (str)
    Output: English text (str)
    """
    if french_text == "":
        return ""
    tr_results = language_translator.translate(text=french_text, model_id="fr-en").get_result()
    english_text = tr_results['translations'][0]['translation']
    return english_text
