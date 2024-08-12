import pathlib
import yaml
import re

# Count the number of red and blue tags
def count_tags(file_path):
    red_count = 0
    blue_count = 0
    for file_path in file_path.glob('*.md'):
        # Read the file's content
        with open(file_path, 'r') as file:
            content = file.read()
        metadata = re.search(r'---(.*?)---', content, re.DOTALL).group(1)
        data = yaml.safe_load(metadata)
        tags = data.get('tags', [])
        red_count += tags.count('red')
        blue_count += tags.count('blue')
    return red_count, blue_count

# Calculate the percentage of red and blue in a color
# http://www.cknuckles.com/rgbsliders.html
def red_or_blue(red_val, blue_val):
    red_percentage = red_val / (red_val + blue_val)
    blue_percentage = blue_val / (red_val + blue_val)
    rgb_value = "(" + str(int(red_percentage * 255)) + ", 0, " + str(int(blue_percentage * 255)) + ")"
    hex_value = '#%02x%02x%02x' % (int(red_percentage * 255), 0, int(blue_percentage * 255))
    return "RGB: " + rgb_value + "\nHEX: " + hex_value

# Main
# Determine ratio of offensive to defensive tags
def main():
    local_path = "/home/brian/Development/hackernotebook/src/posts/"
    red, blue = count_tags(pathlib.Path(local_path))
    print(red_or_blue(red, blue))

# Call the main function
if __name__ == "__main__":
    main()
