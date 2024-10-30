import os
import re

# Replaces in the given directory and its subdirectories in all files matching the given pattern the given search to substitution pattern
# In the replacement regex no escaping is necessary. Replacement groups are written so: \1
def replace(directory, file_pattern, replacements):
    file_pattern_compiled = re.compile(file_pattern)
    for current_directory, dirs, files in os.walk(directory):
        dirs.sort()
        for file in files:
            if file_pattern_compiled.match(file):
                file_path = os.path.join(current_directory, file)
                print(f"Checking: {file_path}")
                with open(file_path, 'r') as f:
                    content = f.read()
                
                modified_content = content
                for pattern, replacement in replacements.items():
                    modified_content = re.sub(pattern, replacement, modified_content, flags=re.MULTILINE)
                
                if modified_content != content:
                    with open(file_path, 'w') as f:
                        f.write(modified_content)
                    print(f"Modified: {file_path}")