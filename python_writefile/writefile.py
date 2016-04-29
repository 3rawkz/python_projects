# if filename.exist() == True: write in existing file 'filename.ext'
# else: create filename.ext & write in filename.ext


text = " Here's some text. \nHere's some text on another line!"

save_file = open('c:/users/dave quarick/desktop/python_projects/python_writefile', 'w')
save_file.write(text)
save_file.close() 
