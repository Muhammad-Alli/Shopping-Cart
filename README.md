# Shopping-Cart

This is a simple interactive Python program that simulates a basic shopping cart system using a dictionary. The user can input items they want to purchase along with their prices. The program calculates and displays the total bill with a neatly formatted receipt.

## Features

- Add any number of items and prices.
- Automatically calculates the total cost which is listed with all items and their prices.
- Validates inputs to avoid incorrect pricing:
  - Items cannot be blank or just whitespace.
  - Prices must be positive numbers.
  - Handles invalid price formats (e.g. letters or symbols).
- Clean and user-friendly output.

## How to Run

Make sure you have Python installed on your machine. Then:

```bash
cd src
ShoppingCart.py
```

## Example Interaction

```
Enter the item to buy or type done if you are done shopping: Apples
Enter the price of the Apples: R12.50
Enter the item to buy or type done if you are done shopping: Bread
Enter the price of the Bread: R18.99
Enter the item to buy or type done if you are done shopping: done

Your receipt:

Apples : R12.5
Bread : R18.99

The total cost: R 31.49
```
