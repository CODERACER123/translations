"""Configuration settings for the translation application."""
import os


class Config:
    """Base configuration class."""
    
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    # Application settings
    SUPPORTED_LANGUAGES = ['en', 'es', 'fr']
    LANGUAGE_NAMES = {
        'en': 'English',
        'es': 'Spanish',
        'fr': 'French'
    }
    
    # Translation settings
    MAX_TEXT_LENGTH = 5000  # Maximum characters for translation
