import feedparser
import webbrowser

rss_url = input("Enter the RSS feed URL: ")

feed = feedparser.parse(rss_url)

article_links = feed.entries

for index, entry in enumerate(article_links):
    title = entry.title
    link = entry.link
    published = entry.published
    formatted_title = f"\033[1;32m{title}\033[0m"
    print(f"{index + 1}. {formatted_title}")
    print(f"   Published: {published}")
    print(f"   Link: {link}")
    print("-" * 50)

while True:
        article_number = int(input("Enter the number of the item you want to open: "))
        if 1 <= article_number <= len(article_links):
            webbrowser.open(article_links[article_number - 1].link)
        else:
            print(f"Invalid Input.  Please enter the number of an article between 1 and {len(article_links)} ")
