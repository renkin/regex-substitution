#!/bin/bash

# Parameters
BASE_DIRECTORY='src/main/java/com/t_systems_mms/sab_fp2'


# Perform find and replace operation for given search and replacement patterns
perform_replace() {
    local SEARCH_PATTERN=$1
    local REPLACEMENT_PATTERN=$2
    local file=$3
    
    SEARCH_PATTERN_HITS=$(grep -c -E "$SEARCH_PATTERN" "$file")
    echo "- $SEARCH_PATTERN_HITS time(s) replaced $SEARCH_PATTERN with $REPLACEMENT_PATTERN"
    
    sed -r -i "s/$SEARCH_PATTERN/$REPLACEMENT_PATTERN/g" "$file"
    # sed --debug -r -i "s/$SEARCH_PATTERN/$REPLACEMENT_PATTERN/g" "$file"
}

# Find all files in a directory (recursively) that match a specific pattern
files=$(find $BASE_DIRECTORY -type f \( -name '*Controller.java' -o -name '*Command.java' \) )

# Iterate over each file and perform the find and replace operation for each pattern pair
# Matching groups are written as \1 not $1 (sed syntax)
echo ""
for file in $files; do
    echo "Processing file $file ..."

    # Controller changes
    perform_replace 'import io.swagger.annotations.ApiOperation' 'import io.swagger.v3.oas.annotations.Operation' "$file"
    #ersetzt auch implizit import io.swagger.annotations.ApiResponses mit entsprechendem import io.swagger.v3.oas.annotations.responses.ApiResponses
    perform_replace 'import io.swagger.annotations.ApiResponse' 'import io.swagger.v3.oas.annotations.responses.ApiResponse' "$file"
    #die ApiResponses Klammer ist in SpringDoc nicht notwendig und wird entfernt
    perform_replace 'import io.swagger.v3.oas.annotations.responses.ApiResponses;' '' "$file"
    perform_replace 'import springfox.documentation.annotations.ApiIgnore' 'io.swagger.v3.oas.annotations.Hidden' "$file"

    perform_replace '@ApiIgnore' '@Hidden' "$file"
    perform_replace '@ApiOperation\("(.+)' '@Operation(summary = "\1' "$file"
    perform_replace '@ApiResponse\(code\s*=\s*(.+),\s*message\s*=\s*"(.+)"' '@ApiResponse\(responseCode = "\1", description = "\2"' "$file"
    #die ApiResponses Klammer ist in SpringDoc nicht notwendig und wird entfernt
    perform_replace '\s*@ApiResponses\(\{' '' "$file"
    perform_replace '(@ApiResponse\(.*\)),' '\1' "$file"
    perform_replace '(@ApiResponse\(.*\))\}\)' '\1' "$file"

    # Command changes
    perform_replace 'import io.swagger.annotations.ApiModelProperty' 'import io.swagger.v3.oas.annotations.media.Schema' "$file"

    perform_replace '@ApiModelProperty\("(.+)' '@Schema(description = "\1' "$file"
    perform_replace '@ApiModelProperty\(notes\s*=\s*"(.+)' '@Schema(description = "\1' "$file"

    echo ""
done
