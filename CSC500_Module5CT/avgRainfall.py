def main () :

    #num_years variable used later in outer for loop
    num_years = int(input("Enter how many years to check for average rainfall: "))
    print()
    #List structure to store month names.
    months_list = ["Jan", "Feb", "Mar", "Apr", "May", "June",
                   "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
    #total_inches_rain updated later in the inner for loop
    total_inches_rain = float(0)
    #since program only asks for number of years, months = years * 12
    total_months = num_years * 12
    #outer loop
    for i in range(num_years) :
        #year_label used later in input prompt
        year_label = i + 1
        #month_incrementer used to increment position of months_list
        month_incrementer = 0
        #inner loop
        for i in range(12) :
            #store month_rain value based on user input
            month_rain=float(input("Enter total rain for the month of {} in year {}: "
                             .format(months_list[month_incrementer], year_label)))
            month_incrementer +=1
            #add month_rain to current value of total_inches_rain, round to 4 decimal places
            total_inches_rain = round((total_inches_rain + month_rain), 4)
    #print total inches of rain over total_months
    print("\nTotal rain over a course of {} months = {} inches"
          .format(total_months, total_inches_rain))
    #calculate average, format and print output.
    print("Average monthly rainfall over the entire period =",
          round((total_inches_rain / total_months), 4), "inches")


if __name__ == '__main__': main()