import pandas as pd
from typing import Dict
import time
import sys
from open_library_client import OpenLibraryClient
from book_details import BookDetails

class BookDataHelper():
    """ Methods to help parse and format book data """

    def get_book_list_details_by_isbn(self, in_path: str, out_path: str, library_client: OpenLibraryClient):
        """ Given a csv containing a list of ISBN numbers, creates a new csv with all the details available in the OpenLibrary """
        book_csv = pd.read_csv(in_path)
        isbn_list = book_csv["ISBN"].tolist()
        book_list = []
        for isbn in isbn_list:
            book_list.append(self.get_book_by_isbn(isbn=isbn, library_client=library_client))
            time.sleep(1)
        book_list_df = pd.DataFrame(book_list)
        book_list_df.to_csv(out_path)

    def get_book_by_isbn(self, isbn: str, library_client: OpenLibraryClient):
            """ Given an ISBN number, calls the OpenLibraryClient to gather all available information about the book, and returns a BookDetails object """
            # Get the book data
            book_data = library_client.get_book_by_isbn(isbn)
            book_info = self.parse_book_data(book_data)
            # Pull out the works_key and the author_key
            works_id = book_info.get("works_key")
            author_key = book_info.get("authors_key")
            if works_id:
                # Call the API to get the works data
                works = library_client.get_works_info(works_id=works_id)
                works_info = self.parse_works_data(works)
                book_info.update(works_info)
                # Get the ratings data
                ratings = library_client.get_ratings(works_id=works_id)
                book_info["rating"] = self.parse_ratings_data(ratings=ratings)
            else:
                # If the book does not have works data, set the relevant columns to None
                book_info["subjects"] = None
                book_info["description"] = None
                book_info["rating"] = None
            if author_key:
                # Get the information about the author
                author_data = library_client.get_author(author_id=author_key)
                book_info["author"] = self.parse_author_data(author_data)
            else: 
                # If there is no author data available, set it to None
                book_info["author"] = None

            # Use all the collected information to create the BookDescription object
            book_description = BookDetails(
                title = book_info.get("title"),
                publish_date= book_info.get("publish_date"),
                publishers = book_info.get("publishers"),
                pages = book_info.get("pages"),
                subjects=book_info.get("subjects"),
                description=book_info.get("description"),
                rating = book_info.get("rating"),
                author=book_info.get("author")
            )
            return book_description

    def parse_book_data(self, book_data) -> Dict:
        """ Takes the JSON string of book data and converts it to a BookDetails object"""
        works = book_data.get("works")
        if works:
            works = works[0].get("key")
        authors = book_data.get("authors")
        if authors:
            authors = authors[0].get("key")
        num_pages = book_data.get("number_of_pages")
        if num_pages is None:
            num_pages = book_data.get("pagination")
        return {
            "title": book_data.get("title"),
            "publish_date": book_data.get("publish_date"),
            "publishers": book_data.get("publishers"),
            "pages": num_pages,
            "works_key": works,
            "authors_key": authors
        }
    
    def parse_works_data(self, works):
        """ Parses the information in the works dictionary and returns the subjects and the subjects and description """
        description_dict = works.get("description")
        if description_dict:
            if type(description_dict) == dict:
                description = description_dict.get("value")
            else:
                print(description_dict)
                description = description_dict
        else:
            description = None
        return {
            "subjects": works.get("subjects"),
            "description": description
        }

    def parse_ratings_data(self, ratings):
        """ Parses the ratings information and returns the average ratings """
        summary = ratings.get("summary")
        if summary:
            return summary.get("average")
        else:
            return None
        
    def parse_author_data(self, authors):
        """ Parse the author information and returns the authors name """
        return authors.get("name")
