import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import re
import numpy as np

lst = []
for i in range(1,11):
    url = f'https://www.meesho.com/men-clothing/pl/lb03x?page={i}'
    lst.append(url)


l_name = []
l_price = []
l_rating = []
l_review_count = []
image_list = []
l_link = []


for n in range(len(lst)):
    r = requests.get(lst[n])
    soup = bs(r.content)
    

    tag_name = soup.find_all('p', class_='Text__StyledText-sc-oo0kvp-0 cPgaBh NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 hofZGw NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 hofZGw')
    product_name = [name.get_text() for name in tag_name]
    l_name.append(product_name)

    tag_price = soup.find_all('h5', class_='Text__StyledText-sc-oo0kvp-0 dLSsNI')
    product_price = [price.get_text().replace('₹', '').strip() for price in tag_price]
    l_price.append(product_price)

    tag_rating = soup.find_all('span', class_='Text__StyledText-sc-oo0kvp-0 kPhFPP')
    product_rating = [rating.get_text() for rating in tag_rating]
    l_rating.append(product_rating[:-1])
    # product_rating[:-1]

    tag_NoOfReviews = soup.find_all('span', class_='Text__StyledText-sc-oo0kvp-0 efHMfi NewProductCard__RatingCount-sc-j0e7tu-19 fZuHRL NewProductCard__RatingCount-sc-j0e7tu-19 fZuHRL')
    product_review_count = [count.get_text().replace('Reviews', '').strip() for count in tag_NoOfReviews]
    l_review_count.append(product_review_count)
    # product_review_count

    tag_image = soup.find_all('img', class_='lazyload NewProductCard__StyledPerfImage-sc-j0e7tu-16 bHZlWX')
    for product_image in tag_image:
        image_list.append(product_image['src'])

    tag_link = soup.find_all('div', class_=['sc-dkzDqf ProductList__GridCol-sc-8lnc8o-0 kmfTGq dXXltq', 'sc-dkzDqf ProductList__GridCol-sc-8lnc8o-0 kmfTGq fPEnaj'])
    product_link = ['https://www.meesho.com'+atag.find('a')['href'] for atag in tag_link]
    l_link.append(product_link)
    


l_link=l_link[0]+l_link[1]+l_link[2]+l_link[3]+l_link[4]+l_link[5]+l_link[6]+l_link[7]+l_link[8]+l_link[9]
l_name=l_name[0]+l_name[1]+l_name[2]+l_name[3]+l_name[4]+l_name[5]+l_name[6]+l_name[7]+l_name[8]+l_name[9]
l_price=l_price[0]+l_price[1]+l_price[2]+l_price[3]+l_price[4]+l_price[5]+l_price[6]+l_price[7]+l_price[8]+l_price[9]
l_rating=l_rating[0]+l_rating[1]+l_rating[2]+l_rating[3]+l_rating[4]+l_rating[5]+l_rating[6]+l_rating[7]+l_rating[8]+l_rating[9]
l_review_count=l_review_count[0]+l_review_count[1]+l_review_count[2]+l_review_count[3]+l_review_count[4]+l_review_count[5]+l_review_count[6]+l_review_count[7]+l_review_count[8]+l_review_count[9]


Dct = {'Product Name':l_name,
   'Price':l_price,
   'Rating':l_rating,
   'Review Count':l_review_count,
   'Link':l_link,
   'Image link': image_list
  }


df = pd.DataFrame(Dct)
df.index = np.arange(1, len(df)+1)
print(df)

df.to_csv('meesho mens clothing big.csv')
