from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timedelta

class InstagramBot():

	def __init__(self):

		self.browser = webdriver.Chrome(ChromeDriverManager().install())
		self.HOME_URL = "https://www.instagram.com/"
		self.TAG_URL = "explore/tags/"
		self.CHOICE = True 
		self.HASHTAG = 1
		self.FOLLOW = 2
		self.QUIT = 0

	def run(self):

		while self.CHOICE:
			self.menuDisplay()
			if self.CHOICE == self.HASHTAG:
				self.hastag()
			elif self.CHOICE == self.FOLLOW:
				self.follow()

	def getFollowCount(self, follow_count):
		"""
		Method to convert follows abbrevation to int
		@param follow_count: Follow count in text format

		@return followers in integer format
		"""

		follow_count = follow_count.replace(',', '') if ',' in follow_count else follow_count
		follow_count = follow_count.replace('k', '000') if 'k' in follow_count else follow_count
		follow_count = follow_count.replace('m', '000000') if 'm' in follow_count else follow_count
		return int(follow_count)

	def getFollowersList(self):
		"""
		Method to get followers list
		"""

		time.sleep(5)
		is_success = False
		try:
			self.browser.find_element_by_xpath("//li/a[contains(.,'followers')]").click()
			is_success = True
		except:
			print("It is a Private Account So Can't Able To Fetch Followers")
		if is_success:
			time.sleep(5)
			last_element = True
			total_followers = self.getFollowCount(follow_count = self.browser.find_elements_by_class_name('g47SY')[1].text)
			print("Total followers: ", total_followers)
			followers_list = set()
			while last_element:
				dialog_element = self.browser.find_element_by_class_name('pbNvD')
				followers_elements = dialog_element.find_elements_by_class_name('FPmhX')
				# followers_elements = self.browser.find_elements_by_class_name('wFPL8')
				count = 0
				for e in followers_elements:
					if not e.text in followers_list:
						followers_list.add(e.text)
						webdriver.ActionChains(self.browser).move_to_element(e).perform()
					count = count + 1
				time.sleep(2)
				if count == total_followers or count > 100:
					last_element = False
				else:
					try:
						move_element = self.browser.find_elements_by_class_name('wFPL8')[count-1]
						webdriver.ActionChains(self.browser).move_to_element(move_element).perform()
					except:
						pass
					try:
						move_element = self.browser.find_elements_by_class_name('wFPL8')[count]
						webdriver.ActionChains(self.browser).move_to_element(move_element).perform()
					except:
						pass
					try:
						move_element = self.browser.find_elements_by_class_name('FPmhX')[count]
						webdriver.ActionChains(self.browser).move_to_element(move_element).perform()
					except:
						pass
			print("Follower List: ", followers_list)

	def getFollowingList(self):
		"""
		Method to get following list
		"""

		time.sleep(5)
		is_success = False
		try:
			self.browser.find_element_by_xpath("//li/a[contains(.,'following')]").click()
			is_success = True
		except:
			print("It is a Private Account So Can't Able To Fetch Following List")
		if is_success:
			time.sleep(5)
			last_element = True
			total_following = self.getFollowCount(follow_count = self.browser.find_elements_by_class_name('g47SY')[2].text)
			print("Total following: ", total_following)
			followers_list = set()
			while last_element:
				dialog_element = self.browser.find_element_by_class_name('pbNvD')
				followers_elements = dialog_element.find_elements_by_class_name('FPmhX')
				# followers_elements = self.browser.find_elements_by_class_name('wFPL8')
				count = 0
				for e in followers_elements:
					if not e.text in followers_list:
						followers_list.add(e.text)
						webdriver.ActionChains(self.browser).move_to_element(e).perform()
					count = count + 1
				time.sleep(2)
				if count == total_following or count > 100:
					last_element = False
				else:
					try:
						move_element = self.browser.find_elements_by_class_name('wFPL8')[count-1]
						webdriver.ActionChains(self.browser).move_to_element(move_element).perform()
					except:
						pass
					try:
						move_element = self.browser.find_elements_by_class_name('wFPL8')[count]
						webdriver.ActionChains(self.browser).move_to_element(move_element).perform()
					except:
						pass
					try:
						move_element = self.browser.find_elements_by_class_name('FPmhX')[count]
						webdriver.ActionChains(self.browser).move_to_element(move_element).perform()
					except:
						pass
			print("Following List: ", followers_list)

	def scrollLast(self):
		"""
		Method to scroll to the last page where has autoload functionality
		"""

		SCROLL_PAUSE_TIME = 1.5
		last_height = self.browser.execute_script("return document.body.scrollHeight")
		while True:
		    self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		    time.sleep(SCROLL_PAUSE_TIME)
		    new_height = self.browser.execute_script("return document.body.scrollHeight")
		    if new_height == last_height:
		        break
		    last_height = new_height
		time.sleep(5)

	def follow(self):
		"""
		Method to fetch followes and following
		"""

		print("Followers/Following List")
		self.follow_username = input("Account: ")
		follow_url = self.HOME_URL + self.follow_username
		self.browser.get(follow_url)
		self.getFollowersList()
		self.browser.get(follow_url)
		self.getFollowingList()
		self.browser.get(follow_url)

	def hastag(self):
		"""
		Method to fetch tagged peoples
		"""

		hashtag_value = input("Hashtag: ")
		self.browser.get(self.HOME_URL + self.TAG_URL + hashtag_value)
		# self.scrollLast()
		self.createHashTagList()

	def createHashTagList(self):
		"""
		Method to create hash tagged persons list.
		"""

		tagged_persons = []
		print("1 --> Top Post")
		print("2 --> Most Recent")
		post_choice = int(input("Select Choice: "))
		if post_choice == 1:
			selected_section = self.browser.find_element_by_xpath("/html/body/div/section/main/article/div[1]")
		else:
			selected_section = self.browser.find_element_by_xpath("/html/body/div/section/main/article/div[2]")
		hash_elements = selected_section.find_elements_by_class_name('v1Nh3')
		hash_elements[0].click()
		cnt = 0
		is_collect = True
		while (post_choice == 1 and cnt < len(hash_elements)) or (post_choice == 2 and is_collect and cnt < 30):
			time.sleep(2)
			is_find_name = True
			while is_find_name:
				try:
					hash_tag_name = self.browser.find_elements_by_class_name('sqdOP')[1].text
					tagged_persons.append(hash_tag_name)
					cnt = cnt + 1
					is_find_name = False
					is_find = True
					stop_time_stamp = datetime.now() + timedelta(0,6)
					while is_find:
						try:
							but = self.browser.find_element_by_class_name('_65Bje')
							but.click()
							is_find = False
						except:
							if stop_time_stamp < datetime.now():
								is_find = False
								is_collect = False
				except:
					pass
		print("Tagged Person List: ", tagged_persons)

	def menuDisplay(self):
		"""
		Method to display menu/choice
		"""

		print("Select The Choice")
		print(str(self.HASHTAG), " --> Hash Tag")
		print(str(self.FOLLOW), " --> Follow List")
		print("0 --> Exit")
		self.CHOICE = int(input("Enter your choice: "))



	def signIn(self):
		"""
		Method to login to the instagram
		"""

		self.browser.get('https://www.instagram.com/accounts/login/')
		self.email = input("Username: ")
		from getpass import getpass
		self.password = getpass("Password: ")
		time.sleep(5)
		emailInput = self.browser.find_element_by_name("username")
		passwordInput = self.browser.find_element_by_name("password")
		emailInput.send_keys(self.email)
		passwordInput.send_keys(self.password)
		passwordInput.send_keys(Keys.ENTER)
		self.run()

if __name__ == '__main__':

	InstagramBot().signIn()
