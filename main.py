# work with urls
import requests 
# extract only specific information from the source code
import selectorlib 


url = "http://programmer100.pythonanywhere.com/tours/"

def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text
    return(source)

if __name__ == "__main__":
    print(scrape(url))

