import argparse
#import argparse to pass commandline imputs
import hashlib
#import hashlib to be able to hash the words in the list



def pass_cracker(filename, passwords_to_compare):
    #define our function and pass in the two files that we are looking at
    file = open(filename, 'r')
    #create file variable and open and read the given file
    user_password_list = open(passwords_to_compare, 'r')
    #create a user password list variable to open the user passwords and read them
    lines = file.readlines()
    #create a lines variable that is equal to the lines in our file being read
    pass_lines = user_password_list.readlines()
    #create a pass lines variable that is equal to the lines in the user password file being read



    for passwords in pass_lines:
        #creates a for loop that iterates through the 
        seperated_passwords = passwords.split(':')
        #creates a variable that is the passwords split from the username that their connected to
        cleaned_passwords = seperated_passwords
        #creates just a different name for the cleaned password variable, easier to understand
        user_passwords = cleaned_passwords[1].strip()
        #user passwordes is a variable equal to the 2nd index in the user password lines which is the hashed passwords



        for line in lines:
            #creates a for loop that loops therough the word list and hashes the words
            line_clean = line.strip()
            #creates a line clean variable that is the words cleaned of any invisible characters
            hashed_pass = hashlib.sha256(line_clean.encode()).hexdigest()
            #creates a hashed pass variable that is the word from the word list cleaned and hashed 
            if user_passwords == hashed_pass:
                #creates an if statement that says if the user password and hashed pass word are a match then exicute whats underneath
                print(f'{cleaned_passwords[0]}:'+ line_clean)
                #Uses the print function to print us the user name and the original word that represents their password before being hashed.

# pass_cracker('wordlist.txt', 'passwords.txt')

if __name__ == "__main__":
#says that if the name of the main function is called than exicute

    parser = argparse.ArgumentParser(description="crack passwords.")
    #creates a parser argument to pass command line imput

    parser.add_argument('passwords_to_compare', help='The known user passwords')
    #creates an arguement that is the passwords that the users have
    parser.add_argument('filename', help='The file with words to hash into passwords')
    #creates an argument that is the words that are getting hashed 

    args = parser.parse_args()
    #creates an args variable of command impits like the file names

    pass_cracker(args.filename, args.passwords_to_compare)
    #calls the function and has args that will acept what we end are put them where their args says