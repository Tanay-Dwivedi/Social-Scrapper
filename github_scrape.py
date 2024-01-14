import streamlit as sl
import requests
from bs4 import BeautifulSoup


def text_converter(text_data):
    return text_data.text.strip()


def github_scrapped_data(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    # Find profile name
    github_profile_name = soup.find(
        "span", class_="p-name vcard-fullname d-block overflow-hidden"
    )
    github_profile_image = soup.find(
        "img", class_="avatar avatar-user width-full border color-bg-default"
    )["src"]

    github_profile_name = text_converter(github_profile_name)

    profile_info = [
        github_profile_name,
        github_profile_image,
    ]

    return profile_info
