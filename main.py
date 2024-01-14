import streamlit as sl
from github_scrape import github_scrapped_data
from instagram_scrape import instagram_scrapped_data
from linkedin_scrape import linkedin_scrapped_data
from youtube_scrape import youtube_scrapped_data


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
        return "https://github.com/" + username + "/"
    elif social_media == "Instagram":
        return "https://www.instagram.com/" + username + "/"
    else:
        return "https://www.youtube.com/" + username + "/"


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

sl.subheader("Scrapped Data")

if submit_button:
    scraped_data = get_data(username)
    sl.write(f"Name: {scraped_data[0]}")
    sl.image(scraped_data[1], width=300, caption="Profile Image")
