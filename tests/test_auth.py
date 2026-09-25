def test_register(client):
    response = client.post(
        "/register",
        json={
            "username": "testuser",
            "password": "password123"
        }
    )

    assert response.status_code == 201
    assert response.json["message"] == "User registered successfully"

def test_login(client):
    client.post(
        "/register",
        json={
            "username": "testuser",
            "password": "password123"
        }
    )

    response = client.post(
        "/login",
        json={
            "username": "testuser",
            "password": "password123"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json