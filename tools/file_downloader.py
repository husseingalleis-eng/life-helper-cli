import re


import os,requests
def download(url, file_name):
    get_response = requests.get(url,stream=True)
    with open(file_name, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

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
    
def get_file_extension_os(url):
    _, file_extension = os.path.splitext(url)
    return file_extension
def file_downloader():
    print("\nWelcome to File Downloader\n")
    file_name = input("Enter the file name: ")
    file_url = (input("Enter the file URL here please: "))
    code = is_valid_url(clean_url(file_url))
    content_type = requests.head(file_url)
    print("Content-Type: ",content_type.headers["Content-Type"])

    if 200 <= code < 300 and content_type !='HTML':
        print("The website URL is valid Status Code: " + str(code))
        print("The URL is valid")
        print(f"Your URL is: {clean_url(file_url)}")
        download(clean_url(file_url), file_name+str(get_file_extension_os(file_url)))
        print("The file is downloaded succesfuly")

    elif 300 <= code < 404:
        while True:
            answer = input("Are you still want to download the file?  (Yes or No): ")
            if answer.lower().strip() in ('yes', 'y'):
                print("The website URL is valid Status Code: " + str(code))
                print("The URL is valid")
                print(f"Your URL is: {clean_url(file_url)}")
                download(clean_url(file_url),file_name)
                print("The file is downloaded")
                break
            elif answer.lower().strip() in ('no', 'n'):
                print("see you next time")
                break
            else:
                print("Wrong input try again")
                
    else:
        print("Error")


    
    
    
    



    

    


