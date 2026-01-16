# --------------------------------------------
# Beckett Pizza Plaza - 4 for 3 Offer Program
# --------------------------------------------
# This program reads pizza prices from a file,
# applies the 4-for-3 discount, and displays
# the total price and discount percentage.
# Module: Foundations of Computing & Programming
# --------------------------------------------

# Import sys module to read command-line arguments
import sys

# Function to display program title
def display_title():
    print("Beckett Pizza Plaza")
    print("4-for-3 Offer")
    print("=" * 32)

# Function to read prices from file
def read_prices_from_file(filename):
    prices = []  # List to store pizza prices

    try:
        # Open the file in read mode
        with open(filename, "r") as file:
            # Read each line from the file
            for line in file:
                # Remove whitespace and newline characters
                line = line.strip()

                # Skip empty lines
                if line == "":
                    continue

                try:
                    # Convert line to float
                    price = float(line)

                    # Check if price is valid
                    if price <= 0:
                        print("Invalid price found:", line)
                        return None

                    # Add valid price to list
                    prices.append(price)

                except ValueError:
                    # Handles non-numeric values
                    print("Invalid price found:", line)
                    return None

    except FileNotFoundError:
        # File does not exist
        print("Error: File not found.")
        return None

    return prices

# Function to calculate total after discount
def calculate_total(prices):
    # Sort prices from lowest to highest
    prices.sort()

    # Cheapest pizza is free
    cheapest_price = prices[0]

    # Total price without discount
    original_total = sum(prices)

    # Total after removing cheapest pizza
    discounted_total = original_total - cheapest_price

    return original_total, discounted_total, cheapest_price

# Function to calculate discount percentage
def calculate_discount(original_total, discounted_total):
    # Calculate discount amount
    discount_amount = original_total - discounted_total

    # Calculate discount percentage
    discount_percentage = (discount_amount / original_total) * 100

    # Return rounded discount percentage
    return round(discount_percentage)

# Main function
def main():
    # Check if filename is provided
    if len(sys.argv) < 2:
        print("Usage: python pizza_offer.py <filename>")
        return

    # Get filename from command-line argument
    filename = sys.argv[1]

    # Display title
    display_title()

    # Read prices from file
    prices = read_prices_from_file(filename)

    # Check if prices were read successfully
    if prices is None:
        print("Failed to process order.")
        return

    # Check for exactly four pizzas
    if len(prices) != 4:
        print("Error: Exactly four pizza prices are required.")
        return

    # Calculate totals
    original_total, discounted_total, cheapest = calculate_total(prices)

    # Calculate discount percentage
    discount_percentage = calculate_discount(original_total, discounted_total)

    # Display results
    print(f"Original Total: £{original_total:.2f}")
    print(f"Cheapest Pizza Free: £{cheapest:.2f}")
    print(f"Order Total is £{discounted_total:.2f}, a fabulous discount of {discount_percentage}%!")

# Run the program
if __name__ == "__main__":
    main() 