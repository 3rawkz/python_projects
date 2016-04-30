# appending new data to a prexisting file


append_me = "Here's new information!\nSo exciting!"

# the second argument represents the action we plan to perform to the file: 'a' = append
save_file = open('c:/users/dave quarick/desktop/python_projects/python_writefile', 'a')
save_file.write(append_me)
save_file.close()
