# coding=utf-8

"""
CDigger tool
Use Bing search engine find the domains of an IP or a C segment network
Copyright (c) 2017 IsTr33
"""
import argparse
from lib.lib import *
from lib.color_print import *
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
    print
    print '         ,_,_   _,,__      ,qs'
    print '      _40B0M0&  00M&000x   #MM'
    print '      &00^``~?  0M` ^^#0&  __    ______    _____    _,_    __ __'
    print '     j0Nf       0#     #0n ]0F  q0Q00NN  p#0MM0MH /00M0&,  #QpQ0&'
    print '     #M&        NB     M0k 4MF ]ME  K0,  N&  l05 ]M&  `0&  B&N9^'
    print '     B#&        00     00Q ]0R  0&,,R0:  B&,_QM9 #MNgmm00I K#H'
    print '     ]MN        M0    j00! [M1  #B#0B7   0MMM07  #MB^-^-^` #NH'
    print '      QM0g,_gA  MML,pN0MF  40M ]N&pg__  ]Nbpgq,  ]00___,,  K#H'
    print '       ~NMNM@D  &#RM0@S^   4Mh _M0MMMNb  B#MMMMQ  ~#0M#0&  #&0'
    print '         `                  `  QMT  _N#1#0@  _MNI    ~'
    print '                               ~NMMM0M$ ^0MMM00#'
    print '                                 ~^^~     ^~  ^'
    print '\n                                            Copyright 2017 @ IsTr33\n'

    parser = argparse.ArgumentParser(description='Find the C segment network domains.')
    parser.add_argument('-c', help='find c segment network hosts and their domains, or only current host and its domains', action='store_true')
    parser.add_argument('-u', '--url', help='set the URL(Host/IP)', type=str)
    parser.add_argument('-o', '--output', help='set output file, default ip.txt', type=str)
    args = parser.parse_args()

    if args.url:
        host = get_host(args.url)
        if host == 'unknown host':
            printRed('[!]Unknown host\n')
            sys.exit(1)
        else:
            print '[*]Host is '+host
            ip = get_ip(host)
            if ip == 'Can not get IP':
                printRed('[!]Can not get IP\n')
                sys.exit(1)
            else:
                print '[*]IP is '+ip
    else:
        printRed('[!]An available URL is needed\n')
        sys.exit(1)

    if args.output:
        try:
            fo = open(args.output, 'w')
        except:
            printRed('[!]Could not open output file ' + args.output + '\n')
            print '[*]The output file is set to ' + ip + '.txt'
            fo = open('./result/'+ip+'.txt', 'wb')
    else:
        print '[*]The output file is set to ' + ip + '.txt'
        fo = open('./result/'+ip + '.txt', 'wb')
    fo.write('CDigger result for ip ' + ip + '(host:' + host + '):\n')

    if args.c:
        count = 0
        network = re.sub('\.\d+?$', '', ip)
        fo.write('Search '+network+'.0/24 network hosts and domains\n')
        print '[*]Searching ' + network + '.0/24 network hosts and domains'
        for i in range(1,254):
            ip = network + '.' + str(i)
            domains = get_domains(ip)
            if domains:
                count = count+1
                printYellow('[+]Find domains in ip ' + ip +'\n')
                fo.write('\n\n[+]Find domains in ip ' + ip + '\n')
                for domain ,title in domains:
                    print '[*]' + title + '\n[*]' + domain
                    fo.write('\n[Title]')
                    fo.write(title.encode('utf8'))
                    fo.write('\n' + domain + '\n')
        if count ==0:
            printYellow('[*]Sorry, no result found\n')
            fo.write('Sorry, no result found\n')
    else:
        fo.write('Search ' + ip + ' host domains\n')
        print '[*]Search ' + ip + ' host domains'
        domains = get_domains(ip)
        if domains:
            printYellow('[+]Find domains in ip ' + ip + '\n')
            fo.write('\n\n[+]Find domains in ip ' + ip + '\n')
            for domain, title in domains:
                print '[*]' + title + '\n[*]' + domain
                fo.write('\n[Title]')
                fo.write(title.encode('utf8'))
                fo.write('\n'+domain+'\n')
        else:
            printYellow('[*]Sorry, no result found\n')
            fo.write('Sorry, no result found\n')
    fo.close


