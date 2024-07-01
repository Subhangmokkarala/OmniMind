# main.py

import sys
import os

# Add the parent directory of 'src' to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.data_loader import load_lecture_notes, load_llm_architectures
from src.query_processor import process_query
from src.vector_indexer import VectorIndexer
from src.answer_generator import generate_answer
from src.reference_citation import cite_sources
from src.memory_handler import MemoryHandler

def main():
    # Load data
    lecture_notes = load_lecture_notes('data/lecture_notes.txt')
    llm_architectures = load_llm_architectures('data/llm_architectures.csv')
    
    # Initialize components
    indexer = VectorIndexer()
    memory = MemoryHandler()
    
    # Example query
    query = "What are some milestone model architectures?"
    
    # Process query
    processed_query = process_query(query)
    
    # Build index (using lecture_notes or other data)
    # indexer.build_index(lecture_notes)
    
    # Search for relevant information
    # relevant_info = indexer.search(processed_query)
    
    # For simplicity, generate a static answer
    relevant_info = "Information about milestone model architectures."
    answer = generate_answer(query, relevant_info)
    
    # Remember context
    memory.remember_context(query, answer)
    
    # Retrieve contextual answer for a follow-up query
    follow_up_query = "Tell me more about BERT architecture."
    contextual_answer = memory.retrieve_context(follow_up_query)
    
    # Cite sources
    references = ["Source A", "Source B"]
    cited_answer = cite_sources(answer, references)
    
    # Output results
    print("Processed Query:", processed_query)
    print("Generated Answer:", answer)
    print("Contextual Answer:", contextual_answer)
    print("Cited Answer:", cited_answer)

if __name__ == "__main__":
    main()
