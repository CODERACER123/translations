"""Translation service module for handling text translations between languages."""


class TranslationService:
    """Service for translating text between English, Spanish, and French."""
    
    def __init__(self):
        """Initialize the translation service with basic dictionaries."""
        # Simple dictionary-based translations for demonstration
        # In production, you would use a proper translation API like Google Translate
        self.translations = {
            # English to Spanish
            ('en', 'es'): {
                'hello': 'hola',
                'goodbye': 'adiós',
                'please': 'por favor',
                'thank you': 'gracias',
                'yes': 'sí',
                'no': 'no',
                'good morning': 'buenos días',
                'good evening': 'buenas noches',
                'how are you': 'cómo estás',
                'welcome': 'bienvenido',
                'friend': 'amigo',
                'family': 'familia',
                'love': 'amor',
                'water': 'agua',
                'food': 'comida',
            },
            # English to French
            ('en', 'fr'): {
                'hello': 'bonjour',
                'goodbye': 'au revoir',
                'please': 's\'il vous plaît',
                'thank you': 'merci',
                'yes': 'oui',
                'no': 'non',
                'good morning': 'bonjour',
                'good evening': 'bonsoir',
                'how are you': 'comment allez-vous',
                'welcome': 'bienvenue',
                'friend': 'ami',
                'family': 'famille',
                'love': 'amour',
                'water': 'eau',
                'food': 'nourriture',
            },
            # Spanish to English
            ('es', 'en'): {
                'hola': 'hello',
                'adiós': 'goodbye',
                'por favor': 'please',
                'gracias': 'thank you',
                'sí': 'yes',
                'no': 'no',
                'buenos días': 'good morning',
                'buenas noches': 'good evening',
                'cómo estás': 'how are you',
                'bienvenido': 'welcome',
                'amigo': 'friend',
                'familia': 'family',
                'amor': 'love',
                'agua': 'water',
                'comida': 'food',
            },
            # Spanish to French
            ('es', 'fr'): {
                'hola': 'bonjour',
                'adiós': 'au revoir',
                'por favor': 's\'il vous plaît',
                'gracias': 'merci',
                'sí': 'oui',
                'no': 'non',
                'buenos días': 'bonjour',
                'buenas noches': 'bonsoir',
                'cómo estás': 'comment allez-vous',
                'bienvenido': 'bienvenue',
                'amigo': 'ami',
                'familia': 'famille',
                'amor': 'amour',
                'agua': 'eau',
                'comida': 'nourriture',
            },
            # French to English
            ('fr', 'en'): {
                'bonjour': 'hello',
                'au revoir': 'goodbye',
                's\'il vous plaît': 'please',
                'merci': 'thank you',
                'oui': 'yes',
                'non': 'no',
                'bonsoir': 'good evening',
                'comment allez-vous': 'how are you',
                'bienvenue': 'welcome',
                'ami': 'friend',
                'famille': 'family',
                'amour': 'love',
                'eau': 'water',
                'nourriture': 'food',
            },
            # French to Spanish
            ('fr', 'es'): {
                'bonjour': 'hola',
                'au revoir': 'adiós',
                's\'il vous plaît': 'por favor',
                'merci': 'gracias',
                'oui': 'sí',
                'non': 'no',
                'bonsoir': 'buenas noches',
                'comment allez-vous': 'cómo estás',
                'bienvenue': 'bienvenido',
                'ami': 'amigo',
                'famille': 'familia',
                'amour': 'amor',
                'eau': 'agua',
                'nourriture': 'comida',
            },
        }
    
    def translate(self, text, source_lang, target_lang):
        """
        Translate text from source language to target language.
        
        Args:
            text (str): Text to translate
            source_lang (str): Source language code ('en', 'es', 'fr')
            target_lang (str): Target language code ('en', 'es', 'fr')
            
        Returns:
            str: Translated text
            
        Raises:
            ValueError: If languages are not supported or if text is invalid
        """
        if not text:
            raise ValueError("Text cannot be empty")
        
        # Validate languages
        supported_langs = ['en', 'es', 'fr']
        if source_lang not in supported_langs:
            raise ValueError(f"Source language '{source_lang}' is not supported")
        if target_lang not in supported_langs:
            raise ValueError(f"Target language '{target_lang}' is not supported")
        
        # If source and target are the same, return original text
        if source_lang == target_lang:
            return text
        
        # Get translation dictionary for this language pair
        trans_dict = self.translations.get((source_lang, target_lang), {})
        
        # Convert text to lowercase for lookup
        text_lower = text.lower().strip()
        
        # Try exact match first
        if text_lower in trans_dict:
            # Preserve original capitalization pattern
            translated = trans_dict[text_lower]
            if text[0].isupper():
                translated = translated.capitalize()
            return translated
        
        # Try word-by-word translation
        words = text.split()
        translated_words = []
        
        for word in words:
            word_lower = word.lower().strip('.,!?;:')
            punctuation = ''
            
            # Preserve punctuation
            if word and not word[-1].isalnum():
                punctuation = word[-1]
            
            if word_lower in trans_dict:
                translated_word = trans_dict[word_lower]
                # Preserve capitalization
                if word[0].isupper():
                    translated_word = translated_word.capitalize()
                translated_words.append(translated_word + punctuation)
            else:
                # If word not found, keep original
                translated_words.append(word)
        
        result = ' '.join(translated_words)
        
        # If no words were translated, return a note
        if result.lower() == text.lower():
            return f"[Translation not available] {text}"
        
        return result
    
    def get_supported_languages(self):
        """
        Get list of supported language codes.
        
        Returns:
            list: List of supported language codes
        """
        return ['en', 'es', 'fr']
    
    def get_language_name(self, lang_code):
        """
        Get human-readable name for a language code.
        
        Args:
            lang_code (str): Language code
            
        Returns:
            str: Language name
        """
        names = {
            'en': 'English',
            'es': 'Spanish',
            'fr': 'French'
        }
        return names.get(lang_code, lang_code)
