def main () :

    num_years = int(input("Enter how many years to check for average rainfall: "))
    months_list = ["Jan", "Feb", "Mar", "Apr", "May", "June",
                   "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
    total_inches_rain = float(0)
    total_months = num_years * 12
    for i in range(num_years) :
        year_label = i + 1
        month_incrementer = 0
        for i in range(12) :
            rain=float(input("Enter total rain for the month of {} in year {}: "
                             .format(months_list[month_incrementer], year_label)))
            month_incrementer +=1
            total_inches_rain = round((total_inches_rain + rain), 4)
    print("Total rain over a course of {} months = {} inches"
          .format(total_months, total_inches_rain))
    print("Average rainfall over the entire period =",
          round((total_inches_rain / total_months), 4), "inches")


if __name__ == '__main__': main()