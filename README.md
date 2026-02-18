# Translation Application

A web-based translation application that supports translation between three languages: English, Spanish, and French. Built with Flask and featuring both a user-friendly web interface and a RESTful API.

> **🚀 New here? Check the [QUICKSTART.md](QUICKSTART.md) for a fast guide on how to run and test the application!**

## Features

- 🌐 **Multi-language Support**: Translate between English, Spanish, and French
- 💻 **Web Interface**: Simple and intuitive UI for translations
- 🔌 **RESTful API**: Programmatic access to translation services
- ✅ **Input Validation**: Comprehensive error handling and validation
- 📱 **Responsive Design**: Works on desktop and mobile devices
- 🎨 **Modern UI**: Clean and attractive user interface

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/CODERACER123/translations.git
   cd translations
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask server**:
   ```bash
   python app.py
   ```

2. **Access the application**:
   - Open your web browser and navigate to: `http://localhost:5000`
   - The web interface will be displayed

3. **Stop the server**:
   - Press `Ctrl+C` in the terminal

## Using the Web Interface

1. **Select source and target languages** from the dropdown menus
2. **Enter text** in the left text area
3. **Click "Translate"** to see the translation in the right text area
4. **Use the swap button (⇄)** to quickly switch between languages
5. **Click "Clear"** to reset both text areas

## API Documentation

### Endpoints

#### 1. Translate Text

**Endpoint**: `POST /api/translate`

**Request Body**:
```json
{
  "text": "Hello",
  "source_lang": "en",
  "target_lang": "es"
}
```

**Response** (Success):
```json
{
  "success": true,
  "translation": "Hola",
  "source_lang": "en",
  "target_lang": "es",
  "original_text": "Hello"
}
```

**Response** (Error):
```json
{
  "success": false,
  "error": "Error message here"
}
```

**Example using curl**:
```bash
curl -X POST http://localhost:5000/api/translate \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello", "source_lang": "en", "target_lang": "es"}'
```

**Example using Python**:
```python
import requests

response = requests.post('http://localhost:5000/api/translate', json={
    'text': 'Hello',
    'source_lang': 'en',
    'target_lang': 'es'
})

data = response.json()
if data['success']:
    print(f"Translation: {data['translation']}")
```

#### 2. Get Supported Languages

**Endpoint**: `GET /api/languages`

**Response**:
```json
{
  "languages": [
    {"code": "en", "name": "English"},
    {"code": "es", "name": "Spanish"},
    {"code": "fr", "name": "French"}
  ]
}
```

**Example using curl**:
```bash
curl http://localhost:5000/api/languages
```

## Supported Languages

| Code | Language |
|------|----------|
| `en` | English  |
| `es` | Spanish  |
| `fr` | French   |

## Configuration

You can customize the application by modifying `config.py`:

- `MAX_TEXT_LENGTH`: Maximum characters allowed for translation (default: 5000)
- `SECRET_KEY`: Flask secret key (set via environment variable in production)
- `DEBUG`: Debug mode (set via `FLASK_DEBUG` environment variable)

## Project Structure

```
translations/
├── app.py              # Main Flask application
├── translator.py       # Translation service module
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Web interface template
├── static/
│   └── style.css      # CSS styling
└── README.md          # This file
```

## Error Handling

The application handles various error scenarios:

- **Empty text**: Returns error if no text is provided
- **Invalid languages**: Validates that languages are supported
- **Text too long**: Enforces maximum text length
- **Same source and target**: Prevents translation to the same language
- **Network errors**: Handles server connection issues gracefully

## Limitations

This application uses a dictionary-based translation approach for demonstration purposes. For production use, consider integrating with professional translation APIs like:

- Google Cloud Translation API
- Microsoft Azure Translator
- DeepL API
- Amazon Translate

## Development

### Running in Debug Mode

```bash
export FLASK_DEBUG=true  # On macOS/Linux
set FLASK_DEBUG=true     # On Windows
python app.py
```

### Adding New Translations

To add new word translations, edit the `translations` dictionary in `translator.py`:

```python
self.translations = {
    ('en', 'es'): {
        'new_word': 'palabra_nueva',
        # ... more translations
    }
}
```

## License

This project is open source and available for educational purposes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues, questions, or contributions, please open an issue on the GitHub repository.