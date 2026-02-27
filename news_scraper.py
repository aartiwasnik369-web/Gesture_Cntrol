import requests
from bs4 import BeautifulSoup

# Website URL (example: BBC News)
URL = "https://www.bbc.com/news"

def fetch_headlines():
    try:
        response = requests.get(URL)
        response.raise_for_status()  # Check for errors
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find all h2 tags
        headlines = soup.find_all("h2")
        
        return [headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)]
    
    except requests.exceptions.RequestException as e:
        print("Error fetching website:", e)
        return []


def save_headlines(headlines):
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for index, headline in enumerate(headlines, start=1):
            file.write(f"{index}. {headline}\n")


def main():
    print("Fetching headlines...")
    headlines = fetch_headlines()
    
    if headlines:
        save_headlines(headlines)
        print("Headlines saved successfully in headlines.txt")
    else:
        print("No headlines found.")


if __name__ == "__main__":
    main()