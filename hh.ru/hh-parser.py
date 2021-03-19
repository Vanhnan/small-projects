import os
from selenium import webdriver
import time,csv

path = os.getcwd()
browser = webdriver.Firefox(path)


#параметры поиска
JOB = 'менеджер' #юрист, программист и т.д.

url='https://hh.ru/search/resume?text=%s&st=resumeSearch&logic=normal&pos=full_text&exp_period=all_time&exp_company_size=any&exp_industry=any&area=1&relocation=living_or_relocation&salary_from=&salary_to=&currency_code=RUR&label=only_with_salary&education=none&age_from=&age_to=&label=only_with_photo&gender=unknown&order_by=publication_time&search_period=30&items_on_page=100'%(JOB)
browser.get (url)
time.sleep (3)


def write_csv(data):
    with open('hh.csv','a',encoding='utf8') as f:
        writer=csv.writer(f)
        writer.writerow((data['name'],
                         data['age'],
                         data['salary'],
                         data['stag'],
                         #data['post_job_place'],
                         data['resume_link'],
                         data['photo_big']
                         #data['job_places'],
                         #data['education'],
                         #data['address'],
                         #data['update']
                         ))

def resume_get():
    #сбор резюме
    a=browser.find_elements_by_class_name('resume-search-item__content-wrapper') #резюме 100 штук
    #len(a)
    #resume-search-item__description-content - стаж работы
    for i in a:
        b=i.find_element_by_class_name('resume-search-item__header')
        try:
            name=b.find_element_by_class_name('resume-search-item__name').text # Юрисконсульт
        except:
            name=''
        try:
            age=b.find_element_by_class_name('resume-search-item__fullname').text # 52 года
        except:
            age=''
        try:
            salary=b.find_element_by_class_name('resume-search-item__compensation').text # 40000 руб.
        except:
            salary=''
        try:
            stag=i.find_elements_by_class_name('resume-search-item__description-content')[0].text # '7 лет и 8 месяцев'
        except:
            stag=''
        try:
            resume_link=i.find_element_by_class_name('resume-search-item__name').get_attribute('href') #ссылка на резюме
        except:
            resume_link=''
        #post_job_place=i.find_elements_by_class_name('resume-search-item__description-content')[1].text #послед. место работы
        #job_places=b.find_elements_by_class_name('resume-search-item__description-content')[1:3] #где работал
        #education=i.find_elements_by_class_name('resume-search-item__description-content')[-1].text #где учился
        #photo_small=browser.find_element_by_class_name('resume-userpic').find_element_by_class_name('resume-userpic__photo').get_attribute('src') #ссылка на фото маленькое
        try:
            photo_big=i.find_element_by_class_name('bloko-modal-content').find_element_by_tag_name('img').get_attribute('src') #ссылка на фото-крупно
        except:
            photo_big=''


        #update=i.find_element_by_class_name('output__addition').text #дата обновления резюме
        data={    'name':name,
                  'age':age,
                  'salary':salary,
                  'stag':stag,
                  #'post_job_place':post_job_place,
                  'resume_link':resume_link,
                  'photo_big':photo_big
                  #'job_places':job_places,
                  #'education':education,
                  #'address':address,
                  #'update':update
                  }
        #print(data)
        write_csv(data)

resume_get()
x=0


while x!=51:
    browser.get (url+'&page='+str(x+1))
    time.sleep(7)
    resume_get()
    x+=1
