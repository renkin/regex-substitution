import os
from substitution import *

# Convert a phind answer into Redmine syntax
if __name__ == "__main__":
    execution_directory = os.getcwd()
    
    replace(execution_directory, r'phind-to-redmine-converted\.txt', {
        # paragraph headings
        r'###\s+(.*?)$' : r'*\1*',
        
        # not numbered information list entry
        r'^- ' : r'* ',
        r'^  - ' : r'** ',
        r'^   - ' : r'** ',
        r'^    - ' : r'** ',

        # numbered information list entry
        r'^\d+\. ' : r'# ',

        # special case of first not numbered information list entry in numbered list:
        # # **Network Services**  - Consistent performance
        r'^(# \*\*.+?\*\*)\s+-\s+(.+)$' : r'\1\n** \2',

        # preformated and code blocks
        r'\n\n```\w*$' : r'\n\n<pre>',
        r'\n```$' : r'\n</pre>',

        # remove empty lines in lists, but keep the ones after headings
        r'[^*]\n\n^([*#]) ' : r'\n\1 ',

        # remove double, tripple etc. empty lines
        r'\n\n\n+' : r'\n\n',
    })
