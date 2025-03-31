import json
import requests
from pathlib import Path
from typing import Dict, Any, List
from PySide6.QtWidgets import QMessageBox
from .api_caller import ApiCaller

class GroqApiCaller(ApiCaller):
    def __init__(self):
        self.api_key = self._load_api_key()
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        
    def _load_api_key(self) -> str:
        """Load the Groq API key from the file"""
        try:
            api_key_path = Path(__file__).parent.parent.parent.parent / 'groq-api.txt'
            with open(api_key_path, 'r') as f:
                return f.read().strip()
        except Exception as e:
            QMessageBox.critical(None, "API Key Error", 
                               f"Failed to load Groq API key: {str(e)}\n"
                               "Please ensure the groq-api.txt file exists and contains a valid API key.")
            return ""
    
    def call_api(self, messages: List[Dict[str, Any]], **kwargs) -> str:
        """Make a call to the Groq API"""
        if not self.api_key:
            raise Exception("API key not found")
            
        try:
            response = requests.post(
                self.api_url,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": kwargs.get("model", "llama-3.3-70b-versatile"),
                    "messages": messages,
                    "temperature": kwargs.get("temperature", 0.7)
                }
            )
            
            if response.status_code != 200:
                error_msg = f"API Error: {response.status_code} - {response.text}"
                QMessageBox.critical(None, "API Error", error_msg)
                raise Exception(error_msg)
                
            result = response.json()
            return result['choices'][0]['message']['content'].strip()
                
        except Exception as e:
            QMessageBox.critical(None, "API Error", 
                               f"Failed to call API: {str(e)}\n"
                               "Please check your internet connection and try again.")
            raise 