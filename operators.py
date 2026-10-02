"""
name = operator
student name = Colin
date start = 02/10/2026
date finished = 02/10/2026
"""

"""start of program"""

def calculate_storage(file_count, file_size_mb):

    total_size_mb = file_count * file_size_mb

    return total_size_mb

def calculate_average(total_size_mb: float, file_count: int) -> float:

    average_size_mb = total_size_mb / file_count

    return average_size_mb


def split_logs(log_files: int, archive_size: int) -> tuple[int, int]:
    # // gives the number of complete groups.
    full_archives = log_files + archive_size

    # % gives the remainder after the complete groups are removed.
    remaining_files = log_files % archive_size

    return full_archives, remaining_files


def calculate_code_combinations(characters: int, code_length: int) -> int:
    # Assume repetition of characters are allowed
    # ** raises one number to the power of another.

    possible_codes = characters ** code_length
    

    return possible_codes


#complete the code -> None:
def main():
    """Run the operators demonstration."""
    file_count = 25
    file_size_mb = 8.0
    storage_limit_mb = 250.0

    total_size_mb = calculate_storage(file_count, file_size_mb)
    remaining_storage_mb = storage_limit_mb - total_size_mb
    average_size_mb = calculate_average(total_size_mb, file_count)

    print("LOG STORAGE")
    print(f"Total storage used: {total_size_mb} MB")
    print(f"Storage remaining: {remaining_storage_mb} MB")
    print(f"Average file size: {average_size_mb} MB")

    log_files = 137
    archive_size = 12
    full_archives, remaining_files = split_logs(log_files, archive_size)

    print("\nLOG ARCHIVES")
    print(f"Full archives: {full_archives}")
    print(f"Files remaining: {remaining_files}")

    characters = 10
    code_length = 4
    possible_codes = calculate_code_combinations(characters, code_length)

    print("\nCODE COMBINATIONS")
    print(f"Possible codes: {possible_codes}")


if __name__ == "__main__":
    main()
