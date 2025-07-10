import json

def crawl_all():
    data = [
        {"shop": "IAMSHOP", "title": "WELLDER SUMMER SALE", "url": "https://www.iamshop-online.com"},
        {"shop": "8DIVISION", "title": "최대 30% 시즌오프", "url": "https://www.8division.com"}
    ]
    with open("sale_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    crawl_all()
