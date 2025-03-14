import os
from substitution import *

# Convert a phind answer into Redmine syntax
if __name__ == "__main__":
    execution_directory = os.getcwd()
    
    # Modify all files following the given RegEx file pattern searching recursivelly within the given directory
    replace(execution_directory, r'some-logs-cleaned\.txt', {
        # remove meta sequences
        r'\[.*?m' : r'',
    })
