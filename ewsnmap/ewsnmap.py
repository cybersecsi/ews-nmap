#!/usr/bin/env python3

import fire
import traceback
from libnmap.parser import NmapParser
from os import path, makedirs

VERSION = '1.0.5'
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

        https://wwww.secsi.io - https://github.com/cybersecsi/ews-nmap - {0}
      '''.format(VERSION))

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

def process(nmap_xml_file,  output_dir = OUTPUT_DIR, txtout = 'output.txt', csvout = 'output.csv', append=False):
    """
    Extract web servers from an Nmap XML file
    """
    targets = []
    services = []

    info(f"Opening XML file {nmap_xml_file}")
    nmap_report = NmapParser.parse_fromfile(nmap_xml_file)
    for host in nmap_report.hosts:
        #if host.is_up():
        for service in host.services:
            if service.state == 'open':
                # Create the version string
                version = ""
                service_product = service.service_dict.get("product",None)
                service_version = service.service_dict.get("version",None)
                if service_product:
                    version = service_product
                if service_version:
                    version = version + " " + service_version

                if 'http' in service.service or 'HTTP/' in service.servicefp:
                    service_row = f"{host.address},{service.port},{service.protocol},{service.service},{version}"
                    services.append(service_row)
                    info(service_row)
                    scheme = 'https' if 'https' in service.service else 'http'
                    if service.port in [80, 443]:
                        target = f"{scheme}://{host.address}"
                    else:
                        target = f"{scheme}://{host.address}:{service.port}"
                    targets.append(target)
                    info(target)

    check_or_create_dir(output_dir)

    file_mode = 'a+' if append else 'w'

    with open(path.join(output_dir, txtout), file_mode, encoding='utf-8', newline='') as file:
        info(f"Store baseurls in {path.join(output_dir, txtout)}")
        for target in targets:
            file.write(f"{target}\n")
        info("TXT file correctly created!")

    with open(path.join(output_dir, csvout), file_mode, encoding='utf-8', newline='') as file:
        info(f"Store services in {path.join(output_dir, csvout)}")
        if not append:
            header = "ip,port,protocol,service,version"
            file.write(f"{header}\n")
        for service in services:
            file.write(f"{service}\n")
        info("CSV file correctly created!")

def main():
    try:
        banner()
        fire.core.Display = lambda lines, out: out.write(
            "\n".join(lines) + "\n")
        fire.Fire(process, command=None)
    except Exception as e:
        err(str(e))

if __name__ == '__main__':
    main()