#!/usr/bin/env python3
#
#  Martin Schobert <martin@weltregierung.de>
#


import argparse
from libnmap.parser import NmapParser, NmapParserException

def parse_scan_report(nmap_xml_files, port):

    targets = []

    for nmap_xml_file in nmap_xml_files:
        
        try:

            nmap_report = NmapParser.parse_fromfile(nmap_xml_file)
            
            for host in nmap_report.hosts:
                for service in host.services:
                    
                    if service.state == 'open':
                        if port == 'web' or port == 'www':
                            if 'https' in service.service:
                                targets.append("https://%s:%s" % (host.address, service.port))

                            elif 'http' in service.service:
                                targets.append("http://%s:%s" % (host.address, service.port))

                            if 'HTTP/' in service.servicefp:
                                targets.append("http://%s:%s" % (host.address, service.port))
                                
                        else:
                            if port == int(service.port):
                                targets.append(host.address)
                            
        except NmapParserException as e:
            print(f"File {nmap_xml_file} is not yet ready:" + str(e), file=sys.stderr)
            pass
            
    return targets

def print_targets(targets):
    for target in targets:
        print(f"{target}")
              
def main():
    # process command line arguments
    parser = argparse.ArgumentParser(description='Extract hosts from an Nmap XML file')
    parser.add_argument('--xml', nargs='+', help='Nmap XML file to parse', metavar='FILE')
    parser.add_argument('--port', help='Which port to lookup? Special port "www" or "web" matches any web related port.', metavar='PORT')
    (options, args) = parser.parse_known_args()

    if options.xml:
        
        targets = parse_scan_report(options.xml, options.port)
        print_targets(targets)
    else:
        print("+ Unknown option")
        parser.print_help()



if __name__ == "__main__":
    main()
