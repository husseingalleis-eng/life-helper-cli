
import re
import requests
import webbrowser
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
        return response.status_code 
    except requests.RequestException:
        return False

def website_status_checker():
    print("\nWelcome to Website Status Checker \n") 
    url = (input("Enter the website URL here please: "))
    code = is_valid_url(clean_url(url))
    if code < 404:
        print("The website URL is valid Status Code: " + str(code))
    else:
        print("The website URL is invalid")

    
    print(f"Your URL is: {clean_url(url)}")
    
    while True:
        open_web = input("\nDo you want to open the website: ")
        open_web = open_web.lower().strip()
        if open_web in ('yes', 'y'):
            if code:
                webbrowser.open(clean_url(url))
            else:
                print("The website url is wrong!")
            break
        elif open_web in ('no', 'n'):
            print("see you next time")
            break
        else:
            print("Wrong input try again")
    
