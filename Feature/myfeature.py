"""Basic feature module."""


def greet_user(name: str) -> str:
    """Return a greeting message for the given user name."""
    return f"Hello, {name}! Welcome to the feature module."


def calculate_sum(values: list[int]) -> int:
    """Return the sum of a list of integers."""
    return sum(values)


if __name__ == "__main__":
    print(greet_user("Developer"))
    print("Sum of [1, 2, 3, 4] is", calculate_sum([1, 2, 3, 4]))
    print ("This is here just to test the feature branch")
    