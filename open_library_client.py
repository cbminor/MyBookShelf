import requests
from book_details import BookDetails
from typing import Dict

class OpenLibraryClient:
    """ A Client for accessing the Open Library API. Requires an appname and Email to ensure the calls are not blocked (see documentation: https://openlibrary.org/developers/api)"""

    def __init__(self, app_name: str, email: str):
        """ Initialize the Open Library API class """
        self.base_url = "https://openlibrary.org"
        self.app_name = app_name
        self.email = email

    def _get_headers(self):
        return {
            "User-Agent": f"{self.app_name} ({self.email})"
        }

    
    def get_works_info(self, works_id: str) -> Dict:
        """ Add the information from the Works data to the book_info Dict """
        url = f"{self.base_url}{works_id}.json"
        response = requests.get(url, headers=self._get_headers())

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")

    def get_ratings(self, works_id: str) -> int:
        """ Get the average ratings for the works """
        url = f"{self.base_url}{works_id}/ratings.json"
        response = requests.get(url, headers=self._get_headers())

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")
    
    def get_author(self, author_id: str) -> int:
        """ Get the average ratings for the works """
        url = f"{self.base_url}{author_id}.json"
        response = requests.get(url, headers=self._get_headers())

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")
        
    def get_book_by_isbn(self, isbn: str) -> BookDetails:
        """ Return s the book details for book with the given ISBN """
        url = f"{self.base_url}/isbn/{isbn}.json"
        response = requests.get(url, headers=self._get_headers())

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")