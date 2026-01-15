# Roblox Sales Project

This project helps manage sales of rare Roblox items, with inventory, platforms, and automatic fee calculations.

## Installation

1. Make sure you have Python installed (preferably via Anaconda).  
2. Install dependencies using pip:

```bash
pip install -r requirements.txt
```
4. Create the MySQL database and import the tables: platforms, items, sales.

5. Add initial data to platforms and items for testing purposes.

## Usage

Run the program with:

```bash
python main.py
```


You will see a menu with the following options:

Register Sale – enter platform, item, quantity, and price. Fees are calculated automatically.

List Items – view all items in the inventory.

List Platforms – check selling platforms and their fees.

Show Sales Report – see all sales with fees and net profit.

Note: To keep data synchronized for multiple users, everyone must connect to the same MySQL database.


