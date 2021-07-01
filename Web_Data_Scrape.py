import bs4
import requests
import shutil

print("============================================================================================================")
print("|-------------------------------------------Web-Data-Scarper-----------------------------------------------|")
print("============================================================================================================")
print("[Note] : For multi word searches use + in between word (e.g) nike shoes = nike+shoes"'\n')

data = input('Please Enter the Keyword to Search : ')
while True:
    limiter = int(input('How Many Images (No more than 100) : '))
    if limiter > 100:
        print("[Caution] : Please Select less than 100 images!")
        continue
    else:
        break

while True:
    choice = input("Start Scraper (y/n) : ")
    if choice == "y" or choice == "Y":
        GOOGLE_IMAGE = \
            'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'
        break
    elif choice == "n" or choice == "N":
        break
    else:
        print("\n Wrong input, try again", 'red')
        # time.sleep(3)
        # clrscr()
        continue


def extract(data, limiter):
    while True:
        ans = choice
        if ans == 'y':
            URL_input = GOOGLE_IMAGE + 'q=' + data
            print('Fetching from url =', URL_input)
            break
        elif ans == 'n':
            print("Ok as you wish :(")
            exit(0)

        continue

    URLdata = requests.get(URL_input)
    soup = bs4.BeautifulSoup(URLdata.text, "html.parser")
    img = soup.find_all('img')
    i = 0
    print('Please wait..')
    while i < limiter:

        for link in img:
            try:
                images = link.get('src')
                ext = images[images.rindex('.'):]
                if ext.startswith('.png'):
                    ext = '.png'
                elif ext.startswith('.jpg'):
                    ext = '.jpg'
                elif ext.startswith('.jfif'):
                    ext = '.jfif'
                elif ext.startswith('.com'):
                    ext = '.jpg'
                elif ext.startswith('.svg'):
                    ext = '.svg'
                data = requests.get(images, stream=True)
                filename = "Downloads/" + str(i) + ext
                with open(filename, 'wb') as file:
                    shutil.copyfileobj(data.raw, file)
                i += 1
                if i >= limiter:
                    break
            except:
                pass
    print('\t\t\t Download Successfull\t\t ')


def fetch_url(data, limiter):
    URL_input = GOOGLE_IMAGE + 'q=' + data
    URLdata = requests.get(URL_input)
    soup = bs4.BeautifulSoup(URLdata.text, "html.parser")

    print('Please wait..')
    # Raw format
    url_limiter = limiter + 21
    x = 0
    urls = soup.find_all('a')
    links = []
    for link in urls:
        links.append(link.get('href'))
        x += 1
        if x > url_limiter:
            break

    # Finding the specific urls
    matches = []
    for match in links:
        if "https" in match:
            matches.append(match)
    result = ['https://www.google.com' + direction for direction in matches]

    # Writing to file
    file = open("urls/"+data+".txt", "w+")
    print(*result[0::2], sep='\n', file=file)
    file.close()
    print("\t\t\t Done - Check urls/"+data+".txt")

extract(data, limiter)
fetch_url(data, limiter)

#Credits : @UmerMehmood_

