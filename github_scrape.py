import streamlit as sl
import requests
from bs4 import BeautifulSoup
import re


def text_converter(text_data):
    return text_data.text.strip()


def github_scrapped_data(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    # Scraping data
    github_profile_name = soup.find(
        "span", class_="p-name vcard-fullname d-block overflow-hidden"
    )
    github_profile_image = soup.find(
        "img", class_="avatar avatar-user width-full border color-bg-default"
    )["src"]
    github_profile_bio = soup.find(
        "div", class_="p-note user-profile-bio mb-3 js-user-profile-bio f4"
    )["data-bio-text"]
    href_data_follower = url + "?tab=followers"
    github_profile_followers = soup.find("a", href=href_data_follower).find(
        "span", class_="text-bold color-fg-default"
    )
    href_data_following = url + "?tab=following"
    github_profile_following = soup.find("a", href=href_data_following).find(
        "span", class_="text-bold color-fg-default"
    )
    github_profile_achievements_badges = [
        img["src"] for img in soup.find_all("img", class_="achievement-badge-sidebar")
    ]
    github_profile_contributions = soup.find("h2", class_="f4 text-normal mb-2")
    github_profile_commit_overview = soup.findAll("title")[-1].text.strip()

    # text converters
    github_profile_name = text_converter(github_profile_name)
    github_profile_followers = text_converter(github_profile_followers)
    github_profile_following = text_converter(github_profile_following)
    github_profile_contributions = re.sub(
        "[^0-9]", "", github_profile_contributions.text.strip()
    )

    profile_info = [
        github_profile_name,
        github_profile_image,
        github_profile_bio,
        github_profile_followers,
        github_profile_following,
        github_profile_achievements_badges,
        github_profile_contributions,
        github_profile_commit_overview,
    ]

    return profile_info
