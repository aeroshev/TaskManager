import pytest
from rest_framewok.test import APIClient

from core.models.users import User

TEST_USERNAME = 'user'


@pytest.fixture
def mock_user() -> User:
    user, _ = User.objects.get_or_create(username=TEST_USERNAME)
    return user


@pytest.fixture
def api_client(mock_user: User) -> APIClient:
    client = APIClient()
    client.login(remote_user=mock_user.username)
    client.force_authenticate(user=mock_user)
    return client
