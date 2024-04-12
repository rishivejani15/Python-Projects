import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = "https://www.amazon.in/Airdopes-141-Playtime-Resistance-Bluetooth/dp/B09N3ZNHTY/ref=sr_1_5?keywords=airdopes%2B141&qid=1691924784&sr=8-5&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8"
}

response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = 100
# print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
# print(title)

BUY_PRICE = 200

if price < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("15rishivejani@gmail.com", "ajyhngdbgddknwkz")
        connection.sendmail(
            from_addr="15rishivejani@gmail.com",
            to_addrs="15rishivejani@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )