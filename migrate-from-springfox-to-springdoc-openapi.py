import os
from substitution import *

# Migrate from SpringFox to Springdoc Open API
# See https://springdoc.org/migrating-from-springfox.html
if __name__ == "__main__":
    execution_directory = os.getcwd()
    
    # Controller changes
    replace(execution_directory, r'.*Controller\.java', {
        # Imports
        r'import io\.swagger\.annotations\.ApiOperation' : r'import io.swagger.v3.oas.annotations.Operation',
        # Replaces also implicitly 'import io.swagger.annotations.ApiResponses' with 'import io.swagger.v3.oas.annotations.responses.ApiResponses'
        r'import io\.swagger\.annotations\.ApiResponse' : r'import io.swagger.v3.oas.annotations.responses.ApiResponse',
        # The ApiResponses in brackets is not necessary in SpringDoc and is removed - import
        r'import io\.swagger\.v3\.oas\.annotations\.responses\.ApiResponses;' : r'',
        r'import springfox\.documentation\.annotations\.ApiIgnore' : r'io.swagger.v3.oas.annotations.Hidden',

        # Usages
        r'@ApiIgnore' : r'@Hidden',
        r'@ApiOperation\("(.+)' : r'@Operation(summary = "\1',
        r'@ApiResponse\(code\s*=\s*(.+),\s*message\s*=\s*"(.+)"' : r'@ApiResponse\(responseCode = "\1", description = "\2"',
        # The ApiResponses in brackets is not necessary in SpringDoc and is removed - usage
        r'\s*@ApiResponses\(\{' : r'',
        r'(@ApiResponse\(.*\)),' : r'\1',
        r'(@ApiResponse\(.*\))\}\)' : r'\1',
    })

    # Command changes
    replace(execution_directory, r'.*Command\.java', {
        # Imports
        r'import io\.swagger\.annotations\.ApiModelProperty' : r'import io.swagger.v3.oas.annotations.media.Schema',

        # Usages
        r'@ApiModelProperty\("(.+)' : r'@Schema(description = "\1',
        r'@ApiModelProperty\(notes\s*=\s*"(.+)' : r'@Schema(description = "\1',
    })
