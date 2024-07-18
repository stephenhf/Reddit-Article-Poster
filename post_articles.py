import praw
import requests
from bs4 import BeautifulSoup
import logging
import time
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load credentials from environment variables
reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    user_agent=os.getenv('REDDIT_USER_AGENT'),
    username=os.getenv('REDDIT_USERNAME'),
    password=os.getenv('REDDIT_PASSWORD')
)

posted_articles_file = 'posted_articles.json'

def load_posted_articles():
    if os.path.exists(posted_articles_file):
        with open(posted_articles_file, 'r') as file:
            return set(json.load(file))
    return set()

def save_posted_articles(articles):
    with open(posted_articles_file, 'w') as file:
        json.dump(list(articles), file)

posted_articles = load_posted_articles()

def scrape_articles(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        articles = []
        for article in soup.find_all('article'):
            title = article.find('h2').get_text()
            link = article.find('a')['href']
            articles.append({'title': title, 'link': link})
            
        return articles
    except requests.RequestException as e:
        logging.error(f"Error fetching articles: {e}")
        return []

def post_to_reddit(subreddit, title, url):
    try:
        reddit.subreddit(subreddit).submit(title, url=url)
        logging.info(f"Posted to Reddit: {title}")
    except Exception as e:
        logging.error(f"Error posting to Reddit: {e}")

def main():
    website_url = 'WESBITE_URL'
    subreddit_name = os.getenv('TARGET_SUBREDDIT')
    
    while True:
        articles = scrape_articles(website_url)
        for article in articles:
            if article['link'] not in posted_articles:
                post_to_reddit(subreddit_name, article['title'], article['link'])
                posted_articles.add(article['link'])
                save_posted_articles(posted_articles)
        
        logging.info('Sleeping for 10 minutes...')
        time.sleep(600)  # Wait for 10 minutes before checking again

if __name__ == "__main__":
    main()
