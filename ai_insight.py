import google.generativeai as genai
import PIL.Image
import os
from dotenv import load_dotenv

class AIInsights:
    def __init__(self):
        load_dotenv() 
        self.api_key = os.getenv("GOOGLEAI_API_KEY")
        if not self.api_key:
            raise ValueError("API key not found. Please set GOOGLEAI_API_KEY in your .env file.")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name = "gemini-2.0-flash")
        
    def generate_insights(self, image_path, stock, market):
        image = PIL.Image.open(image_path)
        prompt = f"This is an image of stock performance of stock : '{stock}' for the last 100 days on market : '{market}', on the basis of volume traded, closing prices and 7,20 day moving averages provide some analysis and suggestion abot this stock. This Stock should be purchased or not."
        response = self.model.generate_content([prompt,image])
        return response