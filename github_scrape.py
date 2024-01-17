import requests
from bs4 import BeautifulSoup
import re
import math


def text_converter(text_data):
    return text_data.text.strip() if text_data else "Data not available"


def scrape_github_repositories(username):
    base_url = "https://github.com/"
    repositories = []

    def get_repo_count(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            repo_count_element = soup.find("span", class_="Counter")
            repo_count_str = (
                repo_count_element.text.strip() if repo_count_element else "0"
            )
            return int(repo_count_str)
        except requests.exceptions.RequestException as e:
            print(f"Error getting repository count: {e}")
            return 0

    def scrape_page(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            repo_list = soup.find_all("li", {"itemprop": "owns"})
            repo_info2 = soup.findAll("div", class_="f6 color-fg-muted mt-2")

            for i, repo in enumerate(repo_list):
                repo_name = repo.find("a", {"itemprop": "name codeRepository"})
                repo_name = (
                    repo_name.get_text(strip=True)
                    if repo_name
                    else "Data not available"
                )

                repo_url_tag = repo.find("a", {"itemprop": "name codeRepository"})
                repo_url = (
                    repo_url_tag["href"] if repo_url_tag else "Data not available"
                )

                repo_description_tag = repo.find("p", {"itemprop": "description"})
                repo_description = (
                    repo_description_tag.get_text(strip=True)
                    if repo_description_tag
                    else "Data not available"
                )

                time_info = (
                    repo_info2[i].find("relative-time") if i < len(repo_info2) else None
                )
                repo_time = (
                    time_info.text.strip() if time_info else "Data not available"
                )

                repo_language_tag = repo.find("span", itemprop="programmingLanguage")
                repo_language = (
                    repo_language_tag.text.strip()
                    if repo_language_tag
                    else "Data not available"
                )

                repositories.append(
                    {
                        "serial_number": len(repositories) + 1,
                        "name": repo_name,
                        "url": f"{base_url}{repo_url}",
                        "description": repo_description,
                        "language": repo_language,
                        "last_updated": repo_time,
                    }
                )
        except requests.exceptions.RequestException as e:
            print(f"Error scraping page: {e}")

    try:
        total_repos_url = f"{base_url}{username}"
        total_repo_count = get_repo_count(total_repos_url)

        page_count = math.ceil(total_repo_count / 30)

        for page_num in range(1, page_count + 1):
            page_url = f"{base_url}{username}?page={page_num}&tab=repositories"
            scrape_page(page_url)

        return repositories
    except Exception as e:
        print(f"Error in scraping GitHub repositories: {e}")
        return []


def github_scrapped_data(url):
    try:
        req = requests.get(url)
        req.raise_for_status()
        soup = BeautifulSoup(req.text, "html.parser")

        usn = url[19:]

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
            img["src"]
            for img in soup.find_all("img", class_="achievement-badge-sidebar")
        ]
        github_profile_contributions = soup.find("h2", class_="f4 text-normal mb-2")
        github_profile_commit_overview = soup.findAll("title")[-1].text.strip()

        repos = scrape_github_repositories(usn)

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
    except requests.exceptions.RequestException as e:
        print(f"Error in fetching GitHub profile data: {e}")
        return ["Data not available"] * 9


# Example usage:
url = "https://github.com/exampleuser"
data = github_scrapped_data(url)
print(data)
