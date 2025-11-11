import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_news(url):
    response = requests.get(url)

    if response.status_code != 200:
        print("خطا در اتصال به سایت")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # پیدا کردن همه تیترهای خبر (سایت نمونه)
    titles = soup.find_all("h2")

    news_list = []
    for t in titles:
        text = t.get_text(strip=True)
        if text:
            news_list.append(text)

    if not news_list:
        print("هیچ خبری پیدا نشد")
        return

    df = pd.DataFrame({"عنوان خبر": news_list})
    df.to_csv("news.csv", index=False, encoding="utf-8-sig")

    print("✅ استخراج شد! فایل news.csv ساخته شد.")


# اجرای برنامه
if __name__ == "__main__":
    URL = "https://www.example.com"
    scrape_news(URL)
