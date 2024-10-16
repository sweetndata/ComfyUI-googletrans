import os
import sys
import re
import googletrans

class GoogletransNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": "Hello, how are you?"}),
                "source_language": (googletrans.LANGUAGES, {"default": "en"}),
                "destination_language": (googletrans.LANGUAGES, {"default": "en"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("translated_text",)
    FUNCTION = "do_translate"
    CATEGORY = "text"

    def do_translate(self, text, source_language, destination_language):
        try :
            translator = googletrans.Translator()
            translated = translator.translate(text, src=source_language, dest=destination_language)
            return (translated.text,)
        except Exception as e:
            return (e,)

NODE_CLASS_MAPPINGS = {
    "googletrans": GoogletransNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "googletrans": "Google Translate"
}
