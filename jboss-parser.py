#!/usr/bin/python3

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
        os.system('clear')
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
    executable_path='/home/'PATH TO'/chromedriver')  # <== set the path to chrome driver
driver.get('https://developer.jboss.org/people/')
count = 0
while True:
    try:
        count = count + 20
        time.sleep(3)
        links = driver.find_elements_by_xpath('//td[@class="j-td-user-info"]/a')
        lst.extend([i.text for i in links])
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        red = '\033[31m'
        yellow = '\033[93m'
        endcolor = '\033[0m'
        print(f'{yellow}Collected:{endcolor} {red}{count}{endcolor}')
        next_page_button = driver.find_element_by_css_selector('a.j-pagination-next')
        if next_page_button:
            next_page_button.click()
        else:
            break
    except:
        break
driver.close()
csvwriter(lst)
