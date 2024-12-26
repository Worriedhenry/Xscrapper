sername_field = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.NAME, "text"))
        # )
        # username_field.send_keys("herapheri512")  # Replace with your username
        # next_button = driver.find_element(By.XPATH, '//button[contains(., "Next")]')
        # next_button.click()
        # time.sleep(3)

        # password_field = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.NAME, "password"))
        # )
        # password_field.send_keys("Pass@1234")  # Replace with your password
        # login_button = driver.find_element(By.XPATH, '//button[@data-testid="LoginForm_Login_Button"]')
        # login_button.click()

        # # time.sleep(10)
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='primaryColumn']"))
        # )

        # show_more_link = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, '//a[@href="/explore/tabs/for-you"]')
        #     )
        # )
        # show_more_link.click()

        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "#")]'))
        # )

        # # Step 7: Scrape the trending hashtags
        # trends_elements = driver.find_elements(By.XPATH, '//span[contains(text(), "#")]')
        # trends = [element.text for element in trends_elements[:5] if element.text.strip()]

        # # Print out the trending hashtags
        # print("Trending Hashtags: ", trends)

        # return {
        #     "trends": trends,
        #     "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        # }