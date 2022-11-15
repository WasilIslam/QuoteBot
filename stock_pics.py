#api for stock pics
import requests
import shutil
AUTHORIZATION_TOKEN="563492ad6f91700001000001e726da8faa804f8dae8aeda48fabea27"

def create_img(query):

    response=requests.get("https://api.pexels.com/v1/search?query={}&per_page=1".format(query),headers={"Authorization":AUTHORIZATION_TOKEN})

    photo_id=response.json()["photos"][0]["id"]
    print(photo_id);
    response = requests.get("https://api.pexels.com/v1/photos/"+str(photo_id),headers={"Authorization":AUTHORIZATION_TOKEN})
    response=response.json()
    print(response["src"]["original"])
    response = requests.get(response["src"]["original"])
    if response.status_code == 200:
        with open("./results/image.jpeg", 'wb') as f:
            f.write(response.content)




create_img("s")

