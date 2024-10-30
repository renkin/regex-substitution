import os
from substitution import *

# Update versions in POM
if __name__ == "__main__":
    execution_directory = os.getcwd()
    
    replace(execution_directory, r'pom\.xml', {
        r'<java\.version>.+<\/java\.version>' : r'<java.version>17</java.version>',

    })
