import os

keystore_path = os.getenv('KEYSTORE_PATH')


def read_code():
    # read code from file & transfer into Array
    s = []
    with open(keystore_path, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            s.append(line)
    key = "Code: [" + s[0]+"]" + "  -  (" + str(len(s)-1) + ") left"
    # key=''.join(s[0]) # remove " "

    # del first code which has been used and write into file
    with open(keystore_path, 'w') as file:
        del s[0]
        for line in s:
            file.write(line+'\n')
    return key