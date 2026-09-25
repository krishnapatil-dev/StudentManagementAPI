def test_create_course(client):
    client.post(
        "/register",
        json={
            "username": "courseuser",
            "password": "password123"
        }
    )

    login_response = client.post(
        "/login",
        json={
            "username": "courseuser",
            "password": "password123"
        }
    )

    token = login_response.json["access_token"]

    response = client.post(
        "/courses",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Python"
        }
    )

    assert response.status_code == 201
    assert response.json["course"]["name"] == "Python"


def test_get_courses(client):
    client.post(
        "/register",
        json={
            "username": "getcourseuser",
            "password": "password123"
        }
    )

    login_response = client.post(
        "/login",
        json={
            "username": "getcourseuser",
            "password": "password123"
        }
    )

    token = login_response.json["access_token"]

    client.post(
        "/courses",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Python"
        }
    )

    client.post(
        "/courses",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Flask"
        }
    )

    response = client.get(
        "/courses",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert len(response.json["courses"]) == 2
    assert response.json["courses"][0]["name"] == "Python"
    assert response.json["courses"][1]["name"] == "Flask"


def test_get_course(client):
    client.post(
        "/register",
        json={
            "username": "singlecourseuser",
            "password": "password123"
        }
    )

    login_response = client.post(
        "/login",
        json={
            "username": "singlecourseuser",
            "password": "password123"
        }
    )

    token = login_response.json["access_token"]

    course_response = client.post(
        "/courses",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Django"
        }
    )

    course_id = course_response.json["course"]["id"]

    response = client.get(
        f"/courses/{course_id}",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json["id"] == course_id
    assert response.json["name"] == "Django"