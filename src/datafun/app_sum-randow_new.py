"""src/datafun/app_case.py - Project script (example).

Author: Denise Case
Date: 2026-04

  Practice key Python skills related to:
    - imports
    - logging
    - pathlib for cross-platform file paths
    - type hints
    - global constants with Final
    - functions
    - repetition patterns:
        - for loop over a numeric range
        - for loop over a list
        - list comprehension
        - while loop with a counter
    - main function
    - conditional execution guard

  Terminal command to run this file from the root project folder:

    uv run python -m datafun.app_sum-randow_new

OBS:
  Don't edit this file - it should remain a working example.
  Copy it, rename it, and modify your copy.
"""

# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging
from pathlib import Path
from typing import Final

from datafun_toolkit.logger import get_logger, log_header

# === CONFIGURE LOGGER ONCE PER MODULE (PYTHON FILE) ===

LOG: logging.Logger = get_logger("P02", level="INFO")

# === DECLARE GLOBAL CONSTANTS ===

ROOT_DIR: Final[Path] = Path.cwd()
DATA_DIR: Final[Path] = ROOT_DIR / "data"
PROCESSED_DIR: Final[Path] = DATA_DIR / "processed"

New_Teacher_LIST: Final[list[str]] = [
    "Grading",
    "Parent_Contact_Log",
    "PLC",
    "Extra_Duties",
]

# === DECLARE A HELPER FUNCTION TO WRITE A FILE ===


def write_text_file(*, path: Path, content: str) -> None:
    """Write content to a text file, creating parent directories as needed.

    Arguments:
        path: Full path to the file to create or overwrite.
        content: Text content to write.

    Returns:
        None
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    LOG.info(f"Wrote file: {path.name}")


# === DECLARE REPETITION FUNCTION 2: FOR LOOP OVER A LIST ===


def create_files_from_list() -> None:
    """Create one text file per item in a list using a for loop.

    WHY: Use a for loop over a list when repeating logic for each item.
    The loop variable takes on each value in the list, one at a time.

    Arguments: None
    Returns: None
    """
    LOG.info("========================")
    LOG.info("FUNCTION 2: for loop over a list")
    LOG.info("========================")

    LOG.info(f"New Teacher List: {New_Teacher_LIST}")

    for new_teacher_name in New_Teacher_LIST:
        filename: str = f"a_{new_teacher_name}.txt"
        path: Path = PROCESSED_DIR / filename
        content: str = f"Data for: '{new_teacher_name}'\n"
        write_text_file(path=path, content=content)


# === DECLARE REPETITION FUNCTION 3: LIST COMPREHENSION ===


def create_files_using_list_comprehension() -> None:
    """Create one text file per item in a transformed list.

    WHY: Use a list comprehension to transform one list into another.
    Read it as: <expression> FOR each <item> IN <list>.
    List comprehensions are more concise than a for loop building a new list.

    Arguments: None
    Returns: None
    """
    LOG.info("========================")
    LOG.info("FUNCTION 3: list comprehension")
    LOG.info("========================")

    prefix: str = "HS_"

    LOG.info(f"Original list: {New_Teacher_LIST}")
    HS_list: list[str] = [f"{prefix}{name}" for name in New_Teacher_LIST]
    LOG.info(f"Transformed list: {HS_list}")

    for _HS in HS_list:
        filename: str = f"{_HS}.txt"
        path: Path = PROCESSED_DIR / filename
        content: str = f"Special data about: '{_HS}'\n"
        write_text_file(path=path, content=content)


# === DEFINE THE MAIN FUNCTION THAT CALLS OTHER FUNCTIONS ===


def main() -> None:
    """Entry point when running this file as a Python script.

    Arguments: None
    Returns: None
    """
    log_header(LOG, "P02")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    create_files_from_list()
    create_files_using_list_comprehension()

    LOG.info("========================")
    LOG.info("Executed successfully!")
    LOG.info("========================")


# === CONDITIONAL EXECUTION GUARD ===

# WHY: Only call main() when running this file directly as a script.
# This is standard Python boilerplate.

if __name__ == "__main__":
    main()
