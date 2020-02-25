import requests
from bs4 import BeautifulSoup

def menu():
    sneaker_on = True
    while sneaker_on:
        print("""
            Welcome to the Nike Shoe Scraper! Enter a proper url for a Nike shoe for this to work.
                - Type 'u' to enter a URL
                - Type 'q' to quit
            """)
        user_input = input("Your choice: ")
        if user_input == 'u':
            ask_for_url()
        elif user_input == 'q':
            sneaker_on = False
        else:
            print("Unknown command, try again.")


def ask_for_url():
    url = input("Enter a URL: ")
    shoe(url)


def go_to_url(url):
    nike_page = requests.get(url).text
    soup = BeautifulSoup(nike_page, 'html.parser')
    return soup


def get_type(url):
    html_contents = go_to_url(url)
    type = html_contents.find('div', class_ = 'css-1nwc9nx').div.div.div.h2.text
    print(f"Type of shoe: {type}")


def get_name(url):
    html_contents = go_to_url(url)
    name = html_contents.find('div', class_ = 'css-1nwc9nx').div.div.div.h1.text
    print(f"Shoe name: {name}")


def get_info(url):
    html_contents = go_to_url(url)
    info = html_contents.find('div', class_ = 'description-preview').p.text
    print(f"Shoe description: {info}")


def get_colorway(url):
    html_contents = go_to_url(url)
    colorway = html_contents.find('li', class_ = 'description-preview__color-description').text
    print(f"Colorway: {colorway}")


def get_price(url):
    html_contents = go_to_url(url)
    price = html_contents.find('div', class_ = 'css-b9fpep').text
    print(f"Price: {price}")


def shoe(url):
    get_type(url)
    get_name(url)
    get_info(url)
    get_colorway(url)
    get_price(url)


menu()