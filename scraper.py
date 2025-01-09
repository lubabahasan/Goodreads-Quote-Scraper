import requests
from bs4 import BeautifulSoup, NavigableString
import csv
import html
import re
import argparse

def quotes_by_book(page_num=1, output_file="quotes.csv", book_url=None):
    if not book_url:
        print("No book URL provided. Exiting.")
        return

    all_quotes = []

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    while True:  # Continue until no quotes are found
        try:
            page = requests.get(f"{book_url}?page={page_num}", headers=headers)
            print(f"Fetching page {page_num}...")
            soup = BeautifulSoup(page.text, 'html.parser')
            print(f"Scraping page {page_num}")
        except Exception as e:
            print(f"Could not connect to Goodreads: {e}")
            break

        # Check if the page contains the quote section
        quote_section = soup.find(class_="leftContainer")
        if not quote_section:
            print("No more quotes found, ending scrape.")
            break

        quote_list = quote_section.find_all(class_="quoteDetails")
        if not quote_list:
            print("No more quotes found, ending scrape.")
            break

        # Process quotes from this page
        for quote in quote_list:
            meta_data = []

            # Get quote's text
            try:
                outer = quote.find(class_="quoteText")
                inner_text = [element for element in outer if isinstance(element, NavigableString)]
                inner_text = [x.strip() for x in inner_text if x.strip()]  # Remove empty strings
                final_quote = " ".join(inner_text)  # Join into one string

                # Remove unwanted characters like curly quotes and surrounding spaces
                final_quote = final_quote.replace("“", "").replace("”", "").replace("‘", "").replace("’", "").strip()

                # Decode HTML entities (e.g., &ldquo; to “, &rdquo; to ”)
                final_quote = html.unescape(final_quote)

                # Use regex to remove unwanted characters
                final_quote = re.sub(r'[â€œâ€•â€™\u201c\u201d]', '', final_quote)

                # Additionally clean up any residual characters that might remain from encoding
                final_quote = re.sub(r'[^\x00-\x7F]+', '', final_quote)  # Remove non-ASCII characters

                meta_data.append(final_quote)
            except Exception as e:
                print("Error extracting quote text:", e)
                meta_data.append(None)

            # Get quote's tags
            try:
                tags_section = quote.find(class_="greyText smallText left")
                if tags_section:
                    tags = tags_section.text
                    tags = [x.strip() for x in tags.split(',') if x.strip()]
                    meta_data.append(tags)
                else:
                    meta_data.append([])  # No tags found, append empty list
            except Exception as e:
                print("Error extracting tags:", e)
                meta_data.append([])  # Append empty list if error occurs

            # Get number of likes
            try:
                likes = quote.find(class_="right").text.replace("likes", "").strip()
                likes = int(likes)
                meta_data.append(likes)
            except Exception as e:
                print("Error extracting likes:", e)
                meta_data.append(None)

            all_quotes.append(meta_data)

        # Go to the next page
        page_num += 1

    if all_quotes:
        # Save the quotes to a CSV file
        with open(output_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            # Write header without the 'Book Title' column
            writer.writerow(["Quote", "Tags", "Likes"])
            # Write rows
            writer.writerows(all_quotes)

        print(f"Quotes saved to {output_file}")
    else:
        print("No quotes were scraped.")

if __name__ == "__main__":
    # Set up argument parser to accept URL as input
    parser = argparse.ArgumentParser(description="Scrape quotes from a Goodreads book URL")
    parser.add_argument("book_url", help="The Goodreads URL of the book to scrape quotes from")
    parser.add_argument("-o", "--output", default="quotes.csv", help="Output CSV file (default: quotes.csv)")

    args = parser.parse_args()

    # Run the scraper with the provided URL
    quotes_by_book(book_url=args.book_url, output_file=args.output)
