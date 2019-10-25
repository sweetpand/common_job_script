from selenuim import webdriver
from selenuim.common.exceptions import NoSuchElementsException
from selenuim.webdriver.common.keys import keysimport os
import time 

URLS = [URL_g1, URL_g2, URL_g3, URL_g4, URL_l1, URL_l2, URL_l3, URL_l4] # to test all the URLS

JOB_APP = {
	"first_name": "Zhama",
	"last_name": "Ryskulova",
	"email": "***@gmail.com",
	"org": "LinkedIn",
	"resume": "CV_Zhama_Ryskulova",
	"resume_textfile":"resume_short.txt",
	"linkedin":"https://www.linkedin.com/in/ryskulova/",
	"website":" ",
	"github":"https://github.com/sweetpand",
	"twiter":" "
	"location": "Dublin, Ireland",
	"grad_month": '06',
	"grad_year": "2018",
	"university": "AUCA"

}

def imb_driver(driver):

	driver.find_element_by_id('first_name').send_keys(JOB_APP['first_name'])
	driver.find_element_by_id('last_name').send_keys(JOB_APP['last_name'])
	driver.find_element_by_id('email').send_keys(JOB_APP['email'])
	driver.find_element_by_id('phone').send_keys(JOB_APP['phone'])

	try:
		loc = driver.find_element_by_id('job_application_location')
		loc.send_keys(JOB_APP['location'])
		loc.send_keys(Keys.DOWN)
		loc.send_keys(Keys.DOWN)
		loc.send_keys(Keys.RETURN)
		time.sleep(5)
	except NoSuchElementsException:
		pass

    drive.find_element_by_css_selector("[data-source='paste']").click()
    resume_zone = driver.find_element_by_id('resume_text')
    resume_zone.click()
    with open(JOB_APP['resume_textfile']) as f:
    	lines = f.readlines()
    	for line in lines:
    		resume_zone.send_keys(line.decode('utf-8'))


	#add linkedIn

	try:
		driver.find_element_by_xpath("/label[conatains(.,'LinkedIn')]").send_keys(JOB_APP['linkedin'])
	except NoSuchElementsException:

def level(driver):
	driver.find_element_by_class_name('template-btn-submit').click()

	first_name = JOB_APP['first_name']
	last_name = JOB_APP['last_name']
	full_name = first_name + ' ' + last_name
	driver.find_element_by_name('name').send_keys(full_name)
	driver.find_element_by_name('email').send_keys(JOB_APP['email'])
	driver.find_element_by_name('phone').send_keys(JOB_APP['phone'])
	driver.find_element_by_name('org').send_keys(JOB_APP['org'])


	driver.find_element_by_name('urls[LinkedIn]').send_keys(JOB_APP['linkedin'])
	driver.find_element_by_name('url[Twitter]').send_keys(JOB_APP['twitter'])
	try:
	   driver.find_element_by_name('urls[Github]').send_keys(JOB_APP['github'])
    except NoSuchElementsException:
    	try:
    		driver.find_element_by_name('urls[Github]').send_keys(JOB_APP['github'])
		except NoSuchElementsException:
			pass
	driver.find_element_by_name('urls[Portfolio]').send_keys(JOB_APP['website'])


	try: 
		driver.find_element_by_class_name('application-university').click()
		search = driver.find_element_by_xpath("//*[@type='search']")
		search.send_keys(JOB_APP['university'])
		search.send_keys(Keys.RETURN)
	except NoSuchElementsException:
		pass

	try:
		driver.find_element_by_class_name('application-droptowm').click()
		search = driver.find_element_by_xpath("//select/option[text()='Glassdoor']").click()
	except NoSuchElementsException:
		pass

	driver.find_element_by_name('resume').send_keys(os.getcwd()+"/CV_Zhama_Ryskulova")
	driver.find_element_by_name('template-btn-submit').click()

 if __name__ == '__main__':
 	driver = webdriver.Chrome(executable_path='/User/zham_rys/chromedriver')

 	for url in URLS:
 		driver.get(url)

 		if 'greenhouse' in url:
 			greenhouse(driver)

		if 'level' in url:
			level(driver)

		time.sleep(1)
	driver.close()		
