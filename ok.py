# # BIO

# import requests
# from bs4 import BeautifulSoup

# url = "https://github.com/Tanay-Dwivedi"

# req = requests.get(url)
# soup = BeautifulSoup(req.text, "html.parser")

# profile_bio = soup.find(
#     "div", class_="p-note user-profile-bio mb-3 js-user-profile-bio f4"
# )["data-bio-text"]

# print(profile_bio)

# # Followers

# import requests
# from bs4 import BeautifulSoup

# url = "https://github.com/aankitasoni"

# req = requests.get(url)
# soup = BeautifulSoup(req.text, "html.parser")

# followers_count_span = soup.find(
#     "a", href="https://github.com/aankitasoni?tab=followers"
# ).find("span", class_="text-bold color-fg-default")

# if followers_count_span:
#     followers_count = followers_count_span.text.strip()
#     print(f"Followers count: {followers_count}")
# else:
#     print("Followers count not found.")


# # following

# import requests
# from bs4 import BeautifulSoup

# url = "https://github.com/aankitasoni"

# req = requests.get(url)
# soup = BeautifulSoup(req.text, "html.parser")

# following_count_span = soup.find(
#     "a", href="https://github.com/aankitasoni?tab=following"
# ).find("span", class_="text-bold color-fg-default")

# if following_count_span:
#     following_count = following_count_span.text.strip()
#     print(f"Following count: {following_count}")
# else:
#     print("Following count not found.")


# # Badges

# import requests
# from bs4 import BeautifulSoup

# url = "https://github.com/Tanay-Dwivedi"

# req = requests.get(url)
# soup = BeautifulSoup(req.text, "html.parser")

# image_links = [
#     img["src"] for img in soup.find_all("img", class_="achievement-badge-sidebar")
# ]

# for link in image_links:
#     print(link)


# # contriutions

# import requests
# from bs4 import BeautifulSoup
# import re

# url = "https://github.com/Tanay-Dwivedi"

# req = requests.get(url)
# soup = BeautifulSoup(req.text, "html.parser")

# profile_bio = soup.find("h2", class_="f4 text-normal mb-2")

# if profile_bio:
#     contributions_number = re.sub("[^0-9]", "", profile_bio.text.strip())
#     print(f"{contributions_number}")
# else:
#     print("Contributions not found.")

# # Commit graph history

# import requests
# from bs4 import BeautifulSoup

# url = "https://github.com/Tanay-Dwivedi"

# req = requests.get(url)
# soup = BeautifulSoup(req.text, "html.parser")

# profile_bio = soup.findAll("title")[-1].text.strip()

# # Remove extra spaces between words
# profile_bio = " ".join(profile_bio.split())

# print(profile_bio)


# # REPO FINDER

# import requests
# from bs4 import BeautifulSoup
# import math


# def scrape_github_repositories(username):
#     base_url = "https://github.com/"
#     repositories = []

#     # Function to get repository count
#     def get_repo_count(url):
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, "html.parser")
#         repo_count_element = soup.find("span", class_="Counter")
#         repo_count_str = repo_count_element.text.strip() if repo_count_element else "0"
#         return int(repo_count_str)

#     # Function to scrape repositories from a page
#     def scrape_page(url):
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, "html.parser")

#         repo_list = soup.find_all("li", {"itemprop": "owns"})
#         repo_info2 = soup.findAll("div", class_="f6 color-fg-muted mt-2")

#         for i, repo in enumerate(repo_list):
#             repo_name = repo.find("a", {"itemprop": "name codeRepository"})
#             repo_name = repo_name.get_text(strip=True) if repo_name else "NA"

#             repo_url_tag = repo.find("a", {"itemprop": "name codeRepository"})
#             repo_url = repo_url_tag["href"] if repo_url_tag else "NA"

#             repo_description_tag = repo.find("p", {"itemprop": "description"})
#             repo_description = (
#                 repo_description_tag.get_text(strip=True)
#                 if repo_description_tag
#                 else "NA"
#             )

#             # Extracting the time information if available
#             time_info = (
#                 repo_info2[i].find("relative-time") if i < len(repo_info2) else None
#             )
#             repo_time = time_info.text.strip() if time_info else "NA"

#             # Extracting and printing the language information
#             repo_language_tag = repo.find("span", itemprop="programmingLanguage")
#             repo_language = (
#                 repo_language_tag.text.strip() if repo_language_tag else "NA"
#             )

#             repositories.append(
#                 {
#                     "serial_number": len(repositories) + 1,
#                     "name": repo_name,
#                     "url": f"{base_url}{repo_url}",
#                     "description": repo_description,
#                     "language": repo_language,
#                     "last_updated": repo_time,
#                 }
#             )

#     # Get total repository count
#     total_repos_url = f"{base_url}{username}"
#     total_repo_count = get_repo_count(total_repos_url)

#     # Determine number of pages
#     page_count = math.ceil(total_repo_count / 30)

#     # Iterate through pages and scrape repositories
#     for page_num in range(1, page_count + 1):
#         page_url = f"{base_url}{username}?page={page_num}&tab=repositories"
#         scrape_page(page_url)

#     return repositories


# # Example usage
# github_username = "Tanay-Dwivedi"
# repos = scrape_github_repositories(github_username)

# for repo in repos:
#     print(f"Serial Number: {repo['serial_number']}")
#     print(f"Repository: {repo['name']}")
#     print(f"URL: {repo['url']}")
#     print(f"Description: {repo['description']}")
#     print(f"Language: {repo['language']}")
#     print(f"Last Updated: {repo['last_updated']}")
#     print("\n")
    
# print(type(repos[0]))
# print(type(repos))