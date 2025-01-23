def add_product_to_supplier(supplier, client, price, quantity):
    """
    Добавляет продукт поставщику, определяет его уровень сети и увеличивает
    долг перед поставщиком.

    :param supplier - поставщик, у которого был заказан продукт.
    :param client - поставщик, который заказал продукт.
    :param price - цена товара за единицу.
    :param quantity - количество продукта, которое было заказано.
    """
    # Устанавливаем уровень клиента на основе его поставщика
    if client:
        client.network_level = supplier.network_level + 1
    else:
        client.network_level = 0


