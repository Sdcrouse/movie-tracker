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
        # TODO: Add test cases for invalid passwords
        # TODO: Add a test case for a user who is already registered
    )
)
def test_register_with_invalid_input(client, email, password, message):
    response = client.post(
        '/auth/register',
        data={'email': email, 'password': password}
    )
    assert message in response.data

@pytest.mark.parametrize('email', [
    'abc123',
    'abc@',
    'abc@gmail.',
    'abc@gmail.c',
    '@yahoo.com',
    'user@.com',
    'abc@123@example.com',
    'example.email@google.c0m'
])
def test_register_with_invalid_emails(client, email):
    response = client.post(
        '/auth/register',
        data={'email': email, 'password': 'p@ssW0rd'}
    )

    assert b'Invalid email address.' in response.data

# TODO: Add a test case for valid emails