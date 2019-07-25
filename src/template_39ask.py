import json

class template_39ask:
	def __init__(self):
		self.departments = [313, 320, 321, 322, 309, 3157, 323, 319465592, 3165, 311, 3162, 3166, 3163, 27]
		self.url_list_url = 'http://ask.39.net/news/{}-{}.html'
		self.data_base_url = 'http://ask.39.net'
		self.loaded_flag = 'selected'
		self.url_loaded_flag = 'list_tag'
		self.template_name = '39ask'

	def extract_urls(self, browser):
		xpath = '//span[@class="a_l"]/p/a'
		urls = [var.get_attribute('href') for var in browser.find_elements_by_xpath(xpath)]
		if len(urls) < 1:
			return None
		return urls

	def extract_text(self, browser):
		departments_xpath = '//div[@class="sub"]/span[not(@class)]/a'
		title_xpath = '//p[@class="ask_tit"]'
		patient_infos_xpath = '//p[@class="mation"]/span'
		question_content_xpath = '//p[@class="ask_tit"]'
		question_time_xpath = '//p[@class="txt_nametime"]/span[2]'
		labels_xpath = '//p[@class="txt_label"]/span/a'
		doctor_page_links_xpath = '//div[@class="selected"]/div[contains(@class, "sele_all")]/div[@class="doctor_all"]/div[@class="doc_img"]/a'
		doctor_names_xpath = '//div[@class="selected"]/div[contains(@class, "sele_all")]/div[@class="doctor_all"]/div[@class="doc_txt"]/p[@class="doc_xinx"]/span[@class="doc_name"]'
		doctor_other_infos_xpath = '//div[@class="selected"]/div[contains(@class, "sele_all")]/div[@class="doctor_all"]/div[@class="doc_txt"]/p[@class="doc_xinx"]/span[@class="doc_yshi"]'
		doctor_specialties_xpath = '//div[@class="selected"]/div[contains(@class, "sele_all")]/div[@class="doctor_all"]/div[@class="doc_txt"]/p[@class="doc_sc"]/span'
		doctor_answers_xpath = '//div[@class="selected"]/div[contains(@class, "sele_all")]/p[@class="sele_txt"]'
		doctor_mids_xpath = '//div[@class="selected"]/div[contains(@class, "sele_all")]/div[@class="doctor_all"]'
		answer_times_xpath = '//div[@class="selected"]/div[contains(@class, "sele_all")]/div[@class="doc_t_strip"]/div[@class="zwAll"]/p[@class="doc_time"]'
		follow_up_roles_xpath = '//div[@class="selected"]/div[contains(@class, "sele_all")]/div[@class="doc_t_strip"]/div[@class="zwenall"]/div[@class="doczw"]/span[@class="zw1"]'
		follow_up_contents_xpath = '//div[@class="selected"]/div[contains(@class, "sele_all")]/div[@class="doc_t_strip"]/div[@class="zwenall"]/div[@class="doczw"]/span[@class="zw2"]'
		follow_up_mids_xpath = '//div[@class="selected"]/div[contains(@class, "sele_all")]/div[@class="doc_t_strip"]/div[@class="zwenall"]/div[@class="doczw"]/span[@class="zw1"]/parent::div[contains(@class, "sele_all")]/div[class="doctor_all"]'
		num_sele_xpath = '//p[@class="sele_img"]'

		json_entry = {}
		departments = browser.find_elements_by_xpath(departments_xpath)
		json_entry['department'] = '>'.join([var.text for var in departments])
		json_entry['title'] = browser.find_element_by_xpath(title_xpath).text
		json_entry['patient_infos'] = [var.text for var in browser.find_elements_by_xpath(patient_infos_xpath)]
		json_entry['question_content'] = browser.find_element_by_xpath(question_content_xpath).text
		json_entry['question_time'] = browser.find_element_by_xpath(question_time_xpath).text
		json_entry['labels'] = '\t'.join([var.text for var in browser.find_elements_by_xpath(labels_xpath)])
		doctor_page_links = browser.find_elements_by_xpath(doctor_page_links_xpath)
		doctor_other_infos = browser.find_elements_by_xpath(doctor_other_infos_xpath)
		doctor_specialties = browser.find_elements_by_xpath(doctor_specialties_xpath)
		doctor_answers = browser.find_elements_by_xpath(doctor_answers_xpath)
		doctor_mids = browser.find_elements_by_xpath(doctor_mids_xpath)
		answer_times = browser.find_elements_by_xpath(answer_times_xpath)
		num_sele = browser.find_elements_by_xpath(num_sele_xpath)
		num_sele = int(num_sele[0].text.split('(')[1][0]) if len(num_sele) > 0 else 0
		doctor_specialties = [var.text for var in doctor_specialties]
		doctor_specialties = doctor_specialties + [''] * (len(doctor_mids) - len(doctor_specialties))
		json_entry['answers'] = [{'mid': doctor_mids[i].get_attribute('mid'), 
								'adopted': str(i < num_sele),
								'page_link': doctor_page_links[i].get_attribute('href'),
								# 'other_info': doctor_other_infos[2 * i].text + '\t' + doctor_other_infos[2 * i + 1].text,
								# 'specialty': doctor_specialties[i],
								'answer': doctor_answers[i].text,
								'answer_time': answer_times[i].text} for i in range(len(doctor_mids))]
		follow_up_mids = browser.find_elements_by_xpath(follow_up_mids_xpath)
		follow_up_roles = browser.find_elements_by_xpath(follow_up_roles_xpath)
		follow_up_contents = browser.find_elements_by_xpath(follow_up_contents_xpath)
		follow_ups = [(follow_up_mids[i].get_attribute('mid'), follow_up_roles[i].text + ':' + follow_up_contents[i].text) for i in range(len(follow_up_mids))]
		distinct_mids = list(set([var.get_attribute('mid') for var in follow_up_mids]))
		follow_ups_grouped = []
		for mid in distinct_mids:
			content = ''
			for follow_up in follow_ups:
				if follow_up[0] == mid:
					content += (follow_up[1] + '\n')
			follow_ups_grouped.append({mid: content})
		json_entry['follow_ups'] = follow_ups_grouped
		return json_entry
