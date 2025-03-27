purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]


def total_revenue(purchases) -> int:
    total = 0
    for i in purchases:
        total += i['price'] * i['quantity']
    return total


def items_by_category(purchases) -> dict:
    result = {}
    for i in purchases:
        if i["category"] not in result:
            result[i["category"]] = []
            result[i["category"]].append(i["item"])
        else:
            if i["item"] not in result[i["category"]]:
                result[i["category"]].append(i["item"])

    return result


def expensive_purchases(purchases, min_price) -> list:
    result = []
    for i in purchases:
        if i['price'] >= min_price:
            result.append(i)
    return result


def average_price_by_category(purchases) -> dict:
    result = {}
    for i in purchases:
        if i["category"] not in result:
            result[i["category"]] = []
            result[i["category"]].append(i["price"])
        else:
            result[i["category"]].append(i["price"])

    result = {i: sum(result[i]) / len(result[i]) for i in result.keys()}

    return result


def most_frequent_category(purchases) -> str:
    result = {}
    for i in purchases:
        if i["category"] not in result:
            result[i["category"]] = []
            result[i["category"]].append(i["quantity"])
        else:
            result[i["category"]].append(i["quantity"])

    result = {i: sum(result[i]) for i in result.keys()}
    return max(result, key=result.get)


print(f"Общая выручка: {total_revenue(purchases)}")
print(f"Товары по категориям: {items_by_category(purchases)}")
min_price = int(input("Введите минмиальную цену "))
print(
    f"Покупки дороже {min_price}: {expensive_purchases(purchases, min_price)}")
print(f"Средняя цена по категориям: {average_price_by_category(purchases)}")
print(
    f"Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}")
