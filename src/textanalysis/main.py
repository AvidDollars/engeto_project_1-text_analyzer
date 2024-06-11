"""
First project - Text Analyzer

author: Dimitrij Kolničenko
email: dima.kol@seznam.cz
discord: dimitrij_kolnicenko
"""
import sys
from typing import Callable

from .constants import AUTH_USERS_JSON
from .constants import HR_LINE
from .constants import TEXT_1
from .constants import TEXT_2
from .constants import TEXT_3
from textanalysis.utils import Auth
from .utils import AuthUsersLoader
from .utils import TextAnalysis
from .utils import TextLoader
from .utils import TokenizedText


TEXTS = (TEXT_1, TEXT_2, TEXT_3)


def ask_user_for_valid_index() -> int:
    """
    Asks for valid index until a proper one is returned.
    """

    prompt = f"Enter a number btw. 1 and {len(TEXTS)} to select: "
    is_valid_index: Callable[[str], bool] = (
        lambda input_: input_.isnumeric() and 1 <= int(input_) <= len(TEXTS)
    )

    while not is_valid_index(provided := input(prompt)):
        print(f"'{provided}' is not valid index. Try again. ")

    return int(provided)


def authenticate_user() -> str:
    """
    Asks user for credentials. Returns provided username if credentials are valid,
    otherwise process will exit with status code of 1.
    """

    provided_username = input("username: ")
    provided_password = input("password: ")

    auth_users = AuthUsersLoader.from_json_file(path=AUTH_USERS_JSON)
    auth = Auth(auth_users=auth_users)

    user_has_access = auth.has_access(
        username=provided_username, password=provided_password
    )

    if not user_has_access:
        print("unregistered user, terminating the program...")
        sys.exit(1)

    return provided_username


def print_welcome_message(*, user: str) -> None:
    print(HR_LINE)
    print(f"Welcome to the app, {user}")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print(HR_LINE)


def text_analysis(*, index_of_text: int) -> TextAnalysis:
    """
    Returns results of text analysis.
    """

    text_to_analyze = TextLoader.from_plain_file(path=TEXTS[index_of_text - 1])
    tokenized_text = TokenizedText(text=text_to_analyze)
    return TextAnalysis(tokenized_text=tokenized_text)


def main() -> None:
    user = authenticate_user()
    print_welcome_message(user=user)
    index_of_text = ask_user_for_valid_index()
    text_analysis_result = text_analysis(index_of_text=index_of_text)
    print(text_analysis_result)
