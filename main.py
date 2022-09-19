import joblib
import re
import warnings
warnings.filterwarnings('ignore')
from fastapi import FastAPI

app = FastAPI()

model = joblib.load('Final_model.joblib')

def preprocessor(text):
    text = re.sub('<[^>]*>', '', text) # Effectively removes HTML markup tags
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    text = re.sub('[\W]+', ' ', text.lower()) + ' '.join(emoticons).replace('-', '') 
    return text
 
def classify_message(model, message):
    message = preprocessor(message)
    label = model.predict([message])[0]
    return {'label': label}

@app.get('/')
def get_root():
    return {'Hello': 'Welcome to the spam detection APP'}

 
@app.get('/spam_detection_path/{message}')
async def detect_spam_path(message: str):
	return classify_message(model, message)