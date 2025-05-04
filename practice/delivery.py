base_price=100
base_distace=10
base_weight=5
price=base_price
distance=int(input("Введите расстояние: "))
weight=int(input("Введите вес (кг): "))
isExtra=input("Срочная доставка (да/нет)")
if distance>base_distace:
    price+= (distance-base_distace)*5
if weight>base_weight:
    price+= (weight-base_weight)*20
if isExtra.lower()=="да":
    price+=price*1.5
price=round(price)
print(f"Стоимость вашей доставки{price} ")