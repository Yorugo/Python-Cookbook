import os

print(os.getcwd())

# Change the current working directory to where this python file is
os.chdir(os.path.dirname(os.path.realpath(__file__)))


def write_txt_file(name, text):
    try:
        os.mkdir("test_files")
    except:
        print("directory already exists")

    with open(f"test_files/{name}.txt", "w") as wf:
        wf.write(text)


def copy_txt_file(name):
    # copy a text file
    with open(f"test_files/{name}.txt", "r") as rf:
        with open(f"test_files/{name}_copy.txt", "w") as wf:
            for line in rf:
                wf.write(line)


def copy_jpg(name):
    # copy an entire file, like an image, by using b for byte
    # use chunks so you don't run out of memory
    with open(f"images/{name}.jpg", "rb") as rb:
        with open(f"images/{name}_copy.jpg", "wb") as wb:
            chunk_size = 4096
            rb_chunk = rb.read(chunk_size)
            while len(rb_chunk) > 0:
                wb.write(rb_chunk)
                rb_chunk = rb.read(chunk_size)


def other():
    with open("test_files/text_file.txt", "r") as f:
        # for line in f:
        #     print(line, end="")

        f_contents = f.read(35)
        print(f_contents, end="")
        f_contents = f.read(35)
        print(f_contents, end="")

    # "r" is used for reading
    # file has to exist to be opened
    with open("test_files/text_file.txt", "r") as f:
        size_to_read = 7

        f_contents = f.read(size_to_read)

        while len(f_contents) > 0:
            print(f"|{f.tell()}|", end="")
            print(f_contents, end="*")
            f_contents = f.read(size_to_read)

    # "w" is used for writing
    # if the file doesn't exist, then it will create it
    # if the file does exist, then it will overwrite it
    # even if no logic is added.
    with open("test_files/text_file.txt", "w") as f:
        f.write("This\n")
        f.write("That")
        f.write("Other")

        # f.seek(0)
        # f.write("overwritten")

    # "a" is used for appending
    # if the file doesn't exist, then it will create it
    # if the file does exist, then it will overwrite it
    with open("test_files/text_file.txt", "a") as f:
        pass


# When writing using triple quotes, be careful of tab indentation
write_txt_file("test", """This is the text file I want to create in order to test the program.
I will take note of the line breaks,


for example, there were three just above this,

and there were two just above this! """)

copy_txt_file("test")

copy_jpg("test_image")
