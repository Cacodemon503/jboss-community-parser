from selenium import webdriver
import time
import csv
import sys
import os


def csvwriter(lst):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    print('File will be saved at:', base_path)
    p_choice = input('Set the path manualy? [y/n]: ').lower().strip(' ')

    if p_choice == 'y':
        file_path = input('Set the path: ').strip(' ')
    elif p_choice == 'n':
        file_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    else:
        csvwriter(lst)

    file_name = input('\nEnter file name: ')
    with open(f'{file_path}/{file_name}.txt', 'w', encoding='utf-8') as filename:
        os.system('cls')
        writer = None
        for i in lst:
            stdout = {'Username': i,
                      'Profile link': 'https://developer.jboss.org/people/' + i}
            if not writer:
                writer = csv.DictWriter(filename, delimiter=';', fieldnames=stdout.keys())
            writer.writerow(stdout)

    print('File saved at:', os.path.realpath(filename.name))

# -------------------- MAIN PROGRAM ---------------------- #


lst = []
driver = webdriver.Chrome(
    executable_path='C:\\Users\\Mi\\Desktop\\chromedriver_win32\\chromedriver')
driver.get('https://developer.jboss.org/people/')
while True:
    time.sleep(3)
    links = driver.find_elements_by_xpath('//td[@class="j-td-user-info"]/a')
    lst.extend([i.text for i in links])
    next_page_button = driver.find_element_by_css_selector('a.j-pagination-next')
    if next_page_button:
        next_page_button.click()
    else:
        break
driver.close()
csvwriter(lst)
