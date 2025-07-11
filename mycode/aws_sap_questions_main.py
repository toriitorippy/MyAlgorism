#!/usr/bin/env python
# coding: utf-8

"""
AWS Solutions Architect Professional (SAP) Exam Question Generator - Main Module

This module provides a command-line interface for the AWS SAP question generator.
"""

from aws_sap_questions import AWSSAPQuestionBank


def main():
    """Main function to run the AWS SAP question generator."""
    print("AWS Solutions Architect Professional (SAP) Exam Question Generator")
    print("===============================================================")
    
    question_bank = AWSSAPQuestionBank()
    
    while True:
        print("\nOptions:")
        print("1. Take a random quiz")
        print("2. Take a domain-specific quiz")
        print("3. List available domains")
        print("4. Export questions to JSON")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            try:
                num_questions = int(input("How many questions would you like? (default: 5): ") or "5")
                question_bank.run_quiz(num_questions)
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == "2":
            print("\nAvailable domains:")
            for code, name in question_bank.domains.items():
                print(f"- {code}: {name}")
            
            domain = input("\nEnter domain code: ").strip().lower()
            if domain in question_bank.domains:
                try:
                    num_questions = int(input("How many questions would you like? (default: 5): ") or "5")
                    question_bank.run_quiz(num_questions, domain)
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print(f"Invalid domain: {domain}")
        
        elif choice == "3":
            print("\nAvailable domains:")
            for code, name in question_bank.domains.items():
                question_count = len(question_bank.get_questions_by_domain(code))
                print(f"- {code}: {name} ({question_count} questions)")
        
        elif choice == "4":
            filename = input("Enter filename (default: aws_sap_questions.json): ").strip() or "aws_sap_questions.json"
            question_bank.export_questions_to_json(filename)
        
        elif choice == "5":
            print("Thank you for using the AWS SAP Question Generator. Good luck with your exam!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()