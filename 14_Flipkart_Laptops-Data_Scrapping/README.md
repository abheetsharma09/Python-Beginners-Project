# Flipkart Laptops Data Scrapping

Welcome to this project form `python-core-to-ds` repo. I build a script that extract laptops specification, and all important details from the flipkart laptop search page.While learning Data Gathering.

## Project Requirement

Using `BeautifulSoup` for WebScrapping Work, to install use \
```pip install bs4```

## Extracting the Data
The HTML tag name can change when flipkart updates its code....so you can change the class name later to work it in a favour.
```
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
```

## Output Data
The script is extracting the data and storing it in a json file later by the use of `json_to_csv.py` i am converting it to csv this script actually helps in extracting the json content into csv without duplicating values and can intergrate multiple json files data in one.

### Data Structure
```
RangeIndex: 139 entries, 0 to 138
Data columns (total 13 columns):
 #   Column                 Non-Null Count  Dtype
---  ------                 --------------  -----
 0   Sl No                  139 non-null    int64
 1   product_name           139 non-null    str
 2   product_imageSRC       139 non-null    str
 3   product_price_in_inr   139 non-null    float64
 4   product_rating         139 non-null    float64
 5   product_total_ratings  139 non-null    int64
 6   product_total_reviews  139 non-null    int64
 7   product_discount       139 non-null    int64
 8   processor              139 non-null    str
 9   ram                    139 non-null    str
 10  os                     139 non-null    str
 11  storage                139 non-null    str
 12  display                139 non-null    str
dtypes: float64(2), int64(4), str(7)
memory usage: 14.2 KB
```

```
{
    "product_name": "Samsung Galaxy Book4 Metal Intel Core i5 13th Gen 1335U - (8 GB/512 GB SSD/Windows 11 Home) NP750XGJ-K...",
    "product_imageSRC": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/k/t/y/-enriched-transparent-original-imahg53xspmfrsdd.png?q=70",
    "product_price_in_inr": 55311.0,
    "product_rating": 4.4,
    "product_total_ratings": 19735,
    "product_total_reviews": 2048,
    "product_discount": 29,
    "processor": "Intel Core i5 Processor (13th Gen)",
    "ram": "8 GB LPDDR4X RAM",
    "os": "64 bit Windows 11 Operating System",
    "storage": "512 GB SSD",
    "display": "39.62 cm (15.6 Inch) Display"
},
```
and so on..
HAPPY Scrapping :)