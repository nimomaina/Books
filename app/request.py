import json
import random
import requests


def get_books():
    random_books = requests.get("https://www.googleapis.com/books/v1/volumes?q=" +
                            random.choice('abcdefghijklmnopqrstuvwxzy') +
                            "&maxResults=40&key=AIzaSyBtprivgL2dXOf8kxsMHuELzvOAQn-2ZZM").json()

    return random_books


