import pytest
from rest_framework import status
from rest_framework.test import APIClient


def read_list_tasks(api_client: APIClient) -> None:
    response = api_client.get('/api/tasks/')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_crud_tasks(api_client: APIClient) -> None:
    read_list_tasks(api_client)
