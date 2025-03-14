# RegEx substitution #

### What is this repository for? ###

The repository contains a Python scripts to do multiline substitutions using regular expressions.

The script is used for some automated migrations/conversions:

- Migrate from JUnit 4 to 5
- Migrate from SpringFox to Springdoc Open API
- Update versions in POM
- Convert a phind answer into Redmine syntax
- Remove meta sequences (for colors) from e.g. logs

### How do I get set up? ###

1. Clone the repository
1. Change to the directory where the changes should be applied
1. Execute any of the migration scripts inside the directory where the changes should be applied providing the path to the scipt, e.g. `python ../regex-substition/migrate-from-junit-4-to-5.py`

### Contribution guidelines ###

- Add another migration script analog the existing ones

### Who do I talk to? ###

https://linktr.ee/renekiessig