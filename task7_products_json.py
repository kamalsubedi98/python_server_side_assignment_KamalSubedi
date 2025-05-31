# Q (7). parse JSON file representing product details 
# (name, price, quantity) and display the details in tabular format.

import json
import os

# Sample data to create if file doesn't exist
sample_products = [
    {"name": "Laptop", "price": 1200, "quantity": 5},
    {"name": "Mouse", "price": 25, "quantity": 50},
    {"name": "Keyboard", "price": 45, "quantity": 30}
]

def create_sample_json(file_name):
    with open(file_name, 'w') as file:
        json.dump(sample_products, file, indent=2)
    print(f"'{file_name}' created with sample product data.\n")

def display_products_table(file_name):
    try:
        with open(file_name, 'r') as file:
            products = json.load(file)

        print("\n{:<15} {:<10} {:<10}".format("Product Name", "Price", "Quantity"))
        print("-" * 35)
        for product in products:
            print("{:<15} {:<10} {:<10}".format(
                product["name"], product["price"], product["quantity"]
            ))

    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Invalid JSON format.")

def main():
    file_name = "products.json"

    # Check and create file if it doesn't exist
    if not os.path.exists(file_name):
        create_sample_json(file_name)

    # Display products
    display_products_table(file_name)

# Run the program
if __name__ == "__main__":
    main()
