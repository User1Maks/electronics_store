import pytest
from django.urls import reverse
from rest_framework import status

from suppliers.models import Supplier


@pytest.mark.django_db
def test_supplier_anonymous_user_permissions(auth_user_2, supplier_plant):
    """Тест на доступ не активному пользователю к CRUD модели поставщика."""

    create_url = reverse('suppliers:supplier_create')
    response_create = auth_user_2.post(create_url)
    assert response_create.status_code == status.HTTP_403_FORBIDDEN

    list_url = reverse('suppliers:supplier_list')
    response_list = auth_user_2.get(list_url)
    assert response_list.status_code == status.HTTP_403_FORBIDDEN

    detail_url = reverse('suppliers:supplier_detail',
                         args=[supplier_plant.id])
    response_detail = auth_user_2.get(detail_url)
    assert response_detail.status_code == status.HTTP_403_FORBIDDEN

    update_url = reverse('suppliers:supplier_update',
                         args=[supplier_plant.id])
    response_update = auth_user_2.patch(update_url)
    assert response_update.status_code == status.HTTP_403_FORBIDDEN

    delete_url = reverse('suppliers:supplier_delete',
                         args=[supplier_plant.id])
    response_delete = auth_user_2.delete(delete_url)
    assert response_delete.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_supplier_create(auth_user):
    """Тест на создание поставщика активным пользователем."""

    url = reverse('suppliers:supplier_create')
    data = {
        'network_name': 'Test title 1',
        'hierarchy_level': 0
    }
    response = auth_user.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED

    assert response.data['network_name'] == data['network_name']
    assert response.data['hierarchy_level'] == data['hierarchy_level']
    assert Supplier.objects.count() == 1


@pytest.mark.django_db
def test_list_suppliers(auth_user, supplier_plant):
    """Тест на просмотр списка поставщиков активным пользователем."""
    url = reverse('suppliers:supplier_list')
    response = auth_user.get(url)
    assert response.status_code == status.HTTP_200_OK
    response_list_data = response.json()
    assert len(response_list_data['results']) == 1


@pytest.mark.django_db
def test_detail_supplier(auth_user, supplier_plant, contacts_supplier_plant):
    """
    Тест на просмотр информации о поставщике и его контактов
    активным пользователем.
    """
    url = reverse('suppliers:supplier_detail',
                  args=[supplier_plant.id])
    response = auth_user.get(url)
    assert response.status_code == status.HTTP_200_OK

    response_data = response.json()
    assert response_data['network_name'] == supplier_plant.network_name
    assert response_data['hierarchy_level'] == supplier_plant.hierarchy_level

    contacts_data = response_data['contacts']
    assert contacts_data['email'] == contacts_supplier_plant.email
    assert contacts_data['country'] == contacts_supplier_plant.country
    assert contacts_data['city'] == contacts_supplier_plant.city
    assert contacts_data['street'] == contacts_supplier_plant.street
    assert contacts_data['house_number'] == contacts_supplier_plant.house_number
    assert contacts_data['phone'] == contacts_supplier_plant.phone


@pytest.mark.django_db
def test_update_supplier(auth_user, supplier_plant, contacts_supplier_plant):
    """Фикстура обновления поставщика и его контактов активным пользователем."""

    url = reverse('suppliers:supplier_update',
                  args=[supplier_plant.id])
    new_data = {
        'network_name': 'New title',
        'contacts': {
            'email': 'new@example.com',
            'country': 'USA',
            'city': 'Los Angeles',
            'street': 'Wilshire Boulevard',
            'house_number': '707',
            'phone': '+1 (310) 555-1234'
        }
    }
    response = auth_user.patch(url, new_data, format='json')
    assert response.status_code == status.HTTP_200_OK

    supplier_plant.refresh_from_db()
    assert supplier_plant.network_name == new_data['network_name']

    contacts_supplier_plant.refresh_from_db()
    assert contacts_supplier_plant.email == new_data['contacts'][
        'email']
    assert contacts_supplier_plant.country == new_data['contacts'][
        'country']
    assert contacts_supplier_plant.city == new_data['contacts']['city']
    assert contacts_supplier_plant.street == new_data['contacts'][
        'street']
    assert contacts_supplier_plant.house_number == new_data['contacts'][
        'house_number']
    assert contacts_supplier_plant.phone == new_data['contacts'][
        'phone']


@pytest.mark.django_db
def test_delete_supplier(auth_user, supplier_plant):
    """Тест на удаление поставщика активным пользователем."""
    url = reverse('suppliers:supplier_delete', args=[supplier_plant.id])
    response = auth_user.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Supplier.objects.filter(id=supplier_plant.id).exists()
    assert Supplier.objects.count() == 0


@pytest.mark.django_db
def test_add_products_to_supplier(auth_user, supplier_plant,
                                  supplier_retail_network, product):
    """
    Тест на добавление активным пользователем товаров поставщику-клиенту от
    другого поставщика. Также проверяет увеличение долго поставщика-клиента.
    """
    url = reverse('suppliers:add_product')
    data = {
        'client_id': supplier_retail_network.id,
        'supplier_id': supplier_plant.id,
        'product_id': product.id,
        'quantity': 10
    }

    initial_debt = supplier_retail_network.debt

    response = auth_user.post(url, data=data)

    assert response.status_code == status.HTTP_200_OK
    expected_debt_increase = product.price * data['quantity']

    supplier_retail_network.refresh_from_db()
    assert supplier_retail_network.debt == initial_debt + expected_debt_increase
