# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from bs4 import BeautifulSoup
# import json
# import pandas as pd

# def main():
#     url = "https://ws.duelbits.com/games/crash/history"
#     html_source = fetch_and_display_html(url)

#     json_data = extract_json_from_html(html_source)
    
#     if json_data:
#         process_and_save_to_csv(json_data, "data.csv")

   
#     return json_data[0]

# def fetch_and_display_html(url):
#     try:
#         options = Options()
#         options.headless = True
#         browser = webdriver.Firefox(options=options)
#         browser.get(url)

#         browser.implicitly_wait(10)
#         html_source = browser.page_source

#         return html_source

#     except Exception as e:
#         print(f"Error: {str(e)}")
#     finally:
#         browser.quit()

# def extract_json_from_html(html_source):
#     soup = BeautifulSoup(html_source, 'html.parser')
#     json_div = soup.find('div', {'id': 'json'})
#     if json_div:
#         json_data = json.loads(json_div.text)
#         return json_data.get("history", [])
#     else:
#         print("Error: Unable to find div with id='json'")
#         return []

# def process_and_save_to_csv(json_data, filename):
#     if json_data:
#         df = pd.DataFrame(json_data)
#         df.to_csv(filename, index=False)
        
#         print(f"Data saved to {filename}")
#     else:
#         print("Error: No JSON data to process and save")

# if __name__ == "__main__":
#     x = main()
#     print(x)


from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
import json
import pandas as pd

def main():
    url = "https://ws.duelbits.com/games/crash/history"
    html_source = fetch_and_display_html(url)

    json_data = extract_json_from_html(html_source)
    
    if json_data:
        process_and_save_to_csv(json_data, "data.csv")

    return json_data[0]

def fetch_and_display_html(url):
    try:
        options = Options()
        options.headless = True
        service = Service(GeckoDriverManager().install())  # Use GeckoDriverManager to get the path dynamically
        browser = webdriver.Firefox(service=service, options=options)
        browser.get(url)

        browser.implicitly_wait(10)
        html_source = browser.page_source

        return html_source

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        if browser:
            browser.quit()

def extract_json_from_html(html_source):
    soup = BeautifulSoup(html_source, 'html.parser')
    json_div = soup.find('div', {'id': 'json'})
    if json_div:
        json_data = json.loads(json_div.text)
        return json_data.get("history", [])
    else:
        print("Error: Unable to find div with id='json'")
        return []

def process_and_save_to_csv(json_data, filename):
    if json_data:
        df = pd.DataFrame(json_data)
        df.to_csv(filename, index=False)
        
        print(f"Data saved to {filename}")
    else:
        print("Error: No JSON data to process and save")


