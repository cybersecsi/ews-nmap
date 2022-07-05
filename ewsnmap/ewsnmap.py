#!/usr/bin/env python3

import fire
import traceback
from libnmap.parser import NmapParser
from os import path, makedirs

VERSION = '1.0.2'
OUTPUT_DIR = 'ewsnmap-output'

def banner():
  print(
      '''
        ███████╗███████╗ ██████╗███████╗██╗
        ██╔════╝██╔════╝██╔════╝██╔════╝██║
        ███████╗█████╗  ██║     ███████╗██║
        ╚════██║██╔══╝  ██║     ╚════██║██║
        ███████║███████╗╚██████╗███████║██║
        ╚══════╝╚══════╝ ╚═════╝╚══════╝╚═╝

        https://wwww.secsi.io - https://github.com/cybersecsi/ews-nmap
      ''')  

def info(msg):
    print("[+] {}".format(msg))

def err(msg):
    traceback.print_exc()
    print("[-] ERR:{}".format(msg))

def check_or_create_dir(dir_path):
    exists = path.exists(dir_path)

    if not exists:
        # Create a new directory because it does not exist 
        makedirs(dir_path)
        info(f"Directory {dir_path} created")

def process(nmap_xml_file,  output_dir = OUTPUT_DIR, output = 'output.txt', append=False):
    """
    Extract web servers from an Nmap XML file
    """
    targets = []

    info(f"Opening XML file {nmap_xml_file}")
    nmap_report = NmapParser.parse_fromfile(nmap_xml_file)
    for host in nmap_report.hosts:
        #if host.is_up():
        for service in host.services:
            if service.state == 'open':
                if 'https' in service.service:
                    targets.append("https://%s:%s" % (host.address, service.port))
                    info("https://%s:%s" % (host.address, service.port))

                elif 'http' in service.service:
                    targets.append("http://%s:%s" % (host.address, service.port))
                    info("http://%s:%s" % (host.address, service.port))

                if 'HTTP/' in service.servicefp:
                    targets.append("http://%s:%s" % (host.address, service.port))
                    info("http://%s:%s" % (host.address, service.port))

    check_or_create_dir(output_dir)

    file_mode = 'a+' if append else 'w'

    with open(path.join(output_dir, output), file_mode, encoding='utf-8', newline='') as file:
        info(f"Store evidences in {path.join(output_dir, output)}")
        for target in targets:
            file.write(f"{target}\n")
        info("File correctly created!")

def main():
    try:
        banner()
        fire.Fire(process)
    except Exception as e:
        err(str(e))

if __name__ == '__main__':
    main()