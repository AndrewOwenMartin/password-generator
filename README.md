# password-generator
Python CLI password generator

## Not using a virtual environment

1. Clone the repo
2. Call like this `python3 password-generator/password_generator/generate_password`
3. See usage like this `python3 password-generator/password_generator/generate_password --help`

## Using a virtual environment

1. Clone the repo
2. *If necessary* make a virtual environment `python3 -m venv ./my-venv`
3. *If necessary* activate your virtual environment `. $YOUR_VENV/bin/activate`
4. Install the module `pip install password-generator`
5. Call like this `generate-password`

# Usage

`generate-password [-h] [-c CHARS] [password_length]`

- `-h`, `--help`: Print help text
- `-c`, `--chars`: A string of character sets (see below).
- `[password_length]`: Length of the generated password.

Default is password length = 32 chars = ldubms (All types of character except "similar" symbols)

## Character sets

- l - Use **L**owercase Letters: `abcdefghijklmnopqrstuvwxyz`
- d - Use **D**igits: `0123456789`
- u - Use **U**ppercase Letters: `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
- b - Use **B**asic Symbols: `!?#$&\*@`
- m - Use **M**ore Symbols: `%()+-=[]{}|~.,`
- s - **S**kip Similar Looking Characters: `0OoIl1`

# Examples

`generate-password 100 --chars ld`

100 character password using only lowercase and digits

`generate-password --chars ldubm 32`

32 character password using all lowercase, digits, uppercase, basic symbols, more symbols.
