# Goodreads-Quote-Scraper
A customizable Python script for scraping book quotes from Goodreads, including metadata such as tags and likes. Users can input any Goodreads book URL to extract relevant quote data, which is saved in a CSV file format for easy access and analysis.

## Features
- Scrapes quotes, tags, and likes from a specified Goodreads book page.
- Saves scraped data in a CSV file format.
- Easy to customize for different Goodreads URLs.
- Removes unwanted characters like curly quotes and extraneous symbols around the quotes.

## Requirements
- Python 3.x
- Required Python packages:
  - `requests`
  - `beautifulsoup4`

## Installation
1. Clone this repository
2. Navigate into the project directory
3. Install the required dependencies

## Usage
1. Run the scraper by providing a Goodreads book URL:

#### The Command:
```python
python scraper.py https://www.goodreads.com/work/quotes/2180358-the-little-prince
```
#### An Example:

```python
python scraper.py https://www.goodreads.com/work/quotes/2180358-the-little-prince
Fetching page 1...
Scraping page 1
Fetching page 2...
Scraping page 2
⋮
Fetching page 52...
Scraping page 52
No more quotes found, ending scrape.
Quotes saved to quotes.csv
```

2. The script will scrape the quotes from the provided URL and save them in a `quotes.csv` file.

## Known Limitations
- **Unwanted Characters for Non-English Languages**: The scraper may produce unwanted characters for books in languages other than English. These characters could include symbols or special characters specific to different languages. The resulting CSV file may require manual cleaning or additional processing to remove these unwanted characters.

- **Cleaning the CSV**: After scraping, it's recommended to review the CSV file for any extraneous characters, especially if the book is in a non-English language. You may need to perform additional data cleaning to get a clean set of quotes.

## Example Output (CSV)
The resulting CSV will include the following columns:
- **Quote**: The text of the quote.
- **Tags**: A list of tags associated with the quote.
- **Likes**: The number of likes for the quote.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Feel free to fork the repository, submit issues, and send pull requests. Contributions are welcome! :D

## Acknowledgements
Thanks to the creators of [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [Requests](https://docs.python-requests.org/en/latest/) for their excellent libraries.



