import argparse
import hashlib



def pass_cracker(filename, passwords_to_compare):
    file = open(filename, 'r')
    user_password_list = open(passwords_to_compare, 'r')
    lines = file.readlines()
    pass_lines = user_password_list.readlines()
    for passwords in pass_lines:
        seperated_passwords = passwords.split(':')
        cleaned_passwords = seperated_passwords
        user_passwords = cleaned_passwords[1].strip()
        # userpass_list.append(user_passwords) 
        for line in lines:
            line_clean = line.strip()
            hashed_pass = hashlib.sha256(line_clean.encode()).hexdigest()
            # hashed_passes.append(hashed_pass)
            if user_passwords == hashed_pass:
                print(f'{cleaned_passwords[0]}:'+ line_clean)

# pass_cracker('wordlist.txt', 'passwords.txt')

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="crack passwords.")

    parser.add_argument('passwords_to_compare', help='The known user passwords')
    parser.add_argument('filename', help='The file with words to hash into passwords')

    args = parser.parse_args()

    pass_cracker(args.filename, args.passwords_to_compare)