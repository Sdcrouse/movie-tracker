import pytest

def test_register(client):
    response = client.get('/auth/register')

    assert response.status_code == 200
    assert b'Register here!' in response.data

    # TODO: Ensure that the user is redirected to the login page after registering

@pytest.mark.parametrize(
    ('email', 'password', 'message'),
    (
        ('', 'paswrd', b'Email is required.'),
        ('userA@gmail.com', '', b'Password is required.'),
        # TODO: Add test cases for invalid emails and passwords
        # TODO: Add a test case for a user who is already registered
    )
)
def test_register_with_invalid_input(client, email, password, message):
    response = client.post(
        '/auth/register',
        data={'email': email, 'password': password}
    )
    assert message in response.data