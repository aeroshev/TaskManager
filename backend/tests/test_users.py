import pytest
from rest_framework import status
from rest_framework.test import APIClient


def create_user(api_client: APIClient) -> str:
    response = api_client.post('/api/users/')
    assert response.status_code == status.HTTP_201_CREATED

    return response.data['id']


def read_list_users(api_client: APIClient) -> None:
    response = api_client.get('/api/users/')
    assert response.status_code == status.HTTP_200_OK


def read_user(api_client: APIClient, user_id: str) -> None:
    response = api_client.get(f'/api/users/{user_id}/')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_crud_users(api_client: APIClient) -> None:
    user_id = create_user(api_client)
    read_list_users(api_client)
    read_user(api_client, user_id)
