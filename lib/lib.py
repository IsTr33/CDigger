# coding=utf-8

"""
Copyright (c) 2017 IsTr33
"""

import socket
import time
import urllib
import urllib2
import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

def print_obj(obj):
    print '\n'.join(['%s:%s' % item for item in obj.__dict__.items()])

def get_host(url):
    try:
        if re.search(r'(http://)|(https://)|(ftp://)|(file://)', url):
            protocol, s1 = urllib.splittype(url)
        else:
            s1 = re.sub('^/*', '//', url)
        host, s2 = urllib.splithost(s1)
        host, port = urllib.splitport(host)
    except:
        host = 'unknown host'
    return host

'''
Use Chinaz tools get the cdn ips of a domain
Function temporarily not used 
'''
def get_cdn_ips(host):
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0")
    browser = webdriver.PhantomJS(executable_path='D:\Program Files\Python27\Scripts\phantomjs.exe',desired_capabilities = dcap)
    url = 'http://ping.chinaz.com/'+host
    print url
    browser.get(url)
    time.sleep(10)
    contents = browser.find_elements_by_xpath("//div[@id='ipliststr']/a")
    for content in contents:
        if content.text:
            print content.text
    browser.quit()

def get_ip(host):
    try:
        ip = socket.gethostbyname(host)
    except:
        ip = 'Can not get IP'
    return ip

def get_domains(ip):
    url = "http://cn.bing.com/search?q=ip:" + ip + "&go=%E6%8F%90%E4%BA%A4&qs=n&first=1&form=QBRE&pq=ip:" + ip + "&sc=0-0&sp=-1&sk=&cvid=5e52385772e24683a0bdf047de60abfc"
    domains = []
    titles = []
    while True:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        soup = BeautifulSoup(response.read(), 'html.parser')
        for h2 in soup.findAll('h2'):
            link = h2.find('a')
            if link:
                if link['href']:
                    domains.append(link['href'])
                else:
                    domains.append('unknown domain')
                if link.string:
                    titles.append(link.string)
                else:
                    titles.append('unknown title')
        if soup.find(class_ = 'sw_next'):
            next_page = soup.find(class_='sb_pagN')
            url = next_page['href']
            url = "http://cn.bing.com"+url
            url = re.sub('%3a', ':' ,url)
            continue
        break
    domains = zip(domains, titles)
    if domains:
        if re.search(u'chinaz\.com', domains[0][0]):
            domains.pop(0)#drop chinaz ip search
    return domains

if __name__ == "__main__":
    print 'No permission'
    pass