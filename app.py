from flask import Flask, render_template, request, jsonify
import joblib
import logging
import re

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the model and vectorizer
try:
    model = joblib.load('model/lr/LogisticRegression.pkl')
    vectorizer = joblib.load('model/lr/tfidf_vectorizer.pkl')
    logger.info("Model and vectorizer loaded successfully")
except Exception as e:
    logger.error(f"Error loading model: {e}")
    model = None
    vectorizer = None

def clean_text(text):
    """Clean and preprocess the input text."""
    # Convert to lowercase
    text = text.lower()
    
    # Remove digits
    text = re.sub(r'\d+', '', text)
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

@app.route('/')
def index():
    """Render the landing page."""
    return render_template('index.html')

@app.route('/features')
def features():
    """Render the features page."""
    return render_template('features.html')

@app.route('/how-it-works')
def how_it_works():
    """Render the how it works page."""
    return render_template('how-it-works.html')

@app.route('/detect', methods=['GET', 'POST'])
def detect():
    """Handle the detection page."""
    prediction = None
    text = ""
    
    if request.method == 'POST':
        text = request.form.get('text', '')
        
        if text and model and vectorizer:
            # Clean the text
            cleaned_text = clean_text(text)
            
            # Vectorize the text
            text_features = vectorizer.transform([cleaned_text])
            
            # Make prediction
            prediction = model.predict(text_features)[0]
            logger.info(f"Prediction made: {prediction}")
        else:
            logger.warning("Text input is empty or model not loaded")
    
    return render_template('detect.html', prediction=prediction, text=text)

@app.route('/testimonials', methods=['GET'])
def testimonials():
    return render_template('testimonials.html')

@app.route('/use-cases', methods=['GET'])
def use_cases():
    return render_template('use-cases.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Here you would typically handle the form submission
        # For now, we'll just return a success message
        return render_template('contact.html', message="Thank you for your message. We'll get back to you soon!")
    return render_template('contact.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)