from pathlib import Path

PROJECTS_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECTS_ROOT.joinpath("data")
AUTH_USERS_JSON = DATA_DIR.joinpath("users.json").resolve()
TEXT_1 = DATA_DIR.joinpath("text_1.txt").resolve()
TEXT_2 = DATA_DIR.joinpath("text_2.txt").resolve()
TEXT_3 = DATA_DIR.joinpath("text_3.txt").resolve()
HR_LINE = 40 * "-"
