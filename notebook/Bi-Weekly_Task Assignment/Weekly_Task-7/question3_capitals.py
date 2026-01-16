def capitals_manager():
    capitals = {}

    while True:
        country = input("\nEnter country name (or 'quit' to exit): ").strip().lower()
        if country == 'quit':
            print("Goodbye!")
            break

        if country in capitals:
            print(f"The capital of {country.title()} is {capitals[country]}.")
        else:
            capital = input(f"I don't know the capital of {country.title()}. Please enter it: ").strip()
            capitals[country] = capital
            print(f"Thanks, I’ve learned that the capital of {country.title()} is {capital}.")

if __name__ == "__main__":
    capitals_manager() 