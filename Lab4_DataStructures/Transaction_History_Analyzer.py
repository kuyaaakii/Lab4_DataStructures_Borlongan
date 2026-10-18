from constants import *
from collections import defaultdict

# Generate five customers using LAST_NAME
customer_names = [c.upper() for c in LAST_NAME[0:5]]
customers = ["C1", "C2", "C3", "C4", "C5"]

# Assign fixed prices to the products
products = ["notebook", "pen", "usb", "headphones", "calculator"]

product_prices = {
    "notebook": 35,
    "pen": 15,
    "usb": 350,
    "headphones": 650,
    "calculator": 250
}

# Generate transaction records
T1, T2, T3, T4, T5 = {}, {}, {}, {}, {}
T6, T7, T8, T9, T10 = {}, {}, {}, {}, {}
T11, T12, T13, T14, T15 = {}, {}, {}, {}, {}

transactions = [
    T1, T2, T3, T4, T5,
    T6, T7, T8, T9, T10,
    T11, T12, T13, T14, T15
]

transaction_plan = [
    ("C1", "notebook"),
    ("C2", "pen"),
    ("C3", "usb"),
    ("C1", "notebook"),
    ("C4", "headphones"),
    ("C5", "calculator"),
    ("C2", "notebook"),
    ("C3", "pen"),
    ("C4", "usb"),
    ("C5", "headphones"),
    ("C1", "pen"),
    ("C2", "usb"),
    ("C3", "calculator"),
    ("C4", "notebook"),
    ("C5", "pen")
]

# Generate quantities using SEED_NUM and FAVORITE_ARTIST
for n in range(len(transactions)):
    letter = FAVORITE_ARTIST[n % len(FAVORITE_ARTIST)].lower()
    letter_position = ord(letter) - 96

    transactions[n]["transaction_id"] = f"T{n + 1}"
    transactions[n]["customer"] = transaction_plan[n][0]
    transactions[n]["customer_name"] = customer_names[
        customers.index(transaction_plan[n][0])
    ]
    transactions[n]["product"] = transaction_plan[n][1]
    transactions[n]["quantity"] = (SEED_NUM + letter_position) % 5 + 1
    transactions[n]["price"] = product_prices[transaction_plan[n][1]]
    transactions[n]["value"] = (
        transactions[n]["quantity"] * transactions[n]["price"]
    )

# Print generated transaction records
print("=" * 30, "GENERATED TRANSACTION RECORDS", "=" * 30)

for t in transactions:
    print(f"Transaction: {t['transaction_id']}")
    print(f"Customer: {t['customer']} - {t['customer_name']}")
    print(f"Product: {t['product']}")
    print(f"Quantity: {t['quantity']}")
    print(f"Price: PHP {t['price']}")
    print(f"Transaction Value: PHP {t['value']}")
    print("-" * 30)


# Organize records by customer and product
organized_transactions = defaultdict(lambda: defaultdict(list))

for t in transactions:
    customer = t["customer"]
    product = t["product"]

    organized_transactions[customer][product].append(t)


# Identify repeated purchases and distinct customers/products
purchase_counts = defaultdict(int)
distinct_customers = set()
distinct_products = set()

for t in transactions:
    key = (t["customer"], t["product"])
    purchase_counts[key] += 1
    distinct_customers.add(t["customer"])
    distinct_products.add(t["product"])

print("=" * 30, "REPEATED AND DISTINCT RECORDS", "=" * 30)
print(f"Distinct Customers: {len(distinct_customers)}")
print(f"Distinct Products: {len(distinct_products)}")

for key, count in purchase_counts.items():
    if count > 1:
        print(f"Repeated Purchase: {key[0]} bought {key[1]} {count} times")


# Determine customer summaries
customer_summary = defaultdict(lambda: {
    "transactions": 0,
    "quantity": 0,
    "total": 0
})

for t in transactions:
    customer = t["customer"]

    customer_summary[customer]["transactions"] += 1
    customer_summary[customer]["quantity"] += t["quantity"]
    customer_summary[customer]["total"] += t["value"]

print("=" * 30, "CUSTOMER SUMMARIES", "=" * 30)

for customer, info in sorted(customer_summary.items()):
    print(f"Customer: {customer}")
    print(f"Transactions: {info['transactions']}")
    print(f"Total Items: {info['quantity']}")
    print(f"Total Spending: PHP {info['total']}")
    print("-" * 30)


# Determine product summaries
product_summary = defaultdict(lambda: {
    "transactions": 0,
    "quantity": 0,
    "total": 0
})

for t in transactions:
    product = t["product"]

    product_summary[product]["transactions"] += 1
    product_summary[product]["quantity"] += t["quantity"]
    product_summary[product]["total"] += t["value"]

print("=" * 30, "PRODUCT SUMMARIES", "=" * 30)

for product, info in sorted(product_summary.items()):
    print(f"Product: {product}")
    print(f"Transactions: {info['transactions']}")
    print(f"Units Sold: {info['quantity']}")
    print(f"Total Sales: PHP {info['total']}")
    print("-" * 30)


# Arrange records by customer and product
ordered_transactions = sorted(
    transactions,
    key=lambda t: (t["customer"], t["product"])
)

print("=" * 30, "ORDERED TRANSACTION RECORDS", "=" * 30)

for t in ordered_transactions:
    print(
        f"{t['transaction_id']} | "
        f"{t['customer']} | "
        f"{t['product']} | "
        f"Quantity: {t['quantity']} | "
        f"Value: PHP {t['value']}"
    )


# Consolidated transaction report
total_value = 0
total_quantity = 0

for t in transactions:
    total_value += t["value"]
    total_quantity += t["quantity"]

print("=" * 30, "CONSOLIDATED TRANSACTION REPORT", "=" * 30)
print(f"Total Transactions: {len(transactions)}")
print(f"Distinct Customers: {len(distinct_customers)}")
print(f"Distinct Products: {len(distinct_products)}")
print(f"Total Quantity Sold: {total_quantity}")
print(f"Overall Transaction Value: PHP {total_value}")
print(f"Repeated Customer-Product Pairs: {sum(1 for count in purchase_counts.values() if count > 1)}")
