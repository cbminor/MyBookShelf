"""
This script takes the path to a csv file with a column labeled 'ISBN' and returns a 
csv file containing book details for each of the ISBN numbers 
"""

import argparse
from open_library_client import OpenLibraryClient
from book_data_helper import BookDataHelper
from open_library_client import OpenLibraryClient

parser = argparse.ArgumentParser(
    prog="Get Book By ISBN",
    description="Returns information about the provided books given ISBN numbers"
)

parser.add_argument("input", help="Path to a CSV file containing ISBN values. The file should contain an 'ISBN' column.")
parser.add_argument("output", help="The name of the result file")

args = parser.parse_args()

APP_NAME = None
EMAIL_ADDRESS = None

if APP_NAME is None:
    APP_NAME = input("Please provide the name of your application: ")
if EMAIL_ADDRESS is None:
    EMAIL_ADDRESS = input("Please enter your email address: ")

open_library_client = OpenLibraryClient(app_name=APP_NAME, email=EMAIL_ADDRESS)
book_data_helper = BookDataHelper()
book_data_helper.get_book_list_details_by_isbn(in_path=args.input, out_path=args.output, library_client=open_library_client)
