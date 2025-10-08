from utils import fetch_html, parse_table
import pandas as pd

def main():
    url = "https://example.com"
    html = fetch_html(url)
    data = parse_table(html)

    df = pd.DataFrame(data)
    print(df.head())

if __name__ == "__main__":
    main()
