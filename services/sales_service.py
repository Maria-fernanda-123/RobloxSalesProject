from db.connection import get_connection
from services.platform_service import get_platform_by_id

def register_sale():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    platforms = list_platforms()
    print("\nPlatforms:")
    for p in platforms:
        print(f"{p['platform_id']} - {p['name']} (Selling Fee: {p['selling_fee']*100}%, Withdrawal Fee: {p['withdrawal_fee']*100}%)")

    platform_id = int(input("Platform ID: "))
    platform = get_platform_by_id(platform_id)
    if not platform:
        print("Invalid platform ID.")
        cursor.close()
        conn.close()
        return

    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    print("\nItems:")
    for i in items:
        print(f"{i['item_id']} - {i['name']} (Stock: {i['quantity']}, Sale price: {i['sale_price']})")

    item_id = int(input("Item ID: "))
    cursor.execute("SELECT * FROM items WHERE item_id=%s", (item_id,))
    item = cursor.fetchone()
    if not item:
        print("Invalid item ID.")
        cursor.close()
        conn.close()
        return

    quantity = int(input(f"Quantity sold (Available: {item['quantity']}): "))
    if quantity <= 0 or quantity > item['quantity']:
        print(f"Invalid quantity. Available stock: {item['quantity']}")
        cursor.close()
        conn.close()
        return


    description = input("Sale description: ")

    unit_price = float(input(f"Unit price (default {item['sale_price']}): ") or item['sale_price'])

    total_sale = unit_price * quantity
    selling_fee_amount = total_sale * platform['selling_fee']
    withdrawal_fee_amount = total_sale * platform['withdrawal_fee']
    net_after_platform = total_sale - selling_fee_amount - withdrawal_fee_amount

    cursor.execute("""
        INSERT INTO sales (platform_id, item_id, description, quantity, unit_price, total_sale, 
                           selling_fee_amount, withdrawal_fee_amount, net_after_platform, sale_date)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,CURDATE())
    """, (platform_id, item_id, description, quantity, unit_price, total_sale,
          selling_fee_amount, withdrawal_fee_amount, net_after_platform))

    new_quantity = item['quantity'] - quantity
    cursor.execute("UPDATE items SET quantity=%s WHERE item_id=%s", (new_quantity, item_id))

    conn.commit()
    print(f"\nSale registered! Total: ${total_sale:.2f}, Net after fees: ${net_after_platform:.2f}")
    cursor.close()
    conn.close()

def list_items():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    print("\nItems:")
    for i in items:
        print(f"{i['item_id']} - {i['name']} | Stock: {i['quantity']} | Sale price: {i['sale_price']}")
    cursor.close()
    conn.close()

def show_sales_report():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT s.sale_id, p.name AS platform, i.name AS item, s.description, s.quantity, s.total_sale,
               s.selling_fee_amount, s.withdrawal_fee_amount, s.net_after_platform, s.sale_date
        FROM sales s
        LEFT JOIN platforms p ON s.platform_id = p.platform_id
        LEFT JOIN items i ON s.item_id = i.item_id
        ORDER BY s.sale_id
    """)
    sales = cursor.fetchall()
    print("\nSales Report:")
    for s in sales:
        print(f"{s['sale_id']} | {s['platform']} | {s['item']} | Qty: {s['quantity']} | Total: ${s['total_sale']:.2f} | Net: ${s['net_after_platform']:.2f} | Date: {s['sale_date']}")
    cursor.close()
    conn.close()
