import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    """Fetch HTML content from a URL."""
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_table(html):
    """Parse table data from HTML."""
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table")
    if not table:
        return []
    rows = []
    for tr in table.find_all("tr"):
        cells = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
        rows.append(cells)
    return rows
