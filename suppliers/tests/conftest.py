import pytest
from rest_framework.test import APIClient

from contacts.models import Contact
from products.models import Product
from suppliers.models import Supplier
from users.models import User


@pytest.fixture
def api_client():
    """Фикстура клиента."""
    return APIClient()


@pytest.fixture
def user():
    """Фикстура активного пользователя."""
    user = User.objects.create(
        username='User',
        email='testuser@example.com',
        password='test-password',
        first_name='User',
        last_name='Testov',
        phone='+7-900-000-00-01'
    )
    user.is_active = True
    user.save()
    return user


@pytest.fixture
def user_2():
    """Фикстура не активного пользователя."""
    user_2 = User.objects.create(
        username='User_2',
        email='test_2_user@example.com',
        password='test-2-password',
        first_name='User_2',
        last_name='Testov_2',
        phone='+7-900-000-00-02'
    )
    user_2.is_active = False
    user_2.save()
    return user_2


@pytest.fixture
def supplier_plant():
    """Фикстура завод-поставщик."""
    supplier = Supplier.objects.create(
        network_name='Завод',
        hierarchy_level=0
    )
    return supplier


@pytest.fixture
def contacts_supplier_plant(supplier_plant):
    """Фикстура контактов завода-поставщика."""
    contacts = Contact.objects.create(
        supplier=supplier_plant,
        email='zavod@example.com',
        country='Russia',
        city='Moscow',
        street='Tverskaya',
        house_number='15 A',
        phone='+7-900-000-00-10'
    )
    return contacts


@pytest.fixture
def supplier_retail_network(supplier_plant):
    """Фикстура поставщик-розничная сеть."""
    supplier = Supplier.objects.create(
        network_name='Розничная сеть',
        hierarchy_level=1,
        supplier=supplier_plant
    )

    Contact.objects.create(
        supplier=supplier,
        email='network@example.com',
        country='Russia',
        city='Vladimir',
        street='Moskovskaya',
        house_number='1 д',
        phone='+7-900-000-00-45'
    )

    return supplier


@pytest.fixture
def supplier_individual_entrepreneur(supplier_retail_network):
    """Фикстура поставщик-индивидуальный предприниматель."""
    supplier = Supplier.objects.create(
        network_name='Индивидуальный предприниматель',
        hierarchy_level=2,
        supplier=supplier_retail_network.id
    )
    Contact.objects.create(
        supplier=supplier,
        email='Petrov@exemple.com',
        country='Russia',
        city='Kovrov',
        street='Pushkin',
        house_number='10',
        phone='+7-900-000-00-15'
    )
    return supplier


@pytest.fixture
def product(user, supplier_plant):
    """Фикстура продукта."""
    product = Product.objects.create(
        title='test-product',
        model='testovay',
        price=53000.00
    )
    product.supplier.set([supplier_plant])
    return product


@pytest.fixture
def auth_user(api_client, user):
    """Фикстура активного пользователя."""
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def auth_user_2(api_client, user_2):
    """Фикстура не активного пользователя."""
    api_client.force_authenticate(user=user_2)
    return api_client
