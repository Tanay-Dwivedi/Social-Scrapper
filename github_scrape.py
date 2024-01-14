import streamlit as sl
import requests
from bs4 import BeautifulSoup


def github_scrapped_data(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    github_profile_name = soup.find(
        "span", class_="p-name vcard-fullname d-block overflow-hidden"
    )

    if github_profile_name:
        return github_profile_name.text.strip()
    else:
        return "Profile name not found on GitHub"
