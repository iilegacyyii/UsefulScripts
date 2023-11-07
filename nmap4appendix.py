# nmap4appendix.py
# QoL tool of which wraps nmap to generate CSV output. Useful for generating tables in word via CSV
# - @0xLegacyy (Jordan Jay)

import argparse
import csv
import ctypes
import os
import subprocess
import sys
import xml.etree.ElementTree as etree

import logger


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="nmap scans given hosts, and outputs in report-friendly CSV")
    
    # hosts either from file or cmdline
    hosts_group = parser.add_mutually_exclusive_group(required=True)
    hosts_group.add_argument("-l", "--list", help="file containing lists of hosts")
    hosts_group.add_argument("-H", "--hosts", help="specify comma-seperated hosts via command line")

    # output file
    parser.add_argument("-o", "--outfile", help="output filepath")

    # udp scan support
    parser.add_argument("-u", "--udp", action="store_true", help="Perform UDP scan (default: false)")
    return parser.parse_args()


def is_admin():
    try:
        return (os.getuid() == 0)
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0


def parse_xml_output(xml):
    root = etree.fromstring(xml)

    # parse hosts
    output = []
    for host in root.findall("host"):
        ip_address = host.find("address").attrib["addr"]
        hostname = host.find("hostnames").find("hostname").attrib["name"]
        for port in host.find("ports").findall("port"):
            # Need an entry per port
            _ = {}
            service = port.find("service")
            _["IP Address"] = ip_address
            _["Hostname"] = hostname
            _["Port"] = port.attrib["portid"]
            _["Protocol"] = service.attrib["name"]
            if _["Protocol"] == "tcpwrapped":
                _["Protocol"] = "" # unsure on protocol
            _["Service"] = service.get("product")
            if _["Service"] == None or "(unknown)" in _["Service"]:
                _["Service"] = "" # unsure on product

            output.append(_)
    return output




if __name__ == "__main__":
    # Parse commandline args
    args = parse_args()

    log = logger.Logger()
    
    # If input file specified, ensure it exists
    if args.list:
        if not os.path.isfile(args.list):
            log.error(f"Specified file '{args.list}' does not exist")
            exit()
    
    # Setup command for the nmap process
    command = ["nmap", "-sC", "-sV", "-p-", "--min-rate=1000", "-oX", "-"]
    if args.udp:
        if not is_admin():
            log.error("UDP scan requires root privileges")
            exit()
        command.append("-sU")
    if args.list:
        command.append("-iL")
        command.append(args.list)
    else:
        if "," in args.hosts:
            for host in args.hosts.split(","):
                command.append(host)
        else:
            command.append(args.hosts)
    
    # Run nmap process
    log.info(f"Executing: {' '.join(command)}")
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate() # wait until process is finished
    if len(stderr) > 0:
        log.error(stderr.decode())
    log.success("Scan complete")

    # Parse results
    log.info("Parsing results")
    csv_rows = parse_xml_output(stdout)
    log.success("Parsing complete")
    
    # Grab handle to stdout/file
    if args.outfile:
        csv_file = open(args.outfile, "w")
    else:
        csv_file = sys.stdout
    
    # Write csv file
    headers = ["IP Address", "Hostname", "Port", "Protocol", "Service"]
    writer = csv.DictWriter(csv_file, headers)
    writer.writeheader()
    writer.writerows(csv_rows)

    # Close file handle if necessary
    if args.outfile:
        csv_file.close()

    log.success("Finished!")
    