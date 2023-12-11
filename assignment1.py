# Import necessary libraries
import datetime

# Task 1: Calculate the percentage of Birmingham and Manchester in a cities string

def calculate_percentage(cities_string):
    """
    Calculate the percentage of Birmingham and Manchester in the given cities string.
    
    Args:
        cities_string (str): A string containing city symbols.
    
    Returns:
        (float, float): Percentage of Birmingham and Manchester, rounded to 2 decimal places.
    """
    # Count the occurrences of 'B' and 'M' in the cities string
    count_birmingham = cities_string.count('B')
    count_manchester = cities_string.count('M')
    
    # Calculate the total count of cities
    total_cities = len(cities_string)
    
    # Calculate the percentage for Birmingham and Manchester
    percentage_birmingham = (count_birmingham / total_cities) * 100
    percentage_manchester = (count_manchester / total_cities) * 100
    
    # Round off the percentages to 2 decimal places
    percentage_birmingham = round(percentage_birmingham, 2)
    percentage_manchester = round(percentage_manchester, 2)
    
    return percentage_birmingham, percentage_manchester

# Task 2: Calculate the total sale based on the prices and cities string

def calculate_total_sale(cities_string):
    """
    Calculate the total sale for a given cities string based on the prices in Table 1.
    
    Args:
        cities_string (str): A string containing city symbols.
    
    Returns:
        float: Total sale rounded to 2 decimal places.
    """
    # Define the city prices in a dictionary
    city_prices = {
        'B': 29.2,
        'C': 16.6,
        'H': 34.7,
        'L': 31.7,
        'M': 38,
        'N': 19.8,
        'S': 15.2
    }
    
    # Calculate the total sale by summing the prices of cities in the cities string
    total_sale = sum(city_prices[city] for city in cities_string)
    
    return round(total_sale, 2)

# Task 3: Convert a cities string into a dictionary of city counts

def cities_to_dictionary(cities_string):
    """
    Convert a cities string into a dictionary containing the symbol and count of each city.
    
    Args:
        cities_string (str): A string containing city symbols.
    
    Returns:
        dict: A dictionary with city symbols as keys and their counts as values.
    """
    city_counts = {}
    
    # Count the occurrences of each city symbol in the cities string
    for city in cities_string:
        if city in city_counts:
            city_counts[city] += 1
        else:
            city_counts[city] = 1
    
    return city_counts

# Task 4: Record and analyze train ticket sales

def record_and_analyze_sales():
    """
    Record train ticket sales, analyze the data, and provide summary information.
    """
    # Initialize variables to store cities data and total sales
    all_cities_data = []
    total_sales = 0
    
    while True:
        cities_string = input("Enter the cities string (or type 'quit' to exit): ")
        
        if cities_string == 'quit':
            break
        
        # Check for unrecognized city symbols
        if any(city not in "BCHLMNS" for city in cities_string):
            print("Error. Unrecognized city symbol is detected. Please enter the cities string again. Acceptable list of cities symbols are B, C, H, L, M, N, and S")
            continue
        
        # Record the current date in the format YYYY-MM-DD
        current_date = datetime.date.today().strftime("%Y-%m-%d")
        
        # Save the cities string to a file named with the current date
        with open(f"{current_date}.txt", "a") as file:
            file.write(cities_string + "\n")
        
        # Update the data for analysis
        all_cities_data.append(cities_string)
        total_sales += calculate_total_sale(cities_string)
    
    # Calculate the number of tickets sold for each city and hours in which they were sold
    city_counts = {}
    hours_sold = {}
    
    for cities_string in all_cities_data:
        current_city_counts = cities_to_dictionary(cities_string)
        total_hours = 1
        
        for city, count in current_city_counts.items():
            if city in city_counts:
                city_counts[city] += 1
            else:
                city_counts[city] = 1
            
            if city in hours_sold:
                hours_sold[city] += total_hours
            else:
                hours_sold[city] = total_hours
    
    # Print the number of tickets sold for each city
    print(f"\nNumber of tickets sold for each city: {city_counts}")
    
    # Print the number of hours in which tickets of each city have been sold
    print(f"\nNumber of hours in which tickets of each city have been sold: {hours_sold}")
    
    # Print the total price of sold tickets
    print(f"\nTotal sales: £{total_sales}")

# Call the main function to start recording and analyzing sales
if __name__ == "__main__":
    record_and_analyze_sales()
