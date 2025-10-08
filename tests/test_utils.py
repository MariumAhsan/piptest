from src.utils import fetch_html, parse_table

def test_parse_table():
    html = "<table><tr><th>Name</th><th>Age</th></tr><tr><td>Alice</td><td>30</td></tr></table>"
    result = parse_table(html)
    assert result == [["Name", "Age"], ["Alice", "30"]]
