from passlib.hash import nthash

# Converts email:plaintext dump to email:ntlm to use for practice with hashcat
# Allows me to to practice with real wordlists to see where my masks, rules, 
# and wordlists are effective
# requires pip3 install passlib
# Usage: python plaintext_to_ntlm_hashcat.py <file_path>

def ntlm_hash(password):
    """Generate NTLM hash from password."""
    return nthash.hash(password).upper()

def process_file(file_path, output_path):
    """Read the file and process each line to generate NTLM hash."""
    try:
        # Open file with write mode, so it doesn't append
        # There's a better way to do this with popen? I don't remember
        with open(file_path, 'r') as file, open(output_path, 'w') as output_file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(':', 1)
                    if len(parts) == 2:
                        email, password = parts
                        # Generate NTLM hash
                        hash = ntlm_hash(password)
                        # Print the output x3
                        print(f"{email}:{password}:{hash}")
                        # Write each line to a file
                        output_file.write(f"{email}:{hash}\n")
                    else:
                        print(f"Skipping invalid line: {line}")
    except FileNotFoundError:
        print(f"File error: {file_path}")
    except Exception as e:
        print(f"Other error: {e}") 

if __name__ == "__main__":
    # Change this to input from console
    # file_path = input("File: ")
    file_path = 'email_plaintext.txt'
    output_path = 'email_ntlm.txt'
    process_file(file_path, output_path)