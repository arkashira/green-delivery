import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class User:
    username: str
    password: str
    role: str

class UserManager:
    def __init__(self):
        self.users = {}

    def create_account(self, username: str, password: str, role: str):
        if username in self.users:
            raise ValueError("Username already exists")
        self.users[username] = User(username, password, role)

    def login(self, username: str, password: str):
        if username not in self.users:
            raise ValueError("Username does not exist")
        if self.users[username].password != password:
            raise ValueError("Incorrect password")
        return self.users[username]

    def manage_user(self, username: str, new_role: str):
        if username not in self.users:
            raise ValueError("Username does not exist")
        self.users[username].role = new_role

    def enforce_permissions(self, username: str, action: str):
        if username not in self.users:
            raise ValueError("Username does not exist")
        if self.users[username].role != "admin" and action == "manage":
            raise ValueError("Insufficient permissions")
