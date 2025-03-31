from abc import ABC, abstractmethod
from typing import List, Dict, Any

class ApiCaller(ABC):
    """Interface for API callers that generate text responses"""
    @abstractmethod
    def call_api(self, messages: List[Dict[str, Any]], **kwargs) -> str:
        """
        Call the API with messages and optional parameters
        Returns the generated text response
        """
        pass 