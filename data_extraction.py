# Importing necessary libraries
from bs4 import BeautifulSoup
import requests

# Function to extract links from dawn.com
def extract_dawn_links():
    url = "https://www.dawn.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [link.get('href') for link in soup.find_all('a')]
    return links

# Function to extract titles from dawn.com
def extract_dawn_titles():
    url = "https://www.dawn.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = [title.text for title in soup.find_all('h2')]
    return titles

# Function to extract descriptions from dawn.com
def extract_dawn_descriptions():
    url = "https://www.dawn.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    descriptions = [desc.text for desc in soup.find_all('p')]
    return descriptions

# Function to extract links from bbc.com
def extract_bbc_links():
    url = "https://www.bbc.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [link.get('href') for link in soup.find_all('a')]
    return links

# Function to extract titles from bbc.com
def extract_bbc_titles():
    url = "https://www.bbc.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = [title.text for title in soup.find_all('h3')]
    return titles

# Function to extract descriptions from bbc.com
def extract_bbc_descriptions():
    url = "https://www.bbc.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    descriptions = [desc.text for desc in soup.find_all('p')]
    return descriptions

# Example usage
dawn_links = extract_dawn_links()
dawn_titles = extract_dawn_titles()
dawn_descriptions = extract_dawn_descriptions()

bbc_links = extract_bbc_links()
bbc_titles = extract_bbc_titles()
bbc_descriptions = extract_bbc_descriptions()

print("Dawn Links:", dawn_links)
print("Dawn Titles:", dawn_titles)
print("Dawn Descriptions:", dawn_descriptions)

print("BBC Links:", bbc_links)
print("BBC Titles:", bbc_titles)
print("BBC Descriptions:", bbc_descriptions)
