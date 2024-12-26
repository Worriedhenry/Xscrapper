# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import requests

# # ProxyMesh credentials
# hostname = 'us-ca.proxymesh.com'  # Replace with your ProxyMesh proxy URL
# port = 31280  # Replace with your ProxyMesh port
# username = 'blah'  # Replace with your ProxyMesh username
# password = '1234'  # Replace with your ProxyMesh password

# proxy_url = f'http://{username}:{password}@{hostname}:{port}'

# # def get_current_ip():
    
# #     try:
# #         # Set up proxy for HTTP requests
# #         proxies = {
# #             "http": proxy_url,
# #             "https": proxy_url,  # Although only HTTP, the same proxy can be set for HTTPS to be safe.
# #         }
        
# #         # Make a request to httpbin using the proxy URL for both HTTP and HTTPS
# #         response = requests.get("https://httpbin.org/ip", proxies=proxies, timeout=10)
        
# #         # Parse and print the proxy IP
# #         if response.status_code == 200:
# #             ip = response.json().get("origin")
# #             print(f"Current Proxy IP Address: {ip}")
# #             return ip
# #         else:
# #             print(f"Failed to get IP. Status code: {response.status_code}")
# #     except requests.exceptions.RequestException as e:
# #         print(f"Error fetching IP: {e}")
        

# def scrape_google():
#     # Set up Chrome options
#     options = webdriver.ChromeOptions()

#     # Set up Proxy
    
#     options.add_argument('--proxy-server=http://%s:%s@%s:%s' % (username, password, hostname, port))
    
#     # Optional: Run in headless mode (for no UI)
#     # options.add_argument("--headless")

#     # Optional: Disable GPU and enable other flags to make it more stable
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("--disable-gpu")

#     # Initialize the WebDriver with ProxyMesh settings
#     driver = webdriver.Chrome(options=options)
#     # 223.178.209.80
#     try:
#         # Step 1: Navigate to Google
#         driver.get("https://x.com/i/flow/login")
#         time.sleep(3)  # Wait for the page to load
#         # ip=get_current_ip()
#         username_field = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.NAME, "text"))
#         )
#         username_field.send_keys("herapheri512")  # Replace with your username
#         next_button = driver.find_element(By.XPATH, '//button[contains(., "Next")]')
#         next_button.click()
#         time.sleep(3)

#         password_field = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.NAME, "password"))
#         )
#         password_field.send_keys("Pass@1234")  # Replace with your password
#         login_button = driver.find_element(By.XPATH, '//button[@data-testid="LoginForm_Login_Button"]')
#         login_button.click()

#         # time.sleep(10)
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='primaryColumn']"))
#         )

#         show_more_link = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located(
#                 (By.XPATH, '//a[@href="/explore/tabs/for-you"]')
#             )
#         )
#         show_more_link.click()

#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "#")]'))
#         )

#         # Step 7: Scrape the trending hashtags
#         trends_elements = driver.find_elements(By.XPATH, '//span[contains(text(), "#")]')
#         trends = [element.text for element in trends_elements[:5] if element.text.strip()]

#         # Print out the trending hashtags
#         print("Trending Hashtags: ", trends)

#         return {
#             "nameoftrend1": trends[0],
#             "nameoftrend2": trends[1],
#             "nameoftrend3": trends[2],
#             "nameoftrend4": trends[3],
#             "nameoftrend5": trends[4],
#             'ip': ip,
#             "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
#         }

        

#     except Exception as e:
#         print(f"Error: {e}")
#     finally:
#         driver.quit()

# # Test the script
# if __name__ == "__main__":
#     scrape_google()

import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
# ProxyMesh credentials
hostname = 'us-ca.proxymesh.com'  # Replace with your ProxyMesh proxy URL
port = 31280  # Replace with your ProxyMesh port
username = 'blah'  # Replace with your ProxyMesh username
password = '1234'  # Replace with your ProxyMesh password
proxy_url = f'http://{username}:{password}@{hostname}:{port}'
def get_current_ip():
    
    try:
        # Set up proxy for HTTP requests
        proxies = {
            "http": proxy_url,
            "https": proxy_url,  # Although only HTTP, the same proxy can be set for HTTPS to be safe.
        }
        
        # Make a request to httpbin using the proxy URL for both HTTP and HTTPS
        response = requests.get("https://httpbin.org/ip", proxies=proxies, timeout=10)
        
        # Parse and print the proxy IP
        if response.status_code == 200:
            ip = response.json().get("origin")
            # print(f"Current Proxy IP Address: {ip}")
            return ip
        else:
            print(f"Failed to get IP. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching IP: {e}")
        

def scrape_google():
    # Set up Chrome options
    options = webdriver.ChromeOptions()

    # Set up Proxy
    # proxy = f'{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}'
    # options.add_argument('--proxy-server=http://%s:%s@%s:%s' % (username, password, hostname, port))
    
    # Optional: Run in headless mode (for no UI)
    options.add_argument("--headless")

    # Optional: Disable GPU and enable other flags to make it more stable
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    # Initialize the WebDriver with ProxyMesh settings
    driver = webdriver.Chrome(options=options)

    try:
        # Step 1: Navigate to Google
        driver.get("https://x.com/i/flow/login")
        time.sleep(3)  # Wait for the page to load
        ip =get_current_ip()
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
        username_field.send_keys("herapheri512")  # Replace with your username
        next_button = driver.find_element(By.XPATH, '//button[contains(., "Next")]')
        next_button.click()
        # time.sleep()

        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_field.send_keys("Pass@1234")  # Replace with your password
        login_button = driver.find_element(By.XPATH, '//button[@data-testid="LoginForm_Login_Button"]')
        login_button.click()

        # time.sleep(10)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='primaryColumn']"))
        )

        show_more_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//a[@href="/explore/tabs/for-you"]')
            )
        )
        show_more_link.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "#")]'))
        )

        # Step 7: Scrape the trending hashtags
        trends_elements = driver.find_elements(By.XPATH, '//span[contains(text(), "#")]')
        trends = [element.text for element in trends_elements[:5] if element.text.strip()]

        # Print out the trending hashtags
        # print("Trending Hashtags: ", trends)

        return {
            "nameoftrend1": trends[0],
            "nameoftrend2": trends[1],
            "nameoftrend3": trends[2],
            "nameoftrend4": trends[3],
            "nameoftrend5": trends[4],
            'ip': ip,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        }

        

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

# Test the script
if __name__ == "__main__":
    result=scrape_google()
    print(json.dumps(result))