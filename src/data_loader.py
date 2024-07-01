# data_loader.py

def load_lecture_notes(file_path):
    """
    Load lecture notes from a text file.

    Args:
    - file_path (str): Path to the lecture notes text file.

    Returns:
    - str: Contents of the lecture notes.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lecture_notes = file.read()
    return lecture_notes

def load_llm_architectures(file_path):
    """
    Load LLM architectures from a CSV file.

    Args:
    - file_path (str): Path to the LLM architectures CSV file.

    Returns:
    - list of dict: List of dictionaries containing LLM architecture details.
    """
    import csv
    architectures = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            architectures.append(row)
    return architectures

# Example usage:
if __name__ == "__main__":
    lecture_notes = load_lecture_notes('data/lecture_notes.txt')
    llm_architectures = load_llm_architectures('data/llm_architectures.csv')
    print("Lecture Notes:")
    print(lecture_notes)
    print("\nLLM Architectures:")
    print(llm_architectures)
