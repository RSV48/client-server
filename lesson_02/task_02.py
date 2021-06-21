import json


def write_order_to_json(item, quantity, price, buyer, date):
    data = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    }
    orders = {}
    with open('orders.json') as file:
        orders = json.load(file)
    if 'orders' not in orders:
        orders['orders'] = []
    orders["orders"].append(data)
    with open('orders.json', 'w') as f_n:
        json.dump(orders, f_n, sort_keys=True, indent=4, ensure_ascii=False)


write_order_to_json("Принтер", 10, 5000, "Александр", "20-06-2021")
write_order_to_json("Монитор", 10, 8000, 'ООО "Рога и копыта"', "18-06-2021")
write_order_to_json("Системный блок", 10, 12000, 'ООО "Рога и копыта"', "18-06-2021")

