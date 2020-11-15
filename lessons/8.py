# """shutil"""
#
# import shutil, os, pathlib, sys
#
# current_directory = pathlib.Path.cwd()  # get current directory to use later for creating Path objects
# test_folder = pathlib.Path.joinpath(current_directory,
#                                     pathlib.Path(r"test_folder"))  # create path for first test folder
# test_folder2 = pathlib.Path.joinpath(current_directory,
#                                      pathlib.Path(r"test_folder2"))  # create path for second test folder
# os.makedirs(test_folder, exist_ok=True)  # create first folder
# os.makedirs(test_folder2, exist_ok=True)  # create 2nd folder
# os.chdir(test_folder)  # change cwd to 1st test folder to create files there
#
# print("data", file=open("test_file1.txt", mode="a"))  # create files
# print("data", file=open("test_file2.txt", mode="a"))
# print("data", file=open("test_file3.txt", mode="a"))
#
# shutil.copy("test_file1.txt",
#             pathlib.Path.joinpath(test_folder2, "test_file1_copied.txt"))  # copy files to 2nd test folder, change names
# shutil.copy2("test_file2.txt",
#              test_folder2)  # name change is optional, its like cp vs mv. !NB copy2 tries to preserve file metadata, still not all metadata is preserved
# #shutil.move("test_file3.txt", test_folder2)  # this WILL throw an error if file exist, however we can avoid this with full path!
# shutil.move("test_file3.txt", pathlib.Path.joinpath(test_folder2, "test_file3.txt"))  # This will just overwrite the file.
#
# shutil.make_archive(pathlib.Path.joinpath(test_folder2, "archived_folder"), "zip",
#                     test_folder)  # create the archive of the test_folder, located in test_folder2. !NB there are MORE args here, you can learn them later
#
# subfolder = pathlib.Path.joinpath(test_folder, pathlib.Path("subfolder"))  # create subfolders paths
# os.makedirs(pathlib.Path.joinpath(subfolder, "sub_subfolder"), exist_ok=True)
#
# os.chdir(subfolder)
# print("data", file=open("sub_file1.txt", mode="a"))
#
# shutil.copytree(subfolder, pathlib.Path.joinpath(test_folder2, "rescued_folder\\"),
#                 dirs_exist_ok=True)  # copying subfolder with renaming to 2nd test folder
#
# os.makedirs(pathlib.Path.joinpath(test_folder2, "unzip_here"), exist_ok=True)
# shutil.unpack_archive(pathlib.Path.joinpath(test_folder2, "archived_folder.zip"),
#                       pathlib.Path.joinpath(test_folder2, "unzip_here"))  # unzip archive
#
# os.chdir(pathlib.Path.joinpath(test_folder, pathlib.Path(
#     "..")))  # move out of our folders to delete them, otherwise OS will keep them locked
#
# sys.exit("do not cleanup yet")
# shutil.rmtree(test_folder, ignore_errors=True)  # delete all files in all subfolders recursively
# shutil.rmtree(test_folder2, ignore_errors=True)
# for f, sf, flist in os.walk(test_folder,
#                             topdown=False):  # we do not have rm -rf here so we have to go from leafs to root with topdown=False
#     if not os.listdir(f):  # if the folder doesnt have subfolders and files in it - remove it
#         os.rmdir(f)
#
# for f, sf, flist in os.walk(test_folder2, topdown=False):
#     if not os.listdir(f):
#         os.rmdir(f)
#=================================================================================================================================
#
# """subprocess"""
# import subprocess
#
# subprocess.run(["C:\Windows\System32\calc.exe"])
# notepad = subprocess.run([r"C:\Windows\System32\notepad.exe", r"C:\Users\yaizk\Desktop\to_delete\test.txt"], capture_output=True)
# print(notepad.returncode)  # get return code value
# print(notepad.stdout)   # get stdout data
# print(notepad.stderr)   # get stderr data
# notepad.check_returncode()  # raises CalledProcessError if exit code is not 0
# # subprocess.run(["ls", "-l"], shell=True)  # shell used to use shell to run our command for example to get access to env. vars, Python can do it w/o shell btw.
#
# # Actually this is very big and powerful tool, you can master it if you like - just google it


#=================================================================================================================================
#
# """Regular expressions"""
#
# # first of all there are 2 ways to address regex:
# # 1. To compile them into variable and use it
# # 2. Use regex each time you call a function of re module
# # We will mostly use the 1st way, compiled regex has all necessary functions as class object methods
#
# import re
# phone_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')  # () represent a capturing group, \d represent a single digit [0-9]
# match = phone_regex.search('My number is 415-555-4242, 415-555-4141')  # The string we search for passed as argument to compiled regex method
#
#
#
# """Let's see what re.search can offer us:"""
#
# print(match)
# print(f"match.group() is the same as match.group(0), they return: {match.group()}")  # return match
# print(f"first group returns: match.group(1) = {match.group(1)}, second group: match.group(2) = {match.group(2)}")  # return 1st(2nd) capturing group match
# print(f"match.groups() returns {match.groups()}")  # return all capturing group matches in a tuple
#
#
#
# """Let's add some logic to our regex:"""
#
# import re
# l_regex = re.compile(r"(Fat|Bat|Rat)man")  # We can use | symbol as OR
# print(l_regex.search("Batman").group())  # again just a reminder that we can return different stuff from re.Match object
# print(l_regex.search("Fatman").groups())
# print(l_regex.search("Ratman").group(0))
# print(l_regex.search("Doberman"))
#
#
#
# """Optional matching, zero or more, one or more"""
#
# # ? modifier stands for 0 or one of preceding capturing group
#
# import re
# opt_regex = re.compile(r"Bat(wo)?man")
# print(opt_regex.search("Batman"))
# print(opt_regex.search("Batwoman").group())
# print(opt_regex.search("Batwoman").group(1))
#
# # + stands for 1 or one of preceding capturing group
#
# import re
# one_or_more_regex = re.compile(r"Bat(wo)+man")
# print(one_or_more_regex.search("Batman"))
# print(one_or_more_regex.search("Batwoman").group())
# print(one_or_more_regex.search("Batwoman").group(1))
# print(one_or_more_regex.search("Batwowoman").group())
#
# # * stands for zero or more of preceding capturing group
#
# import re
# star_regex = re.compile(r"Bat(wo)*man")
# print(star_regex.search("Batman"))
# print(star_regex.search("Batwoman").group())
# print(star_regex.search("Batwowowoman").group())
#
#
# # match position as you've seen is the attribute of re.Match object:
#
# import re
# star_regex = re.compile(r"Bat(wo)*man")
# attr_match = star_regex.search("Batman")
# print(attr_match.span())
# print(attr_match.start())
# print(attr_match.end())
#
#
# """Exact count of matches"""
#
# import re
# count_regex = re.compile(r"(ha){3}")
# print(count_regex.search("hahahaha"))
# print(count_regex.search("haha"))
# print(count_regex.search("hahaha"))
#
# """Greedy and non-greedy match"""
#
# import re
# greedy_regex = re.compile(r"(ha)+")
# non_greedy_regex = re.compile(r"(ha)+?")
#
# print(greedy_regex.search("hahahaha"))
# print(non_greedy_regex.search("hahahaha"))
#
#
#
# """re.findall"""
# # What if we need to get all matches from our string?
# # we'd use re.findall
# import re
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # has no groups
# print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
#
# # If there are groups in the regular expression, then findall() will return a list of tuples.
# # Each tuple represents a found match, and its items are the matched strings for each group in the regex.
# # To see findall() in action, enter the following into the interactive shell
# # (notice that the regular expression being compiled now has groups in parentheses):
#
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # has groups
# print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))  # list of tuples returned
#
#
# """Character classes"""
# import re
# char_re = re.compile(r"[aeou]")
# print(char_re.findall("anappeanorangeawatermelon"))  # actually [] means - match ANY character in brackets
# char_re = re.compile(r"[^aeou]")
# print(char_re.findall(r"anappeanorangeawatermelon"))  # we can invert this with ^ = ANY character NOT in brackets
#
#
# """Positioning within string"""
# import re
# # Actually we have 2 symbols: ^ = at the start of the string and $ = at the end of the string
#
# start_re = re.compile(r"^[Helo]+\s?[W|w]orld!")  # ^ shows string start location and our positioning towards it
#
# print(start_re.search("ororo Hello world!"))
# print(start_re.search("Helloworld!"))
#
# end_re = re.compile(r"[Helo]+\s?[W|w]orld!$")  # $ shows location of string end and our positioning towards it
# print(end_re.search("ororo Helloworld!"))
# print(end_re.search("Helloworld! ororo"))
#
# both_re = re.compile(r"^[Helo]+\s?[W|w]orld!$")  # they could be used at the same time
#
# print(both_re.search(r"Hello world!"))
#
#
#
# """Wildcard character + modifiers"""
#
# import re
#
# wild_re = re.compile(r"Wat.+melon")  # . = any symbol (wildcard),
# print(wild_re.search(r"Watermelon"))
#
# wild_re_any = re.compile(r"Wa.*")  # .* = any amount of wildcards
# print(wild_re_any.search(r"Watermelon"))
# print(wild_re_any.search(r"Waterfall"))
#
# wild_re_non_greedy = re.compile(r"Wa.*?")  # .*? - any amount of any symbols, but non greedy
# wild_re_greedy = re.compile(r"Wa.*")  # same but greedy
# print(wild_re_non_greedy.search("Waterfall"))
# print(wild_re_greedy.search("Waterfall"))
#
#
#
# """re.DOTALL, re.VERBOSE, re.IGNORECASE"""
#
# # What if we try to match multiline string with our regex? Lets try and see what will happen
#
# import re
#
# mline_re = re.compile(r".*")  # we match everything :)
#
# print(mline_re.search("first string\nsecondstring\nthirdstring"))
#
# mline_re = re.compile(r".*", re.DOTALL)  # re.DOTALL includes \n for wildcard match
# print(mline_re.search("first string\nsecondstring\nthirdstring"))
#
# ignore_re = re.compile(r"[abc]+", re.IGNORECASE)  # re.IGNORECASE just ignores the case of string letters
# #ignore_re = re.compile(r"[abc]+")
# print(ignore_re.search("AABC"))
#
# # re.VERBOSE allows us to compile multiline regex also comments are allowed
# datePattern = re.compile(r"""^(.*?) # all text before the date
#     (([01])?\d)- # one or two digits for the month
#     (([0123])?\d)- # one or two digits for the day
#     ((19|20)\d\d) # four digits for the year (must start with 19 or 20)
#     (.*?)$ # all text after the date
#     """, re.VERBOSE)
#
#
#
# """re.sub"""
#
# import re
# namesRegex = re.compile(r'Agent \w+')
# print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))


##===========================================================================================
#
# """Error handling"""
#
# test = [1, 2, "a", "bb", "ccc", 5]
#
# for item in test:
#     try:
#         print(len(item))
#     except Exception as my_exception:  # Exception is a general class for all exceptions so it can be ANY exception, however you may put specific exceptions here.
#         print(f"Error occured: {my_exception}, item is {item}")  # you can write errors to some log file here
#     else:
#         print(f"No errors happened with item {item}")  # this code executed ONLY if no errors happened in try: block, i.e. except: block was not executed
#     finally:
#         print("This code will be executed anyway")  # this code executed regardless of try: block state


