import re
import sys

if len(sys.argv) != 3:
    print("Usage: python replace_placeholders.py input.html output.html")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

# Regex pattern:
# matches https://via.placeholder.com/300x300/4a4a4a/ffffff
# plus anything after it (until whitespace or quote)
pattern = r"https://via\.placeholder\.com/300x300/4a4a4a/ffffff[^\"'\s]*"

content = re.sub(pattern, "https://placehold.co/500", content)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Replacements complete! Output written to {output_file}")
