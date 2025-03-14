import os
from substitution import *

# Update versions in POM
if __name__ == "__main__":
    execution_directory = os.getcwd()
    
    # Modify all files following the given RegEx file pattern searching recursivelly within the given directory
    replace(execution_directory, r'pom\.xml', {
        r'<java\.version>.+<\/java\.version>' : r'<java.version>17</java.version>',

    })
