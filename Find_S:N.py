from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv



driver = webdriver.Chrome()

#Change url to company Oomnitza 
driver.get("URL-to-Oomnitza")


def write_csv():
	serial_numbs = navigate()
	with open('serial_numbs_test.csv', 'w' ,newline='') as csvfile:
	    serial_numb_csv = csv.writer(csvfile, delimiter=',', quotechar='|')
	    for index in range(len(serial_numbs)):
    		tmp_str = ""
    		for strings in serial_numbs[index]:
    			tmp_str += strings + "            "

    		serial_numb_csv.writerow([tmp_str])
    
	csvfile.close()
    	






def get_users():
	user_list = []
	with open('Term Email List - Sheet1 copy.csv', 'r' ,newline='') as csvfile:
	    user_csv = csv.reader(csvfile, delimiter=',', quotechar='|')
	    for row in user_csv:
	    	row = row[0].split("@")
	    	user_list += [row[0]]


	    	
	    print(user_list)	
	
	csvfile.close()
	return user_list

#Input your own login credentials
def login():
	okta_butt = driver.find_element(By.CLASS_NAME, "ssoLink")	
	okta_butt.click()


	time.sleep(2)

	
	user = driver.find_element(By.ID, "input28")
	user.send_keys("")#input your own user

	pass_word = driver.find_element(By.ID, "input36")
	pass_word.send_keys("") #input your own pass

	time.sleep(2)


	sighn_in_butt = driver.find_element(By.XPATH, "//input[@value='Sign in']").click() 


	time.sleep(5)



def navigate():

	serialNumb_arr = [] #I.e: [[Serial number - Status, Serial number - Status], [Serial number - Status, Serial number - Status]]
	len_check = 0
	cell = 0

	list_of_users = get_users()

	time.sleep(2)

	Asset_page = driver.find_element(By.LINK_TEXT, 'Assets').click()
	time.sleep(2)


	search_bar = driver.find_element(By.XPATH, "//input[@placeholder= 'Search' ] ")

	for user_email in list_of_users: 

		print(f"{len_check} of {len(list_of_users)} checked")
		len_check += 1

		search_bar.send_keys(Keys.CONTROL , "a")
		for index in range(50):
			search_bar.send_keys(Keys.BACK_SPACE)

		search_bar.send_keys(user_email)

		time.sleep(2)
		Serial_numb_objs = driver.find_elements(By.CLASS_NAME, "listcontrol-column" )
		
		print(f"\nUser : {user_email}")


		#obj[2], is the serial number
		#obj[3], is the status

		serial_numbs = Serial_numb_objs[2].text.split('\n')
		status = Serial_numb_objs[3].text.split('\n')

		serialNumb_arr.append([])
	
		for index in range(len(serial_numbs)):
			tmp = ''
			if index > 0:
				tmp += serial_numbs[index]
				tmp += ' - ' + status[index]
				
				serialNumb_arr[cell] += [tmp]

		print(serialNumb_arr)
		cell+= 1

	return serialNumb_arr

			




login()
write_csv()


driver.quit()
driver.close() 

