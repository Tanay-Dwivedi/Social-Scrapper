import streamlit as sl
from time import time
from github_scrape import github_scrapped_data
from instagram_scrape import instagram_scrapped_data
from linkedin_scrape import linkedin_scrapped_data
from youtube_scrape import youtube_scrapped_data


sl.markdown(
    """
<h1 style='text-align:center'>Social Scrapper</h1>
""",
    unsafe_allow_html=True,
)
sl.markdown("---")

social_media = sl.selectbox(
    "Social Media Platform", options=["Linkedin", "Instagram", "GitHub", "YouTube"]
)

with sl.form("Form 1", clear_on_submit=True):
    username = sl.text_input("Enter the username")
    submit_button = sl.form_submit_button("Scrape")

sl.write("## Scrapped Data")


def get_data(username):
    if social_media == "Linkedin":
        return linkedin_scrapped_data(link_converter(username))
    elif social_media == "GitHub":
        return github_scrapped_data(link_converter(username))
    elif social_media == "Instagram":
        return instagram_scrapped_data(link_converter(username))
    else:
        return youtube_scrapped_data(link_converter(username))


def link_converter(username):
    if social_media == "Linkedin":
        return "https://www.linkedin.com/in/" + username + "/"
    elif social_media == "GitHub":
        return "https://github.com/" + username
    elif social_media == "Instagram":
        return "https://www.instagram.com/" + username + "/"
    else:
        return "https://www.youtube.com/" + username + "/"


def github_data_onclick():
    scraped_data = get_data(username)
    if scraped_data[0] == "Data not available" or scraped_data == "":
        sl.error("### Account data not available")
    else:
        sl.write("##")
        if scraped_data[0] == "":
            sl.warning("Name not available")
        else:
            sl.write(f"### Name: {scraped_data[0]}")
        sl.write("##")
        sl.image(scraped_data[1], width=300, caption=f"{username}'s Image")
        sl.write("##")
        if scraped_data[2] == "":
            sl.warning("Bio not available")
        else:
            sl.write("### Bio: ")
            sl.write(f"{scraped_data[2]}")
        sl.write("##")
        try:
            sl.write(f"### Followers: {scraped_data[3]}")
        except:
            sl.warning("### Followers not available")
        try:
            sl.write(f"### Following: {scraped_data[4]}")
        except:
            sl.warning("### Followings not available")
        sl.write("##")
        sl.write(f"### {username}'s contribution badges: ")
        try:
            badges_row = sl.columns(len(scraped_data[5]))
            for index, link in enumerate(scraped_data[5]):
                badges_row[index].image(link, width=100)
        except:
            sl.warning("Badges not available")
        sl.write("##")
        sl.write(f"### Total public commits: {scraped_data[6]}")
        sl.write("##")
        sl.write("### Commit overview: ")
        sl.write(f"{scraped_data[7][21:]}")
        sl.write("##")
        for repo in scraped_data[8]:
            heading = str(repo["serial_number"]) + "- " + repo["name"]
            with sl.expander(heading):
                sl.markdown("""Link - [Link to project](repo["url"])""")
                if repo["description"] == "Data not available":
                    sl.warning("Description of the project is not available")
                else:
                    sl.write("Description: " + repo["description"])
                if repo["language"] == "Data not available":
                    sl.warning("Programming Language of the project is not available")
                else:
                    sl.write("Description: " + repo["language"])
                sl.write("Last updated on: " + repo["last_updated"])


def scrap_time():
    end = time()
    time_taken = format((end - start), ".2f")
    time_taken = "Scraped in " + str(time_taken) + " seconds"
    sl.success(time_taken)


if submit_button:
    if social_media == "GitHub":
        start = time()
        github_data_onclick()
        scrap_time()
    elif social_media == "Instagram":
        start = time()
        sl.write(get_data(username))
        scrap_time()
    elif social_media == "Linkedin":
        start = time()
        sl.write(get_data(username))
        scrap_time()
    else:
        start = time()
        sl.write(get_data(username))
        scrap_time()
