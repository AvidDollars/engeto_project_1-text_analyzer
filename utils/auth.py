import hashlib
import json
from pathlib import Path

from typing_extensions import Self


class AuthUsersLoader:
    """
    Class for loading authenticated users from a data source.
    For each new data source you must implement classmethod that
    returns an instance of the class.
    """

    def __init__(self, *, auth_users: dict[str, str]) -> None:
        self.data = auth_users

    @classmethod
    def from_json_file(cls, *, path: Path) -> Self:
        """
        Loads a JSON file based on provided path argument and
        returns class instance with the data from loaded file.
        """

        with open(path, mode="r", encoding="utf-8") as auth_users:
            loaded_auth_users: dict[str, str] = json.load(auth_users)
            return cls(auth_users=loaded_auth_users)

    @classmethod
    def from_db(cls, *, db_uri: str) -> Self:  # dead: disable
        raise NotImplementedError("import from db file not implemented")


class Auth:
    """
    Class for user authentication.
    Authentication is done based on comparison against loaded
    data source by "AuthUsersLoader" class instance.
    """

    def __init__(self, *, auth_users: AuthUsersLoader) -> None:
        self.auth_users = auth_users.data

    @classmethod
    def hash(cls, *, text: str) -> str:
        """
        Returns sha256 hash of provided input.
        """

        return hashlib.sha256(bytes(text, encoding="utf-8")).hexdigest()

    def has_access(self, *, username: str, password: str) -> bool:
        """
        Compares provided "username" and "password" arguments agains loaded
        data source containing user credentials. "password" argument is hashed
        with sha256 algorithm and then compared with a hash from a data source.
        """

        provied_password = self.hash(text=password)
        from_db_password = self.auth_users.get(username)

        if from_db_password is None or provied_password != from_db_password:
            return False
        return True
