#!/usr/bin/env python3
#
#  Martin Schobert <martin@weltregierung.de>
#


import argparse
from libnmap.parser import NmapParser

def parse_scan_report(nmap_xml_file):

    targets = []

    nmap_report = NmapParser.parse_fromfile(nmap_xml_file)
    for host in nmap_report.hosts:
        #if host.is_up():
        for service in host.services:
            if service.state == 'open':
                # and service.port in ports:
                #targets.append([host.address, ports[service.port]])
                #print(service.servicefp)

                if 'https' in service.service:
                    print("https://%s:%s" % (host.address, service.port))

                elif 'http' in service.service:
                    print("http://%s:%s" % (host.address, service.port))

                if 'HTTP/' in service.servicefp:
                    print("http://%s:%s" % (host.address, service.port))
                    
    return targets


def main():
    # process command line arguments
    parser = argparse.ArgumentParser(description='Extract web servers from an Nmap XML file')
    parser.add_argument('--xml', help='Nmap XML file to parse', metavar='FILE')
    (options, args) = parser.parse_known_args()

    if options.xml:
        
        parse_scan_report(options.xml)
    else:
        print("+ Unknown option")
        parser.print_help()



if __name__ == "__main__":
    main()
