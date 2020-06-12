# Count and Fix Green Eggs and Ham
#
# Some of you may remember the Dr. Sues story "Green Eggs and Ham". For those of you that don't remember it or have never heard of it,
# here is the story. However, there is a problem with the story I gave you - every time the word I is used, it is lowercase.
# Because of this problem, your job is to do the following:
#
#     Copy the story I gave you into a regular text file.
#     Create a program that reads through the story and makes the letter i uppercase any time it should be.
#     (Make sure to change it when it's used in sam-I-am's name too.)
#     Have your program make a new file, and have it write out the story correctly.
#     Print out how many errors were corrected.
#     When you're finished, you should have corrected this many errors.


def word_i_checker(word):
    """Function to replace i with I and fix Sam-I-am's name"""
    if str(word) == "i":
        return "I", 1
    elif str(word) == "Sam-i-am" or str(word)[:-1] == "Sam-i-am":  # we check both "clear" name and name -1 symbol in case of ! or . after the name.
        return "Sam-I-am", 1
    return str(word), 0


counter = 0
mylist = []
with open("story.txt", mode="r", encoding="utf8") as srcfile:  # open file
    for string in srcfile.readlines():  # read it string by string
        for word in string.split():  # read splitted string word by word
            result = word_i_checker(word)  # save result to variable
            mylist.append(result[0])  # append checked word to list
            counter += int(result[1])  # if word was fixed, counter will be increased by 1 returned from function
            mylist.append(" ")  # to keep spaces of original text
        mylist.append("\n")  # to keep newlines of original text

print(counter)

with open("story_fixed.txt", mode="w", encoding="utf8") as outfile:
    outfile.writelines(mylist)  # saving to new file
