"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record: tuple[str]) -> str:
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    Parameters:
        record: A (treasure, coordinate) pair.

    Returns:
        The extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate: str) -> tuple[str, str]:
    """Split the given coordinate into tuple containing its individual components.

    Parameters:
        coordinate: A string map coordinate.

    Returns:
        The string coordinate split into its individual components.
    """

    return tuple(coordinate[0:2])


def compare_records(azara_record: tuple[str, str], rui_record: tuple[str]) -> bool:
    """Compare two record types and determine if their coordinates match.

    Parameters:
        azara_record: A (treasure, coordinate) pair.
        rui_record: A (location, tuple(coordinate_1, coordinate_2), quadrant) trio.

    Returns:
        Do the coordinates match?
    """
    return tuple(azara_record[1]) == rui_record[1]


def create_record(azara_record: tuple[str, str], rui_record: tuple[str]) -> tuple | str:
    """Combine the two record types (if possible) and create a combined record group.

    Parameters:
        azara_record: A (treasure, coordinate) pair.
        rui_record: A (location, coordinate, quadrant) trio.

    Returns:
        The combined record (if compatible), or the string "not a match" (if incompatible).
    """
    
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record 
    return 'not a match'


def clean_up(combined_record_group: tuple[tuple]) -> str:
    """Clean up a combined record group into a multi-line string of single records.

    Parameters:
        combined_record_group: Everything from both participants.

    Returns:
        Everything "cleaned", excess coordinates and information are removed.

    """
    
    report = []
    for record in combined_record_group:
        cleaned_record = record[:1] + record[2:]
        report.append(str(cleaned_record))
    return '\n'.join(report) + '\n'