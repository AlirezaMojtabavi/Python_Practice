import requests
import re
from bs4 import BeautifulSoup

getURL = requests.get("https://maktabkhooneh.org/learn/?q=%D9%85%DA%A9%D8%AA%D8%A8+%D9%BE%D9%84%D8%A7%D8%B3/")
soup = BeautifulSoup(getURL.text,'html.parser')
allMaktabClass = soup.find_all('a')

for maktabClass in allMaktabClass:

    controlText = re.search(r'.*مکتب‌خونه.*',maktabClass.text)
    if controlText != None:
        firstModified = re.sub(r'\s+' ,' ',maktabClass.text).strip()
        secondModified = re.sub(r'مکتب‌پلاس','',firstModified)
        print(secondModified)

## I can't use attributes in this case , due to :
## maktabClass.attrs = {'class': ['course-card__wrapper'], 'href': '/course/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D9%85%DB%8C%DA%A9%D8%B1%D9%88%DA%A9%D9%86%D8%AA%D8%B1%D9%84%D8%B1-AVR-mk395/', 'data-course-id': '395'}
## and in "class': ['course-card__wrapper']" I can't point to "مکتب‌خونه"
## then I utilize another trick and it's working