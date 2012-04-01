# Module for reserved words

class rwords:
    # read in file/strip trailing and leading whitespace
    rw_file = open('reservedWord.txt').read().strip(' ')

    # Put the reserved words into an array, sorted by 'words'
    rw_array = []
    rw_array[:] = rw_file.split()

    def check_rword(word):
        # Check to see if the word is on the list
        array_length = len(rwords.rw_array)
        counter = 0
        value = 0
        for x in range(0, array_length):
            if rwords.rw_array[counter] == word:
                value = 1
            counter+= 1

        # Return the result
        if value == 1:
            return True
        else: return False
