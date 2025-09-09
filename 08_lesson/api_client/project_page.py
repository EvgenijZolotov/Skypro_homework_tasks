# api_client/project_page.py

import requests
from config import API_BASE_URL, API_TOKEN


class ProjectAPI:
    def __init__(self):
        self.base_url = f"{API_BASE_URL}/api-v2/projects"
        self.headers = {
            "Authorization": f"Bearer {API_TOKEN}",
            "Content-Type": "application/json"
        }

    def create_project(self, name):
        payload = {"name": name}
        response = requests.post(
            self.base_url, json=payload, headers=self.headers
            )
        return response

    def get_project(self, project_id):
        url = f"{self.base_url}/{project_id}"
        return requests.get(url, headers=self.headers)

    def update_project(self, project_id, new_name):
        payload = {"name": new_name}
        url = f"{self.base_url}/{project_id}"
        return requests.put(url, json=payload, headers=self.headers)
