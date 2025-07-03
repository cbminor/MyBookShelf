# MyBookShelf

An application for tracking books I have read or want to read

## Overview

This project is the foundation for a React application designed to track and display books in my personal collection. While the application is still in its early stages, it will be developed incrementally over time. Currently, it includes a few backend models and a script that gathers book data from a CSV file containing ISBNs.

## Installation

The current script can be run by following the steps below:

```
# Example
git clone https://github.com/cbminor/MyBookShelf.git
cd MyBookShelf
pip install -r requirements.txt
```

## Usage

The following provides examples of how the application and included scripts can be used.

### Get Books By ISBN

The ```get_books_by_isbn``` script can be used to get the book details from the OpenLibrary API and export the results to a CSV file. The input file must contain a column with the header: "ISBN".

```
# Example usage
python get_books_by_isbn.py INPUT_FILE_PATH OUTPUT_FILE_PATH
```

## Future Improvements

This repository currently contains the initial groundwork for a Bookshelf application. Future development plans include:

* Creating a database to store and manage book information

* Building a React application to display and interact with the data