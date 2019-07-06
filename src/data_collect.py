from template_39ask import template_39ask

import time
from selenium import webdriver
import json
import codecs
import glob
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import os
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random

def _get_page(browser, url, element_present, timeout):
	try:
		browser.get(url)
		WebDriverWait(browser, timeout).until(element_present)
	except Exception as e:
		print(e)
		browser.quit()
		time.sleep(2)
		browser = webdriver.Chrome(options=options)
		browser.get(url)
		WebDriverWait(browser, timeout).until(element_present)
	return browser

if __name__ == '__main__':
	template = template_39ask()
	options = Options()
	options.add_argument("--headless")
	options.add_argument('--ignore-certificate-errors')
	# options.add_argument('--disable-features=NetworkService')
	# options.add_argument("start-maximized") # open Browser in maximized mode
	# options.add_argument("disable-infobars") # disabling infobars
	# options.add_argument("--disable-extensions") # disabling extensions
	# options.add_argument("--disable-gpu") # applicable to windows os only
	# options.add_argument("--disable-dev-shm-usage") # overcome limited resource problems
	# options.add_argument("--no-sandbox") # Bypass OS security model
	# options.add_argument('--remote-debugging-port=922')
	loaded_flag = template.loaded_flag
	element_present = EC.presence_of_element_located((By.CLASS_NAME, loaded_flag))
	timeout = 10
	departments = template.departments
	num_urls_per_dept = 50000
	sample_rate = 0.2
	if not os.path.isfile('{}_urls_list'.format(template.template_name)):
		loaded_flag = template.url_loaded_flag
		element_present = EC.presence_of_element_located((By.CLASS_NAME, loaded_flag))
		browser = webdriver.Chrome(options=options)
		urls = []
		for dept_ind in range(len(departments)):
			dept = departments[dept_ind]
			page_ind = 1
			while True:
			# while len(urls) // (dept_ind + 1) < num_urls_per_dept:
				try:
					url = template.url_list_url.format(dept, page_ind)
					browser = _get_page(browser, url, element_present, timeout)
					urls_on_page = template.extract_urls(browser)
					if urls_on_page is None:
						break
					urls += urls_on_page
					page_ind += 1
					if page_ind > 100 and page_ind % 10 == 0 and len(urls) > 0:
						with open('{}_urls_list'.format(template.template_name), 'a') as url_out:
							url_out.write('\n')
							url_out.write('\n'.join(urls))
							urls = []
				except:
					if len(urls) > 0:
						with open('{}_urls_list'.format(template.template_name), 'a') as url_out:
							url_out.write('\n')
							url_out.write('\n'.join(urls))
							urls = []
		if len(urls) > 0:
			with open('{}_urls_list'.format(template.template_name), 'a') as url_out:
				url_out.write('\n')
				url_out.write('\n'.join(urls))
				urls = []
	loaded_flag = template.loaded_flag
	element_present = EC.presence_of_element_located((By.CLASS_NAME, loaded_flag))
	browser = webdriver.Chrome(options=options)
	urls = open('{}_urls_list'.format(template.template_name)).read().split('\n')
	del(urls[0])
	# urls = [random.sample(urls[num_urls_per_dept * i: (num_urls_per_dept + 1) * i], sample_rate * num_urls_per_dept) for i in range(len(departments))]
	json_entries = []
	batch_size = 1000
	batch_counter = 0
	for url in urls:
		browser = _get_page(browser, url, element_present, timeout)
		json_entry = template.extract_text(browser)
		json_entries.append(json_entry)
		if len(json_entries) > batch_size - 1:
			json_str = {'data': json_entries}
			out_path = '{}_1k_batch_{}.json'.format(template.template_name, batch_counter)
			with codecs.open(out_path, 'w') as f:
				json.dump(json_str, f, ensure_ascii=False)
			batch_counter += 1