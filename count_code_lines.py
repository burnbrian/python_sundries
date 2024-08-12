import pathlib

def count_code_lines(path):
    # Read through all files in the directory by line
    # Count the number of lines of code
    # Print the total number of lines of code
    total_lines = 0
    for file in path.glob('*.py'):
        with open(file, 'r') as f:
            # Only open question files that are py
            # print(f'File name: {f}')
            lines = f.readlines()
            # Do not count comments #
            for line in lines:
                # Do not count empty lines
                if line.strip() and not line.strip().startswith('#') and 'import' not in line:
                        total_lines += 1
    # Total lines of code
    return total_lines

def main():
    # Use a specific directory
    path = pathlib.Path('/home/student/course-sans-sec573/questions/')
    print(f'Total lines of code: {count_code_lines(path)}.')
    pass

if __name__ == "__main__":
    main()