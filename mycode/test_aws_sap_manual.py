#!/usr/bin/env python
# coding: utf-8

"""
Manual test script for AWS Solutions Architect Professional (SAP) Exam Question Generator
"""

from aws_sap_questions import AWSQuestion, AWSSAPQuestionBank

def test_question_class():
    """Test the AWSQuestion class."""
    print("Testing AWSQuestion class...")
    
    # Create a test question
    question = AWSQuestion(
        question_text="Test question?",
        options={
            "A": "Option A",
            "B": "Option B",
            "C": "Option C",
            "D": "Option D"
        },
        correct_answer="B",
        explanation="This is the explanation",
        domain="test"
    )
    
    # Test display_question
    print("\nTesting display_question:")
    question.display_question()
    
    # Test check_answer
    print("\nTesting check_answer:")
    print(f"Answer 'B' is correct: {question.check_answer('B')}")
    print(f"Answer 'b' is correct: {question.check_answer('b')}")
    print(f"Answer 'A' is correct: {question.check_answer('A')}")
    
    # Test display_explanation
    print("\nTesting display_explanation:")
    question.display_explanation()


def test_question_bank():
    """Test the AWSSAPQuestionBank class."""
    print("\nTesting AWSSAPQuestionBank class...")
    
    # Create a question bank
    question_bank = AWSSAPQuestionBank()
    
    # Test question bank initialization
    print(f"\nNumber of questions in bank: {len(question_bank.questions)}")
    
    # Test get_questions_by_domain
    print("\nTesting get_questions_by_domain:")
    for domain in question_bank.domains:
        domain_questions = question_bank.get_questions_by_domain(domain)
        print(f"Domain '{domain}' has {len(domain_questions)} questions")
    
    # Test get_random_questions
    print("\nTesting get_random_questions:")
    random_questions = question_bank.get_random_questions(3)
    print(f"Got {len(random_questions)} random questions")
    
    # Display a sample question
    if random_questions:
        print("\nSample random question:")
        random_questions[0].display_question()
        random_questions[0].display_explanation()


if __name__ == "__main__":
    test_question_class()
    test_question_bank()
    
    print("\nAll manual tests completed!")