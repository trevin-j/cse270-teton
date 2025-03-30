import pytest
import requests

URL = "http://127.0.0.1:8000/users"
TIMEOUT = 5


def test_user_api_401(mocker):
    params = {"username": "admin", "password": "admin"}

    mocked_response = mocker.Mock()
    mocked_response.status_code = 401
    mocked_response.text = ""

    mocker.patch("requests.get", return_value=mocked_response)

    response = requests.get(URL, params=params, timeout=TIMEOUT)

    assert response.status_code == 401
    assert response.text.strip() == ""


def test_user_api_200(mocker):
    params = {"username": "admin", "password": "qwerty"}

    mocked_response = mocker.Mock()
    mocked_response.status_code = 200
    mocked_response.text = ""

    mocker.patch("requests.get", return_value=mocked_response)

    response = requests.get(URL, params=params, timeout=TIMEOUT)

    assert response.status_code == 200
    assert response.text.strip() == ""
