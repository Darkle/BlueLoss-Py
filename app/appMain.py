
msg = 'hi'

asdFoo = 5

print(
    msg.capitalize())

print(2+2 )
# see if this is fixed: https://github.com/DamnWidget/anaconda/issues/747
print(3+3)






def main():
    x = 'a'
    _x = 'a'
    _ = 'a'


# define the name of the file to read from
filename = "test.txt"

# open the file for reading
filehandle = open(filename, 'r')
while True:
    # read a single line
    line = filehandle.readline()
    if not line:
        break
    print(line)

# close the pointer to that file
filehandle.close()
