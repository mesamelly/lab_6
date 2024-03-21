# Melissa Li's Submission
def menu():
    '''
    Prints the decoding/encoding menu.
    :return: Does not return anything.
    '''
    print('Menu')
    print('-------------')
    print('1. Encode\n2. Decode\n3. Quit\n')


def decode(password):
    '''
    Decodes a password by adding 3 to each digit.
    :param password: The password to be decoded.
    :return: Returns the decoded password.
    '''
    decoded = ''
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2']
    for i in range(8):
        current_num = str(password[i])
        decoded += nums[nums.index(current_num) + 3]
    return decoded


def main():
    option = 4
    password = ''
    while option != 3:
        menu()
        print('Please enter an option: ', end='')
        option = int(input())
        if option == 1:
            print('Please enter your password to encode: ', end='')
            password = input()
            print('Your password has been encoded and stored!\n')
        if option == 2:
            decoded = decode(password)
            print(f'The encoded password is {decoded}, and the original password is {password}.\n')


if __name__ == '__main__':
    main()
