
import re
import requests

def clean_url(url):
    url = url.strip()

    # remove spaces inside
    url = re.sub(r'\s+', '', url)

    # remove duplicated protocol (httphttps:// etc)
    url = re.sub(r'^(https?:\/\/)+', '', url)

    # remove leading www.
    url = re.sub(r'^www\.', '', url)

    # remove trailing slashes
    url = re.sub(r'\/+$', '', url)

    # add https:// if missing
    url = re.sub(r'^(?!https?:\/\/)', 'https://', url)

    return url


def is_valid_url(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code < 400
    except requests.RequestException:
        return False

def url_cleaner_validator():
    print("\nWelcome to URL Cleaner & Validator \n") 
    url = (input("Enter the URL here please: "))
    if is_valid_url(clean_url(url)):
        print("The URL is valid")
    else:
        print("The URL is invalid")


    print(f"Your URL is: {clean_url(url)}")


