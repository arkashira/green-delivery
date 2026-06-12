from user import UserManager, User

def test_create_account():
    manager = UserManager()
    manager.create_account("test", "password", "user")
    assert "test" in manager.users

def test_login():
    manager = UserManager()
    manager.create_account("test", "password", "user")
    user = manager.login("test", "password")
    assert user.username == "test"

def test_manage_user():
    manager = UserManager()
    manager.create_account("test", "password", "user")
    manager.manage_user("test", "admin")
    assert manager.users["test"].role == "admin"

def test_enforce_permissions():
    manager = UserManager()
    manager.create_account("test", "password", "user")
    try:
        manager.enforce_permissions("test", "manage")
        assert False
    except ValueError as e:
        assert str(e) == "Insufficient permissions"

def test_enforce_permissions_admin():
    manager = UserManager()
    manager.create_account("test", "password", "admin")
    manager.enforce_permissions("test", "manage")
