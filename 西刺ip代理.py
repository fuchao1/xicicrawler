# -*- coding:utf8 -*-
"""
如无必要。勿增实体！
"""

import requests
from bs4 import BeautifulSoup

class xici(object):
    def __init__(self,headers,url):
        self.__headers = headers
        self.__url = url
    def getip(self):
        header = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            'Hosts': 'www.xicidaili.com',
        }
        headers = self.__headers.copy()
        headers.update(header)
        proxies = {"http":"http://122.193.14.102:80"}
        response = requests.get(self.__url, headers=headers,timeout=5,proxies=proxies)
        soup = BeautifulSoup(response.text, 'lxml')
        morepage = soup.find('a',class_='next_page').string
        homepagelist = []
        for proxyip in soup.find_all('tr', class_='odd'):
            proxyiplist = []
            for ip in proxyip.find_all('td'):
                proxyiplist.append(ip.string)
            del proxyiplist[0]
            homepagelist.append(proxyiplist)
        return homepagelist,morepage


def xicihomepage():
    '''
    西刺免费代理IP 首页
    '''
    url = 'http://www.xicidaili.com/'
    headers = {
        'Referer': 'http://www.xicidaili.com/'
    }



def xicidomestic():
    '''
    西刺免费代理IP 国内高匿代理
    '''
    headers = {
        'Referer': 'http://www.xicidaili.com/nt'
    }
    num = 1
    while num:
        url = 'http://www.xicidaili.com/nt/%s' % num
        print url
        morepage = xici(headers,url).getip()[1]
        if morepage == u'下一页 ›':
            num += 1
            print xici(headers, url).getip()[0]
        else:
            num = 0
            return xici(headers, url).getip()[0]




def xiciGeneralagent():
    '''
    西刺免费代理IP 国内普通代理
    '''
    url = 'http://www.xicidaili.com/nn'
    headers = {
        'Referer': 'http://www.xicidaili.com/nn'
    }
    num = 1
    while num:
        url = 'http://www.xicidaili.com/nn/%s' % num
        print url
        morepage = xici(headers,url).getip()[1]
        if morepage == u'下一页 ›':
            num += 1
            print xici(headers, url).getip()[0]
        else:
            num = 0
            return xici(headers, url).getip()[0]

def xicihttpsproxy():
    '''
    西刺免费代理IP 国内普通代理
    '''
    url = 'http://www.xicidaili.com/wn'
    headers = {
        'Referer': 'http://www.xicidaili.com/wn'
    }
    num = 1
    while num:
        url = 'http://www.xicidaili.com/wn/%s' % num
        print url
        morepage = xici(headers,url).getip()[1]
        if morepage == u'下一页 ›':
            num += 1
            print xici(headers, url).getip()[0]
        else:
            num = 0
            return xici(headers, url).getip()[0]

def xicihttpproxy():
    '''
    西刺免费代理IP 国内普通代理
    '''
    url = 'http://www.xicidaili.com/wt'
    headers = {
        'Referer': 'http://www.xicidaili.com/wt'
    }
    num = 1
    while num:
        url = 'http://www.xicidaili.com/wt/%s' % num
        print url
        morepage = xici(headers,url).getip()[1]
        if morepage == u'下一页 ›':
            num += 1
            print xici(headers, url).getip()[0]
        else:
            num = 0
            return xici(headers, url).getip()[0]

if __name__ == '__main__':
    xicidomestic()