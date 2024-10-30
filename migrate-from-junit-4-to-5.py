import os
from substitution import *

# Migrate from JUnit 4 to 5
if __name__ == "__main__":
    execution_directory = os.getcwd()
    
    replace(execution_directory, r'.*Test.*\.java', {
        r'import org\.junit\.Before;' : r'import org.junit.jupiter.api.BeforeEach;',
        r'import org\.junit\.After;' : r'import org.junit.jupiter.api.AfterEach;',
        r'import org\.junit\.BeforeClass;' : r'import org.junit.jupiter.api.BeforeAll;',
        r'import org\.junit\.AfterClass;' : r'import org.junit.jupiter.api.AfterAll;',
        r'import org\.junit\.Test' : r'import org.junit.jupiter.api.Test',
        r'import org\.junit\.runner.RunWith' : r'import org.junit.jupiter.api.extension.ExtendWith',
        r'import org.mockito.junit.MockitoJUnitRunner' : r'import org.mockito.junit.jupiter.MockitoExtension',
        r'import org.springframework.test.context.junit4.SpringRunner': r'import org.springframework.test.context.junit.jupiter.SpringExtension',
        r'import static org\.junit\.Assert.': r'import static org.junit.jupiter.api.Assertions.',
        r'import org\.junit\.Ignore' : r'import org.junit.jupiter.api.Disabled',

        r'@Before$' : r'@BeforeEach',
        r'@After$' : r'@AfterEach',
        r'@BeforeClass$' : r'@BeforeAll',
        r'@AfterClass$' : r'@AfterAll',
        r'@RunWith\(MockitoJUnitRunner\.class\)' : r'@ExtendWith(MockitoExtension.class)',
        r'@RunWith\(SpringRunner\.class\)' : r'@ExtendWith(SpringExtension.class)',
        r'@Ignore' : r'@Disabled',

        r'import static org\.junit\.jupiter\.api\.Assertions\.assertThat' : r'import static org.assertj.core.api.Assertions.assertThat',
        r'(assertThat\(.*),\s*is(\(.*\))\);' : r'\1).isEqualTo\2;',
        r'(assertThat\(.*),\s*(is.*)\);' : r'\1).\2;',
        r'(assertThat\(.*),\s*containsString(.*)\);' : r'\1).contains\2;',
        r'(assertThat\(.*),\s*containsInAnyOrder(.*)\);' : r'\1).contains\2;',
        r'(assertThat\(.*),\s*hasItems(.*)\);' : r'\1).contains\2;',
        r'(assertThat\(.*),\s*hasSize(.*)\);' : r'\1).hasSize\2;',
        r'assertEquals\((".*"),\s*(.*,.*)\);' : r'assertEquals(\2, \1);',
        r'assertNotNull\((".*"),\s*(.*)\);' : r'assertNotNull(\2, \1);',
    })
