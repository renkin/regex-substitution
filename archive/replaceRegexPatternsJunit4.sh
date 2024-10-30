#!/bin/bash

# Parameters
BASE_DIRECTORY='/home/rene/Projekte/SAB/git'
FILE_PATTERN='*Test*.java'

# Perform find and replace operation for given search and replacement patterns
perform_replace() {
    local SEARCH_PATTERN=$1
    local REPLACEMENT_PATTERN=$2
    local file=$3
    
    SEARCH_PATTERN_HITS=$(grep -c -E "$SEARCH_PATTERN" "$file")

    if [ $SEARCH_PATTERN_HITS -gt 0 ]; then
        echo "- $SEARCH_PATTERN_HITS time(s) found $SEARCH_PATTERN in $file"
    fi
    
    sed -r -i "s/$SEARCH_PATTERN/$REPLACEMENT_PATTERN/g" "$file"
    # sed --debug -r -i "s/$SEARCH_PATTERN/$REPLACEMENT_PATTERN/g" "$file"
}

# Find all files in a directory (recursively) that match a specific pattern
files=$(find $BASE_DIRECTORY -type f -name $FILE_PATTERN)

# Iterate over each file and perform the find and replace operation for each pattern pair
# Matching groups are written as \1 not $1 (sed syntax)
echo ""
for file in $files; do
    #echo "Processing file $file ..."
    perform_replace 'import org.junit.Test' '' "$file"
    perform_replace 'import org.junit.runner.RunWith' '' "$file"
done
