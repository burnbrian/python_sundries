# SANS Certificate Checker

Pass the script either a comma separated list of names or a file with a first/last name combination on each line. Manually gather or scrape names from Slack. May be helpful in stacking your next SANS class CTF team.

## Description

This Python script performs SANS certification checks for individuals. Here's a concise breakdown:

- Argument Parsing: Utilizes the argparse module to handle command-line arguments. Accepts either a file (-f) with one name per line or a comma-separated list of names (-n).
- SANS Cert Checker Function: sans_cert_checker(name) queries the GIAC website for SANS certifications of an individual. It replaces spaces, makes the name lowercase, and retrieves certification details, organizing them by analyst ID.
- Read Names from File: read_names_from_file() reads names from a file (names.txt) and returns a list of names.
- Output Function: output_function(names) processes the names, performs SANS cert checks, and prints results for each individual, including name, analyst ID, and certifications.

The script can be used to check SANS certifications for individuals either through a file or by providing names directly on the command line.

## Example Output

```bash
$ python3 sans_cert_checker.py -n "Brian, Mark"
[+] Name: Brian, Analyst ID: XXX, Certs: ['GPEN', 'GAWN', 'GCIH']
[+] Name:  Mark, Analyst ID: XXX, Certs: ['GX-IH', 'GX-IA', 'GX-CS', 'GSP', 'GPYC', 'GXPN', 'GWAPT', 'GCPM', 'GSE', 'GCIA', 'GPEN', 'GCIH', 'GSEC']
```
