# Contains input validation & array search functions

# Helper function: Linear Search on Array
def array_search(array_list: list, product_id: int):
    # Performs a standard 0(N) linear search through a list.
    for item in array_list:
        if item is not None and item.product_id == product_id:
            return item
    return None

# Helper Input Validation Functions
def get_valid_int(prompt_text: str) -> int:
    # Repeatedly prompts user until a valid positive integer is entered
    while True:
        try:
            val = int(input(prompt_text))
            if val < 0:
                print("Invalid input. Value cannot be negative, please enter a positive integer")
                continue
            return val
        except ValueError:
            print("Invalid input. Please enter an integer only.")

def get_valid_float(prompt_text: str) -> float:
    # Repeatedly prompts user until a valid number (float) is entered
    while True:
        try:
            val = float(input(prompt_text))
            if val < 0:
                print("Invalid input. Value cannot be negative, please enter a positive float")
                continue
            return val
        except ValueError:
            print("Invalid input. Please enter a valid number for price.")