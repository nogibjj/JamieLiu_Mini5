"""
Test goes here

"""

import subprocess


def test_extract():
    """tests extract()"""
    result = subprocess.run(
        ["python", "main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Extracting data..." in result.stdout


def test_transform_load():
    """tests transform_load()"""
    result = subprocess.run(
        ["python", "main.py", "transform_load"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Transforming data..." in result.stdout


def test_update_record():
    """tests update_record()"""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "update_record",
            "Germany",   # Using country as identifier
            "320",       # Updated beer_servings
            "210",       # Updated spirit_servings
            "160",       # Updated wine_servings
            "13.0",      # Updated total_alcohol
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_delete_record():
    """tests delete_record()"""
    result = subprocess.run(
        ["python", "main.py", "delete_record", "Germany"],  # Delete using country name
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_create_record():
    """tests create_record()"""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "create_record",
            "Germany",    # country
            "300",        # beer_servings
            "200",        # spirit_servings
            "150",        # wine_servings
            "12.5",       # total_litres_of_pure_alcohol
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_general_query():
    """tests general_query"""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "general_query",
            "SELECT * FROM DrinksDB WHERE country = 'Germany'",  # Query based on country
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_read_data():
    """tests read_data"""
    result = subprocess.run(
        ["python", "main.py", "read_data"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


if __name__ == "__main__":
    test_extract()
    test_transform_load()
    test_create_record()
    test_read_data()
    test_update_record()
    test_delete_record()
    test_general_query()
