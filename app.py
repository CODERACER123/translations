"""Flask application for translation service."""
from flask import Flask, render_template, request, jsonify
from translator import TranslationService
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

# Initialize translation service
translator = TranslationService()


@app.route('/')
def index():
    """Render the main web interface."""
    languages = {
        'en': 'English',
        'es': 'Spanish',
        'fr': 'French'
    }
    return render_template('index.html', languages=languages)


@app.route('/api/translate', methods=['POST'])
def api_translate():
    """
    API endpoint for translation requests.
    
    Expected JSON payload:
    {
        "text": "text to translate",
        "source_lang": "en",
        "target_lang": "es"
    }
    
    Returns:
    {
        "success": true,
        "translation": "translated text",
        "source_lang": "en",
        "target_lang": "es"
    }
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'error': 'No JSON data provided'
            }), 400
        
        # Extract parameters
        text = data.get('text', '').strip()
        source_lang = data.get('source_lang', '').strip().lower()
        target_lang = data.get('target_lang', '').strip().lower()
        
        # Validate input
        if not text:
            return jsonify({
                'success': False,
                'error': 'Text parameter is required'
            }), 400
        
        if not source_lang:
            return jsonify({
                'success': False,
                'error': 'source_lang parameter is required'
            }), 400
        
        if not target_lang:
            return jsonify({
                'success': False,
                'error': 'target_lang parameter is required'
            }), 400
        
        # Check text length
        if len(text) > app.config['MAX_TEXT_LENGTH']:
            return jsonify({
                'success': False,
                'error': f'Text exceeds maximum length of {app.config["MAX_TEXT_LENGTH"]} characters'
            }), 400
        
        # Validate languages
        if source_lang not in app.config['SUPPORTED_LANGUAGES']:
            return jsonify({
                'success': False,
                'error': f'Source language "{source_lang}" is not supported. Supported languages: {", ".join(app.config["SUPPORTED_LANGUAGES"])}'
            }), 400
        
        if target_lang not in app.config['SUPPORTED_LANGUAGES']:
            return jsonify({
                'success': False,
                'error': f'Target language "{target_lang}" is not supported. Supported languages: {", ".join(app.config["SUPPORTED_LANGUAGES"])}'
            }), 400
        
        # Perform translation
        translation = translator.translate(text, source_lang, target_lang)
        
        return jsonify({
            'success': True,
            'translation': translation,
            'source_lang': source_lang,
            'target_lang': target_lang,
            'original_text': text
        }), 200
        
    except ValueError as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'An unexpected error occurred'
        }), 500


@app.route('/api/languages', methods=['GET'])
def api_languages():
    """
    API endpoint to get supported languages.
    
    Returns:
    {
        "languages": [
            {"code": "en", "name": "English"},
            {"code": "es", "name": "Spanish"},
            {"code": "fr", "name": "French"}
        ]
    }
    """
    languages = [
        {'code': code, 'name': name}
        for code, name in app.config['LANGUAGE_NAMES'].items()
    ]
    return jsonify({
        'languages': languages
    }), 200


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({
        'success': False,
        'error': 'Resource not found'
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 errors."""
    return jsonify({
        'success': False,
        'error': 'Method not allowed'
    }), 405


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500


if __name__ == '__main__':
    # Use configuration from Config class for debug mode
    # Only bind to all interfaces in development
    import os
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    host = '0.0.0.0' if debug_mode else '127.0.0.1'
    app.run(debug=debug_mode, host=host, port=5000)
