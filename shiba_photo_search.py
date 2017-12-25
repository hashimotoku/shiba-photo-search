import random
import requests

FLICKR_URL = 'https://api.flickr.com/services/rest/'

payload = {
    'method':'flickr.photos.search',
    'api_key':'e73d77d132d8daaf71fc613cbbbe841e',
    'text':'shiba dog',
    'format':'json',
    'nojsoncallback':'1',
}

PHOTO_URL_FORMAT = 'https://farm{farmid}.staticflickr.com/{serverid}/{id}_{secret}.jpg'

response = requests.get(FLICKR_URL, params=payload).json()
photo = random.choice(response['photos']['photo'])
photo_url = PHOTO_URL_FORMAT.format(farmid=photo['farm'], serverid=photo['server'], id=photo['id'], secret=photo['secret'])
print(photo_url)
