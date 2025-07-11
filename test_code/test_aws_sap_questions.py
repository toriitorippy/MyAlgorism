#!/usr/bin/env python
# coding: utf-8

"""
Test module for AWS Solutions Architect Professional (SAP) Exam Question Generator
"""

import sys
import os
import unittest
from io import StringIO
import json
import tempfile

# Add the parent directory to the path so we can import the module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from mycode.aws_sap_questions import AWSQuestion, AWSSAPQuestionBank


class TestAWSQuestion(unittest.TestCase):
    """Test cases for the AWSQuestion class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.question = AWSQuestion(
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
    
    def test_check_answer(self):
        """Test the check_answer method."""
        self.assertTrue(self.question.check_answer("B"))
        self.assertTrue(self.question.check_answer("b"))
        self.assertFalse(self.question.check_answer("A"))
        self.assertFalse(self.question.check_answer("C"))
        self.assertFalse(self.question.check_answer("D"))
    
    def test_display_question(self):
        """Test the display_question method."""
        captured_output = StringIO()
        sys.stdout = captured_output
        self.question.display_question()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Test question?", output)
        self.assertIn("A. Option A", output)
        self.assertIn("B. Option B", output)
        self.assertIn("C. Option C", output)
        self.assertIn("D. Option D", output)
    
    def test_display_explanation(self):
        """Test the display_explanation method."""
        captured_output = StringIO()
        sys.stdout = captured_output
        self.question.display_explanation()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Correct answer: B", output)
        self.assertIn("This is the explanation", output)


class TestAWSSAPQuestionBank(unittest.TestCase):
    """Test cases for the AWSSAPQuestionBank class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.question_bank = AWSSAPQuestionBank()
    
    def test_question_bank_initialization(self):
        """Test that the question bank is initialized with questions."""
        self.assertGreater(len(self.question_bank.questions), 0)
    
    def test_get_questions_by_domain(self):
        """Test the get_questions_by_domain method."""
        domains = ["networking", "security", "storage", "compute", "database", 
                  "migration", "cost", "ha", "serverless", "hybrid"]
        
        for domain in domains:
            questions = self.question_bank.get_questions_by_domain(domain)
            # Check that we have at least one question for each domain
            self.assertGreaterEqual(len(questions), 1)
            # Check that all questions have the correct domain
            for question in questions:
                self.assertEqual(question.domain, domain)
    
    def test_get_random_questions(self):
        """Test the get_random_questions method."""
        # Test with default count
        random_questions = self.question_bank.get_random_questions()
        self.assertEqual(len(random_questions), 5)
        
        # Test with custom count
        random_questions = self.question_bank.get_random_questions(3)
        self.assertEqual(len(random_questions), 3)
        
        # Test with count larger than available questions
        all_questions = len(self.question_bank.questions)
        random_questions = self.question_bank.get_random_questions(all_questions + 10)
        self.assertEqual(len(random_questions), all_questions)
    
    def test_export_questions_to_json(self):
        """Test the export_questions_to_json method."""
        with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as temp_file:
            temp_filename = temp_file.name
        
        try:
            # Export questions to the temporary file
            self.question_bank.export_questions_to_json(temp_filename)
            
            # Check that the file exists and contains valid JSON
            self.assertTrue(os.path.exists(temp_filename))
            
            with open(temp_filename, 'r', encoding='utf-8') as f:
                questions_data = json.load(f)
            
            # Check that the exported data matches the questions in the bank
            self.assertEqual(len(questions_data), len(self.question_bank.questions))
            
            # Check the structure of the exported data
            for question_data in questions_data:
                self.assertIn("question_text", question_data)
                self.assertIn("options", question_data)
                self.assertIn("correct_answer", question_data)
                self.assertIn("explanation", question_data)
                self.assertIn("domain", question_data)
        
        finally:
            # Clean up the temporary file
            if os.path.exists(temp_filename):
                os.unlink(temp_filename)


if __name__ == "__main__":
    unittest.main()