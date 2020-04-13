from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep 
import os

class InstaBot:
    def __init__(self, username, pwd):
        self.username = username;
        if not pwd: 
            print('No password available');
            return;
        self.driver = webdriver.Chrome("c:\\rajan\devtools\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://instagram.com")
        sleep(1)
        
        u_input = self.driver.find_element_by_name('username').send_keys(username)
        p_input = self.driver.find_element_by_name('password').send_keys(pwd)

        self.driver.find_element_by_xpath('//button[@type="submit"]').click();
        sleep(4);
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now' )]").click();
        sleep(2);
    
    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username)).click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        following = self._get_names()
        print("Following: ", following)
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)
    
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

my_bot = InstaBot( 'rajanpupa',  os.getenv('INSTA_PASSWORD') );
my_bot.get_unfollowers();

