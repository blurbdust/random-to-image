#So I got bored on a Fridasy night and got to thinking about evolution and how much I want to simulate it with a computer
#Seriously, particle simulations would be dope

import sys, getopt, io
from timeit import default_timer as timer
from random import randint

def main(argv):
    help_message = "main.py -w <width in pixels> -t <height in pixels> -o <output filename.ppm> -n "
    try:
        opts, args = getopt.getopt(argv,"hw:t:o:n:",["width=", "height=","ofile=", "num="])
    except getopt.GetoptError:
        print help
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print help_message
            sys.exit()
        elif opt in ("-w", "--width"):
            width = int(arg)
        elif opt in ("-t", "--height"):
            height = int(arg)
        elif opt in ("-o", "--ofile"):
            filename = arg
        elif opt in ("-n", "--num"):
            num = int(arg)
            
    picture = []
    
    for x in range(0, num):
        if num > 0:
            filename += "_" + str(num)
        random_fill(picture, width, height, filename)
        

        
def random_fill(picture, width, height, filename):
    red = 0
    green = 0
    blue = 0
    pixel = [red, green, blue]
    output = open(filename + ".ppm", "w+")
    #I'm not sure how Python handles new lines so that's why I do it separately.
    output.write("P3" + '\n')
    output.write(str(width) + " " + str(height) + '\n' + "255" + '\n')
    
    for i in range(0, width):
        picture.append([])
    for i in range(0, width):
        for j in range(0, height):
            picture[i].append(pixel)
            red = randint(0, 255)
            green = randint(0, 255)
            blue = randint(0, 255)
            picture[i][j] = [red, green, blue]
            
            output.write("%i %i %i  " % (red, green, blue))
            #output.write("%i %i %i  " % (255, 0, 0))
        output.write('\n')
        
    output.write('\n')
    output.close()


if __name__ == "__main__":
    main(sys.argv[1:])
