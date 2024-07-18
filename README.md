# Reddit Article Poster

A Python script that scrapes articles from a specified website and automatically posts them to a Reddit subreddit.

## Features

- Scrapes articles from a specified website
- Automatically posts new articles to a specified subreddit
- Prevents duplicate postings
- Runs continuously, checking for new articles at regular intervals

## Requirements

- Python 3
- `praw` library
- `requests` library
- `beautifulsoup4` library
- `python-dotenv` library (optional, for environment variable support)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/stephenhf/reddit-article-poster.git
    cd reddit-article-poster
    ```

2. Install the required Python packages:

    ```sh
    pip install praw requests beautifulsoup4 python-dotenv
    ```

3. Set up your credentials:

    ### Using Environment Variables

    - Create a `.env` file in the project directory with the following content:

      ```sh
      REDDIT_CLIENT_ID=your_client_id
      REDDIT_CLIENT_SECRET=your_client_secret
      REDDIT_USER_AGENT=your_user_agent
      REDDIT_USERNAME=your_username
      REDDIT_PASSWORD=your_password
      TARGET_SUBREDDIT=your_target_subreddit
      ```

    ### Using a Configuration File

    - Create a `config.json` file in the project directory with the following content:

      ```json
      {
        "REDDIT_CLIENT_ID": "your_client_id",
        "REDDIT_CLIENT_SECRET": "your_client_secret",
        "REDDIT_USER_AGENT": "your_user_agent",
        "REDDIT_USERNAME": "your_username",
        "REDDIT_PASSWORD": "your_password",
        "TARGET_SUBREDDIT": "your_target_subreddit"
      }
      ```

    - Add `config.json` to `.gitignore`:

      ```sh
      echo "config.json" >> .gitignore
      ```

4. Update the `website_url` in the `post_articles.py` script to the website you want to scrape:

    ```python
    website_url = 'YOUR_WEBSITE_URL'
    ```

## Usage

Run the script:

    ```sh
    python post_articles.py
    ```

The script will continuously monitor the specified website and post new articles to Reddit as they are added. It will log its activities and errors to help you track its operation.

## Contributing

Feel free to submit issues or pull requests if you have any improvements or suggestions.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
