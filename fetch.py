from bs4 import BeautifulSoup
import requests
import pprint
import json 
try: 
	from urllib.parse import urlparse, urljoin
except ImportError:
	from urlparse import urlparse, urljoin

pp = pprint.PrettyPrinter(indent=4)

URL = 'https://boards.greenhouse.io/braintree/jobs/1316736?gh_jid=1316736&gh_src=1d1244401'
s = requests.Session()

JOB_APP = {
	"first_name" : "Hatshi",
	"last_name":"Bar",
	"email":"@gmail.com",
	"phone":"+000000000",
	"resume":"CV_Zhama_Ryskulova",
	"linkedin": "",
	"website": "www.jam.kz",
	"github":"https://github.com/sweetpand/"

}

def fetch(url, data=None):
	if data is None:
		return s.get(url).contect
	else:
		return s.post(url, data=data).content


def greenhouse(empty_form):
	print(empty_form.keys())
	for key in empty_form.keys():
		try:
			key.encode('utf8')
			print(key)
		except:
			print('fail')
	app = empty_form.job_application
	pp.pprint(app)
	pass


def lever():
	pass


if __name__ == '__main__':
	soup = BeautifulSoup(fetch(URL), 'html.parser')
	form = soup.find('form')
	soup_fields = form.findAll('input')
	fields = soup.findAll('div', {'class': 'field'})

	form_fields = {}
	for field in fields:
		print ("\n\n FIELD", field)
		if (field.input):
			print("INPUT", field.input, filed.input['id'])
			form_fields[field.label.contents[0]] = field.input.id


	print("\n\n RES", form_fields)

	empty_form = dict( (field.get('id'), field.get('value')) for field in soup_fields)
    print("\n\n EMPTY", empty_form)


    if "greehouse" in URL:
       comlete_form = greenhouse(form)

   posturl = urljoin(URL, form['action'])


   r = s.post(posturl, data=complete_form)
   