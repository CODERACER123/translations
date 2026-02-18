# Quick Start Guide

## 🚀 Where to Check the Translation Application

### 1. **Read the Full Documentation**
📖 **Check the [README.md](README.md)** - Contains complete setup instructions, API documentation, and usage examples.

### 2. **Run the Application** (3 Simple Steps)

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Start the server
python app.py

# Step 3: Open in your browser
# Go to: http://localhost:5000
```

### 3. **Access the Web Interface**
🌐 **Open your browser and visit:** `http://localhost:5000`

You'll see a beautiful translation interface where you can:
- Translate between English, Spanish, and French
- Swap languages with one click
- See character counts
- Get instant translations

### 4. **Test the API**

Try this command in your terminal:

```bash
curl -X POST http://localhost:5000/api/translate \
  -H "Content-Type: application/json" \
  -d '{"text": "hello", "source_lang": "en", "target_lang": "es"}'
```

**Expected Response:**
```json
{
  "success": true,
  "translation": "hola",
  "source_lang": "en",
  "target_lang": "es",
  "original_text": "hello"
}
```

### 5. **Check the Code**

📂 **Main Files:**
- **`app.py`** - Flask application with API endpoints
- **`translator.py`** - Translation logic
- **`templates/index.html`** - Web interface
- **`static/style.css`** - Styling

### 6. **API Endpoints**

Once the server is running, you can check:

- **Web Interface:** `http://localhost:5000/`
- **Translation API:** `POST http://localhost:5000/api/translate`
- **Languages List:** `GET http://localhost:5000/api/languages`

## 🎯 Quick Test

After starting the application:

1. **Via Web Browser:**
   - Go to `http://localhost:5000`
   - Type "hello friend" in the text box
   - Select "English" to "Spanish"
   - Click "Translate"
   - You should see "hola amigo"

2. **Via Command Line:**
   ```bash
   # Get supported languages
   curl http://localhost:5000/api/languages
   
   # Translate text
   curl -X POST http://localhost:5000/api/translate \
     -H "Content-Type: application/json" \
     -d '{"text": "thank you", "source_lang": "en", "target_lang": "fr"}'
   ```

## 🐛 Troubleshooting

### Port Already in Use?
```bash
# Check if something is running on port 5000
lsof -i :5000

# Or change the port in app.py
# Edit line 178: app.run(debug=debug_mode, host=host, port=5001)
```

### Dependencies Not Installed?
```bash
# Make sure you're in the project directory
cd /path/to/translations

# Install requirements
pip install -r requirements.txt
```

### Can't Access from Another Computer?
```bash
# Enable debug mode to bind to all interfaces
export FLASK_DEBUG=true
python app.py

# The app will be accessible at http://your-ip-address:5000
```

## 📚 Need More Info?

- **Setup Instructions:** See [README.md](README.md#installation)
- **API Documentation:** See [README.md](README.md#api-documentation)
- **Configuration:** Edit `config.py` for settings

## ✅ Verification Checklist

- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Server running (`python app.py`)
- [ ] Browser shows the translation interface at `http://localhost:5000`
- [ ] Can translate "hello" to "hola" (English to Spanish)
- [ ] API responds to curl commands

---

**Still need help?** Check the [README.md](README.md) for detailed documentation!
