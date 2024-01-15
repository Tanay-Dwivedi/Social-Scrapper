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

    # REPO FINDER -----------------------------------------------

    def scrape_github_repositories(url):
        url = url + "?tab=repositories"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            repositories = []

            # Extract repository information
            repo_list = soup.find_all("li", {"itemprop": "owns"})
            repo_info2 = soup.findAll("div", class_="f6 color-fg-muted mt-2")

            for i, repo in enumerate(repo_list):
                repo_name = repo.find("a", {"itemprop": "name codeRepository"})
                repo_name = repo_name.get_text(strip=True) if repo_name else "NA"

                repo_url_tag = repo.find("a", {"itemprop": "name codeRepository"})
                repo_url = repo_url_tag["href"] if repo_url_tag else "NA"

                repo_description_tag = repo.find("p", {"itemprop": "description"})
                repo_description = (
                    repo_description_tag.get_text(strip=True)
                    if repo_description_tag
                    else "NA"
                )

                # Extracting the time information
                time_info = repo_info2[i].find("relative-time")
                repo_time = time_info.text.strip() if time_info else "NA"

                # Extracting and printing the   language information
                repo_language_tag = repo.find("span", itemprop="programmingLanguage")
                repo_language = (
                    repo_language_tag.text.strip() if repo_language_tag else "NA"
                )

                repositories.append(
                    {
                        "name": repo_name,
                        "url": f"https://github.com {repo_url}",
                        "description": repo_description,
                        "language": repo_language,
                        "last_updated": repo_time,
                    }
                )

            return repositories

    repos = scrape_github_repositories(url)

    # --------------------------------------------------------------

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
        repos,
    ]

    return profile_info
