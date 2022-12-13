``extract_hosts_from_nmap.py`` is a python script for generating a list of web URLs from an Nmap XML file.

Purpose
==================

Network penetration testing usually starts with a portscan of available hosts and services and almost always you will find all kinds of web servers and web applications. While it is easy find all web servers on standard ports, Nmap does not always detect web services, when they are on non-standard ports while Nmap may even have enough information to derive this.

This python script scrapes information from Nmap XML files together in order to identify web server ports and renders a list of URIs.

::
   
   $ ./extract_hosts_from_nmap.py --xml 2018-05-23_fullrange_*.xml --port www
   https://aaa.bbb.ccc.ddd:8443
   http://aaa.bbb.ccc.ddd:8080
   http://aaa.bbb.ccc.ddd:10000
   http://aaa.bbb.ccc.ddd:12000
   [...]

::
   
   $ ./extract_hosts_from_nmap.py --xml 2018-05-23_fullrange_*.xml --port 445
   192.168.23.42
   192.168.23.23
   192.168.23.5   
   [...]
   
When you have a list of URLs, you may want to open them in a browser or lauch a screen shot tool, for example:

::
   
   ./extract_hosts_from_nmap.py --xml nmap_*tcp.xml --port web | xargs -n 25 -P 1 firefox


Copyright and Licence
=====================

The tool is developed by Martin Schobert martin@schobert.cc and
published under a BSD licence with a non-military clause. Please read
``LICENSE.txt`` for further details.
