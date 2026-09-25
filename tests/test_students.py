def test_create_student(client):
    client.post(
        "/register",
        json={
            "username": "studentuser",
            "password": "password123"
        }
    )

    login_response = client.post(
        "/login",
        json={
            "username": "studentuser",
            "password": "password123"
        }
    )

    token = login_response.json["access_token"]

    client.post(
        "/courses",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "name": "Python",
        }
    )

    response = client.post(
        "/students",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "name": "Joy",
            "age": 22,
            "course_id": 1,
            "email": "joy@test.com",
            "marks": 45
        }
    )

    assert response.status_code == 201
    assert response.json["student"]["name"] == "Joy"

def test_get_student(client):
    client.post(
        "/register",
        json={
            "username": "testuser",
            "password": "password123"
        }
    )

    login_response = client.post(
        "/login",
        json={
            "username": "testuser",
            "password": "password123"
        }
    )

    token = login_response.json["access_token"]

    client.post(
        "/courses",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "name": "Flask",
        }
    )

    student_response = client.post(
        "/students",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "name": "Aman",
            "age": 21,
            "course_id": 1,
            "email": "aman@test.com",
            "marks": 65
        }
    )

    student_id = student_response.json["student"]["id"]

    response = client.get(
        f"/students/{student_id}",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200
    assert response.json["name"] == "Aman"
    assert response.json["marks"] == 65

def test_get_students(client):
    client.post(
        "/register",
        json={
            "username": "listuser",
            "password": "password123"
        }
    )

    login_response = client.post(
        "/login",
        json={
            "username": "listuser",
            "password": "password123"
        }
    )

    token = login_response.json["access_token"]

    client.post(
        "/courses",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "name": "Python"
        }
    )

    client.post(
        "/students",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "name": "Rahul",
            "age": 21,
            "course_id": 1,
            "email": "rahul2@test.com",
            "marks": 85
        }
    )

    response = client.get(
        "/students",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200
    assert len(response.json["students"]) == 1
    assert response.json["students"][0]["name"] == "Rahul"

def test_search_students(client):
    client.post(
        "/register",
        json={
            "username": "searchuser",
            "password": "password123"
        }
    )

    login_response = client.post(
        "/login",
        json={
            "username": "searchuser",
            "password": "password123"
        }
    )

    token = login_response.json["access_token"]

    client.post(
        "/courses",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "name": "Python"
        }
    )

    client.post(
        "/students",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "name": "Rohit",
            "age": 22,
            "course_id": 1,
            "email": "rohit@test.com",
            "marks": 88
        }
    )

    response = client.get(
        "/students/search?keyword=Rohit",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200
    assert response.json["keyword"] == "Rohit"
    assert len(response.json["students"]) == 1
    assert response.json["students"][0]["name"] == "Rohit"

def test_students_pagination_and_course_filter(client):
    client.post(
        "/register",
        json={
            "username": "filteruser",
            "password": "password123"
        }
    )

    login_response = client.post(
        "/login",
        json={
            "username": "filteruser",
            "password": "password123"
        }
    )

    token = login_response.json["access_token"]

    # Create two courses
    client.post(
        "/courses",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": "Python"}
    )

    client.post(
        "/courses",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": "Flask"}
    )

    # Create students
    client.post(
        "/students",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Rahul",
            "age": 21,
            "course_id": 1,
            "email": "rahul3@test.com",
            "marks": 85
        }
    )

    client.post(
        "/students",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Aman",
            "age": 22,
            "course_id": 2,
            "email": "aman2@test.com",
            "marks": 90
        }
    )

    # Pagination
    response = client.get(
        "/students?page=1&limit=1",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json["page"] == 1
    assert response.json["limit"] == 1
    assert len(response.json["students"]) == 1

    # Course filter
    response = client.get(
        "/students?course_id=2",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert len(response.json["students"]) == 1
    assert response.json["students"][0]["name"] == "Aman"

def test_update_student(client):
    client.post(
        "/register",
        json={
            "username": "updateuser",
            "password": "password123"
        }
    )

    login_response = client.post(
        "/login",
        json={
            "username": "updateuser",
            "password": "password123"
        }
    )

    token = login_response.json["access_token"]

    # Create course
    client.post(
        "/courses",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": "Python"}
    )

    # Create student
    student_response = client.post(
        "/students",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Rahul",
            "age": 21,
            "course_id": 1,
            "email": "rahul_update@test.com",
            "marks": 80
        }
    )

    student_id = student_response.json["student"]["id"]

    # Update student
    response = client.put(
        f"/students/{student_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Rahul Patil",
            "age": 22,
            "course_id": 1,
            "email": "rahul_update@test.com",
            "marks": 95
        }
    )

    assert response.status_code == 200
    assert response.json["student"]["name"] == "Rahul Patil"
    assert response.json["student"]["age"] == 22
    assert response.json["student"]["marks"] == 95

def test_delete_student(client):
    client.post(
        "/register",
        json={
            "username": "deleteuser",
            "password": "password123"
        }
    )

    login_response = client.post(
        "/login",
        json={
            "username": "deleteuser",
            "password": "password123"
        }
    )

    token = login_response.json["access_token"]

    # Create course
    client.post(
        "/courses",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": "Python"}
    )

    # Create student
    student_response = client.post(
        "/students",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Delete Me",
            "age": 21,
            "course_id": 1,
            "email": "delete@test.com",
            "marks": 75
        }
    )

    student_id = student_response.json["student"]["id"]

    # Delete student
    response = client.delete(
        f"/students/{student_id}",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json["message"] == "Student deleted successfully."