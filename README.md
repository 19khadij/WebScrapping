# Web Scraping Using Python
This Python script demonstrates how to scrape a website, "https://codewithharry.com", using both an API and HTML web scraping with the BeautifulSoup library (bs4).

# Prerequisites
Before running the script, make sure you have the following libraries installed:

requests: To make HTTP requests and fetch the HTML content.
beautifulsoup4 (bs4): For parsing and navigating the HTML content.
You can install these libraries using pip:
pip install requests beautifulsoup4

# Usage
Clone this repository to your local machine or download the Python script.
Ensure you have Python and the required libraries installed.
Open a terminal or command prompt and navigate to the directory where the code is located.
Run the web_scraping.py script to start scraping the website.
Description
This script demonstrates the following web scraping steps:

Fetching HTML Content: It sends an HTTP GET request to the specified URL and retrieves the HTML content of the webpage.

Parsing HTML: The HTML content is parsed using BeautifulSoup, making it easier to navigate and extract data.

HTML Tree Traversal: Various methods are demonstrated for traversing the HTML tree, including finding elements by tag name, class, and extracting text.

Scraping Links: The script extracts all the anchor tags (links) from the webpage and prints them.

# Customization
You can modify the url variable to specify the URL of the website you want to scrape. 
Additionally, you can customize the code to extract specific data or elements of interest from the webpage.

# Author
Khadija
