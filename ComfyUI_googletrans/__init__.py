import googletrans
import logging

class GoogletransNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_text": ("STRING", {"multiline": True, "default": "Hello, how are you?"}),
                "source_language": (["auto"] + list(googletrans.LANGUAGES.values()), {"default": "english"}),
                "destination_language": (list(googletrans.LANGUAGES.values()), {"default": "english"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("translated_text",)
    FUNCTION = "do_translate"
    CATEGORY = "text"

    def do_translate(self, input_text, source_language, destination_language, *args, **kwargs):
        try :
            translator = googletrans.Translator()
            translated = translator.translate(input_text, src=source_language, dest=destination_language)
            return (translated.text,)
        except Exception as e:
            logging.exception(f"Error translating text. args={args}, kwargs={kwargs}")
            return (e,)

class ViewTextNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": "Hello, how are you?"}),
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "do_view_text"
    OUTPUT_NODE = True
    CATEGORY = "text"

    def do_view_text(self, text):
        return {"ui": {"text": text}}

NODE_CLASS_MAPPINGS = {
    "googletrans": GoogletransNode,
    "view_text": ViewTextNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "googletrans": "Google Translate",
    "view_text": "View Text",
}
