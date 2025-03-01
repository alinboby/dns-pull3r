import dns.resolver
from termcolor import colored

def get_dns_records(domain, flag_prefix):
    record_types = [
        'A', 'AAAA', 'CNAME', 'MX', 'NS', 'TXT', 'SOA', 'SRV', 'PTR',
        'CAA', 'DNSKEY', 'DS', 'NAPTR', 'SMIMEA', 'SSHFP', 'TLSA', 'URI'
    ]
    
    print(f"\nChecking DNS records for: {domain}\n")
    
    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            for answer in answers:
                record_value = answer.to_text()
                if flag_prefix in record_value:
                    print(colored(f"[{record_type}] {record_value}", 'red'))
                else:
                    print(f"[{record_type}] {record_value}")
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout, dns.resolver.NoNameservers):
            pass  # Skip if no records found

if __name__ == "__main__":
    print("""
  _____  _   _  _____            _____       _ _ ____       
 |  __ \| \ | |/ ____|          |  __ \     | | |___ \      
 | |  | |  \| | (___    ______  | |__) |   _| | | __) |_ __ 
 | |  | | . ` |\___ \  |______| |  ___/ | | | | ||__ <| '__|
 | |__| | |\  |____) |          | |   | |_| | | |___) | |   
 |_____/|_| \_|_____/           |_|    \__,_|_|_|____/|_|   
                                                            
                                                            
    
    Author: HxN0n3
    Email: alinboby@gmail.com
    Team: bdhxgrp
    Last Updated: 01/03/2025
    """)
    
    domain = input("Enter the domain: ")
    flag_prefix = input("Enter the flag prefix to check: ")
    get_dns_records(domain, flag_prefix)
