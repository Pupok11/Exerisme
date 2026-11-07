"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record: tuple[str]) -> str:
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    Parameters:
        record (tuple): A (treasure, coordinate) pair.

    Returns:
        str: The extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate: str) -> tuple[str, str]:
    """Split the given coordinate into tuple containing its individual components.

    Parameters:
        coordinate (str): A string map coordinate.

    Returns:
        tuple: The string coordinate split into its individual components.
    """

    return tuple(coordinate[0:2])


def compare_records(azara_record: tuple[str, str], rui_record: tuple[str]) -> bool:
    """Compare two record types and determine if their coordinates match.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, tuple(coordinate_1, coordinate_2), quadrant) trio.

    Returns:
        bool: Do the coordinates match?
    """
    return tuple(azara_record[1]) == rui_record[1]


def create_record(azara_record: tuple[str, str], rui_record: tuple[str]) -> tuple | str:
    """Combine the two record types (if possible) and create a combined record group.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, coordinate, quadrant) trio.

    Returns:
        tuple or str: The combined record (if compatible), or the string "not a match" (if incompatible).
    """
    
    if compare_records(azara_record, rui_record) == True:
         return azara_record + rui_record 
    return "not a match"


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    Parameters:
        combined_record_group (tuple): Everything from both participants.

    Returns:
        str: Everything "cleaned", excess coordinates and information are removed.

    Note:
        The return statement is a multi-lined string with items separated by newlines.
        (see HINTS.md for an example).

    """
    
    report = []

    for record in combined_record_group:
        cleaned_record = record[:1] + record[2:]
        report.append(str(cleaned_record))

    return '\n'.join(report) + '\n'