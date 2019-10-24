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
		
