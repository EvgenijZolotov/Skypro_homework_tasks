# test_projects.py

import pytest
from api_client.project_page import ProjectAPI

api = ProjectAPI()


@pytest.fixture(scope="module")
def created_project():
    """Фикстура: создаёт проект и возвращает его ID"""
    response = api.create_project("Test Project")
    assert response.status_code == 200
    return response.json()["id"]

# === Позитивные тесты ===


def test_create_project_positive():
    response = api.create_project("Another Project")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Another Project"


def test_get_project_positive(created_project):
    response = api.get_project(created_project)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == created_project


def test_update_project_positive(created_project):
    new_name = "Updated Name"
    response = api.update_project(created_project, new_name)
    assert response.status_code == 200
    assert response.json()["name"] == new_name

# === Негативные тесты ===


def test_create_project_negative_missing_name():
    # Принудительно передаем пустое тело
    response = api.create_project(name=None)
    assert response.status_code in (400, 422)


def test_get_project_negative_invalid_id():
    response = api.get_project("invalid-id-123")
    assert response.status_code == 404


def test_update_project_negative_invalid_id():
    response = api.update_project("invalid-id-123", "Name")
    assert response.status_code == 404
