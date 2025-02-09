from products.models import Product
from suppliers.models import Supplier


def is_purchase_valid(client, supplier):
    """
    Проверяет, что поставщик-клиент, находится ниже по
    уровню иерархии поставщика или равен ему.
    """

    if client.hierarchy_level >= supplier.hierarchy_level:
        return True
    return False


def add_product_to_supplier(client_id, supplier_id, product_id, quantity):
    """
    Добавляет продукт поставщику-клиенту, и увеличивает его долг перед
    поставщиком у которого закупает товар.

    :param client_id - id поставщика, который заказал продукт.
    :param supplier_id - id поставщика, у которого был заказан продукт.
    :param product_id - id продута, который закупает поставщик.
    :param quantity - количество продукта, которое было заказано.
    """

    client = Supplier.objects.get(id=client_id)
    supplier = Supplier.objects.get(id=supplier_id)
    product = Product.objects.get(id=product_id)

    if not is_purchase_valid(client, supplier):
        raise ValueError(
            'Невозможно закупить товар у поставщика, так как его уровень'
            'иерархии ниже вашего.')

    if not supplier.products.filter(id=product_id).exists():
        raise ValueError(
            'У поставщика нет этого продукта.')

    product.supplier.add(client)

    purchase_sum = product.price * quantity
    client.debt += purchase_sum
    client.save()
    return product
