def main () :

    #num_books purchased will determine points awarded
    num_books = int(input("Enter the number of books purchased this month : "))
    #points variable to store number of points
    points = 0
    #Print number of points awarded based on user input
    if num_books < 2 :
        points = 0
    elif num_books >=2 and num_books < 4 :
        points = 5
    elif num_books >=4 and num_books < 6 :
        points = 15
    elif num_books >=6 and num_books < 8 :
        points = 30
    elif num_books >= 8 :
        points = 60
    #print points earned
    print("You have earned {} book club points".format(points))

if __name__ == '__main__': main()