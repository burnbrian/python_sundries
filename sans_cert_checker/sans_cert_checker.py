import argparse
import pathlib
import json
import requests

def sans_cert_checker(name):
    """Check for SANS certs..."""
    url = "https://www.giac.org/certified-professionals/search?q="
    # Proxy requests through burpsuite
    # https://www.giac.org/certified-professionals/search?q=mark%20baggett
    # Replace spaces with %20 and make lowercase
    name_strip = name.replace(' ', '%20').lower()
    response = requests.get(url+name_strip)
    # If request response is 200 continue
    if response.status_code == 200:
        # Make data a json object/dictionary
        data = json.loads(response.text)
        results = {}
        # Could probably use a list comprehension here
        for item in data['results']:
            analyst_id = item['analyst_id']
            cert_initials = item['initials_upper']
            if analyst_id in results:
                results[analyst_id].append(cert_initials)
            # Already exists in dict, just append it
            else:
                results[analyst_id] = [cert_initials]
        return results
    else:
        # Professional level error handling
        print(f'[!] Error: {name} not found...')
        return response.status_code

def read_names_from_file():
    """Read names from file"""
    # Hard coded file path
    names_file = pathlib.Path('names.txt')
    # Read lines from text file and return a list of names
    names = [name.strip() for name in names_file.read_text().splitlines()]
    return names

def output_function(names):
    """Read through the names and print results"""
    for name in names:
        # Return results from the def sans_cert_checker
        results = sans_cert_checker(name)
        # Iterate through the results dictionary and print to std_out
        for analyst_id, initials in results.items():
            print(f'[+] Name: {name}, Analyst ID: {analyst_id}, Certs: {initials}')

def main():
    # Setup args, require at least one
    parser=argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    # File and name
    group.add_argument('-f', '--filename', help='File with one name per line')
    group.add_argument('-n', '--name', help='Comma separated list of names or single name')
    # Set args
    args=parser.parse_args()

    # Do the thing
    if args.filename is not None:
        names = read_names_from_file()
        output_function(names)
    else:
        names = args.name.split(",")
        output_function(names)

if __name__ == "__main__":
    main()