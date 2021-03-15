from time import sleep

list_coffee = [
    {"name" : 'Latte', "price" : 25, 'ID' : '001'},
    {"name": 'Espresso', "price": 38, 'ID': '002'},
    {"name": 'Bombino', "price": 12, 'ID': '003'}
]
print("         Добро пожаловать!")
sleep(1)
print("Ниже вы сможете увидеть список всех кофе")
sleep(1)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
for i,products in enumerate(list_coffee, 1):
    print(
        f'\t {i}.', f'\t ID: {products["ID"]}', f'\t Название: {products["name"]}', f'\t Цена товара: {products["price"]}'
        )
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

print("Выберите кофе по ID")
product_id = input('Введите ID продукта (Latte -001, Espresso - 002, Bambino - 003): ')

for product in list_coffee:
    if product_id == product['ID']:
        text = (f'Цена за {product["name"]} составляет: {product["price"]} сом')
        print(text)
        sleep(0.5)

        client_money = int(input("Для оплаты введите банкноты в терминал: "))

        while True:
            if client_money > product['price']:
                change = client_money - product['price']
                print(f'Вы купили {product["name"]}." Спасибо!')
                print(f'Ваша сдача: {change} сомов')
                break

            elif client_money ==product['price']:
                print(f'Вы купили {product["name"]}. Наслаждайтесь!')
                break

            else:
                insuf = product['price'] - client_money
                client_money += int(input(f' Вам нужно доплатить {insuf} сом, чтобы завершить покупку: '))
                continue

