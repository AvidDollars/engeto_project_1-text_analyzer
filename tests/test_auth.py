from pathlib import Path

from utils import AuthUsersLoader


def test_loading_data_from_dict():
    input_data = {"jimi": "123", "johnny": "abc"}
    auth_users = AuthUsersLoader(auth_users=input_data)
    assert input_data == auth_users.data


def test_loading_data_from_json_file():
    data_path = Path(__file__).parent.joinpath("users.json")
    expected_data = {"jimi": "123", "johnny": "abc"}
    loaded_data = AuthUsersLoader.from_json_file(path=data_path)
    assert expected_data == loaded_data.data
