# crtsh_query.py
# A QoL script to query crt.sh and get unique domain names
# - @0xLegacyy (Jordan Jay)
import argparse
import requests


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Script to query crt.sh and pull unique domain names")
    parser.add_argument("query", help="query for crt.sh (e.g. google.com)")
    return parser.parse_args()



if __name__ == "__main__":
    # Ensure args are parsed properly
    args = parse_args()
    if len(args.query) == 0:
        print("[!] query cannot be empty")
        exit(0)
        
    # Perform query
    print("[*] Querying crt.sh")
    response = requests.get(f"https://crt.sh/?Identity={args.query}&match=ILIKE&deduplicate=Y").text

    # Parse results
    print("[*] Parsing results")
    response = response.split("<TH>Matching Identities</TH>")[1].split("</TABLE>")[0]
    rows = response.split("<TR>")[1:]

    domains = list()
    for row in rows:
        for line in row.split("<TD>"):
            if "style=" in line:
                continue
            _ = line.split("</TD>")[0]
            if "<BR>" in _:
                [domains.append(domain) for domain in _.split("<BR>")]
            else:
                domains.append(_)
    domains = list(dict.fromkeys(domains))
    domains.sort()

    # Print results in user-friendly format
    print(f"[+] {len(domains)} domains found!")
    for domain in domains:
        print(domain)