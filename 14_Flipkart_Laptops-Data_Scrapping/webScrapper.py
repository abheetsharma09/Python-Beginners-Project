import requests
import time
import json
from bs4 import BeautifulSoup

products = []
for url_param in range(44 , 55):
  url = f"https://www.flipkart.com/search?q=laptop&otracker=search&otracker2=search&marketplace=FLIPKART&as-show=on&as=off&page={url_param}"
  custom_headers = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",        "Accept": "application/json",
    }
  
  siteData = requests.get(url , headers=custom_headers)
  if siteData.status_code == 200:
    try:
      with open("dataIndex.html" , "w" , encoding="UTF-8") as r:
        r.write(siteData.text)
        print("HTML Data Written sucessfull!!")

    except FileNotFoundError or OSError as err:
      print(f'ERROR!!...{err}')


    try:
      with open("dataIndex.html" , "r" , encoding="UTF-8") as s:
        html = s.read()

      soupDATA = BeautifulSoup(html, 'html.parser')

      # print(soupDATA.prettify())

    except FileNotFoundError or OSError as err:
      print(f'ERROR!!...{err}')


    image_tags = soupDATA.find_all("img", class_="UCc1lI")
    price_tags = soupDATA.find_all("div", class_="hZ3P6w DeU9vF")
    review_decimal = soupDATA.find_all("div" , class_="MKiFS6")
    total_rating = soupDATA.find_all("span" , class_="EZaE0Q")
    discount_data = soupDATA.find_all("div" , class_="HQe8jr cEBXHx")
    specification_details = soupDATA.find_all("ul" , class_="HwRTzP")

    for img_tag, price_tag , rating , int_rating , discount , s_details in zip(image_tags, price_tags, review_decimal,total_rating , discount_data ,specification_details):    
        numbers = []

        for text in int_rating.stripped_strings:
            if text != "&":
                # Split the text by spaces and take the first item (the number)
                split_text = text.split()
                number = split_text[0]
                
                # Add the isolated number to our list
                numbers.append(number)
        
        # Extract the ratings count
        if len(numbers) > 0:
            ratings_count = numbers[0].replace(",", "")
        else:
            ratings_count = "0"

        # Extract the reviews count
        if len(numbers) > 1:
            reviews_count = numbers[1].replace(",", "")
        else:
            reviews_count = "0"

        specification_list = []
        for li in s_details.find_all("li", class_="DTBslk"):
            specification_list.append(li.get_text().strip())


        product = {
            'product_name': img_tag.get('alt'),
            'product_imageSRC': img_tag.get('src'),
            'product_price_in_inr': float(price_tag.get_text().strip().replace(",", "").replace("₹" ,"")),
            'product_rating' : float(rating.get_text().strip()),
            'product_total_ratings' : int(ratings_count),
            'product_total_reviews' : int(reviews_count),
            'product_discount' :int(discount.get_text().strip().replace("% off" , "")),
            'processor' : specification_list[0],
            'ram' : specification_list[1],
            'os' :specification_list[2],
            'storage' : specification_list[3],
            'display' : specification_list[4],
            # 'software_included' : specification_list[5],
            # 'services' : specification_list[6],
        }
        
        products.append(product)
        time.sleep(3)
        print("Attempting....")
  else:
     continue

try:
  with open("exported_data.json" , "w" , encoding="UTF-8") as raw_json:
    json.dump(products, raw_json, indent=2, ensure_ascii=False)
    print("Data Written Sucessfully!!!")
except FileNotFoundError or FileExistsError as err:
  print(f'ERROR!!...{err}')
