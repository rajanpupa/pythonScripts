from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep 


class InstaBot:
    base_url = "https://instagram.com/"
    long_sleep = 4
    short_sleep = 2
    chrome_driver_location = "c:\\rajan\devtools\chromedriver.exe"

    # opens and logins to instagram page
    def __init__(self, username, pwd):
        self.username = username;
        if not pwd: 
            print('No password available');
            return;
        self.driver = webdriver.Chrome( self.chrome_driver_location )
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        sleep(1)
        
        u_input = self.driver.find_element_by_name('username').send_keys(username)
        p_input = self.driver.find_element_by_name('password').send_keys(pwd)

        self.driver.find_element_by_xpath('//button[@type="submit"]').click();
        sleep(4);
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now' )]").click();
        sleep(2);
    
    # finds the usernames which are not following but being followed by cur user
    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        following = self._get_names()
        print("Following: ", following)
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)
    
    # find followers of the current profile page user
    def find_followers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self._get_names()
        return followers;
    
    # find followees current profile page user
    def find_followees(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        following = self._get_names()
        return following;
    
    # navigate to the profile page of user
    def navigate_profile_page(self, username):
        self.driver.get( self.base_url + username )
        sleep(2)

    # scroll the popup window (followers, following)
    def _scroll(self):
        view_div = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
        size = -1
        lst = []
        while size < len(lst):
            lst = view_div.find_elements_by_tag_name("li")
            size = len(lst)
            # print(" -- Scrolling to: ", lst[size-1].text)
            self.driver.execute_script('arguments[0].scrollIntoView()', lst[size-1])
            sleep(2)
            lst = view_div.find_elements_by_tag_name("li")
        print("Total people: ", len(lst))

    # get names from the popup window
    def _get_names(self):
        sleep(2)
        # scroll the popup window
        self._scroll();
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
        return names
