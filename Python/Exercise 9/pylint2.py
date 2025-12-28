"""
Name: Liam Saunders
Student Number: L00187849
Date: 15-DEC-2024
Version: 1.0
Purpose:
    Demonstrate clean Python style and correct type handling to satisfy pylint.
"""

def main() -> None:
    """Run simple arithmetic and safe string output."""
    a: int = 1
    b: int = 2
    c: str = "JOR"

    # Integer addition
    print(a + b)

    # String concatenation (explicit conversion avoids TypeError)
    print(f"{a}{c}")


if __name__ == "__main__":
    main()
