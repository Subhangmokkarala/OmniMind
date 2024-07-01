# query_processor.py

def process_query(query_text):
    """
    Process a natural language query.

    Args:
    - query_text (str): Natural language query.

    Returns:
    - str: Processed query text.
    """
    # Add your query processing logic here
    processed_query = query_text.lower()  # Example: Convert query to lowercase
    return processed_query

# Example usage:
if __name__ == "__main__":
    query = "What are some milestone model architectures and papers in the last few years?"
    processed_query = process_query(query)
    print("Processed Query:")
    print(processed_query)
