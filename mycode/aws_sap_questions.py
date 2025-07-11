#!/usr/bin/env python
# coding: utf-8

"""
AWS Solutions Architect Professional (SAP) Exam Question Generator

This module provides a collection of AWS SAP exam practice questions and
functionality to quiz users on these questions.
"""

import random
import json
import os
import sys
from typing import Dict, List, Tuple, Optional


class AWSQuestion:
    """Class representing an AWS Solutions Architect Professional exam question."""
    
    def __init__(self, 
                 question_text: str, 
                 options: Dict[str, str], 
                 correct_answer: str, 
                 explanation: str, 
                 domain: str):
        """
        Initialize an AWS exam question.
        
        Args:
            question_text: The question text
            options: Dictionary of options (A, B, C, D) and their text
            correct_answer: The correct option (A, B, C, D)
            explanation: Explanation of the correct answer
            domain: The AWS domain this question belongs to
        """
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer
        self.explanation = explanation
        self.domain = domain
    
    def display_question(self) -> None:
        """Display the question and its options."""
        print(f"\n{self.question_text}\n")
        for key, value in self.options.items():
            print(f"{key}. {value}")
    
    def check_answer(self, user_answer: str) -> bool:
        """
        Check if the user's answer is correct.
        
        Args:
            user_answer: The user's answer (A, B, C, D)
            
        Returns:
            bool: True if correct, False otherwise
        """
        return user_answer.upper() == self.correct_answer.upper()
    
    def display_explanation(self) -> None:
        """Display the explanation for the correct answer."""
        print(f"\nCorrect answer: {self.correct_answer}")
        print(f"Explanation: {self.explanation}")


class AWSSAPQuestionBank:
    """Class to manage a collection of AWS SAP exam questions."""
    
    def __init__(self):
        """Initialize the question bank with predefined questions."""
        self.questions = self._create_question_bank()
        self.domains = {
            "compute": "Compute and Containers",
            "storage": "Storage Solutions",
            "database": "Database Services",
            "networking": "Network Design and Connectivity",
            "security": "Security and Identity",
            "migration": "Migration and Transfer",
            "cost": "Cost Optimization",
            "ha": "High Availability and Disaster Recovery",
            "serverless": "Serverless Architecture",
            "hybrid": "Hybrid Architecture"
        }
    
    def get_questions_by_domain(self, domain: str) -> List[AWSQuestion]:
        """
        Get questions filtered by domain.
        
        Args:
            domain: The domain to filter questions by
            
        Returns:
            List[AWSQuestion]: List of questions in the specified domain
        """
        return [q for q in self.questions if q.domain == domain]
    
    def get_random_questions(self, count: int = 5) -> List[AWSQuestion]:
        """
        Get a random selection of questions.
        
        Args:
            count: Number of random questions to return
            
        Returns:
            List[AWSQuestion]: List of random questions
        """
        if count > len(self.questions):
            count = len(self.questions)
        return random.sample(self.questions, count)
    
    def run_quiz(self, num_questions: int = 5, domain: Optional[str] = None) -> Tuple[int, int]:
        """
        Run an interactive quiz with the specified number of questions.
        
        Args:
            num_questions: Number of questions to include in the quiz
            domain: Optional domain to filter questions by
            
        Returns:
            Tuple[int, int]: (Number of correct answers, Total number of questions)
        """
        if domain:
            available_questions = self.get_questions_by_domain(domain)
            if not available_questions:
                print(f"No questions available for domain: {domain}")
                return (0, 0)
        else:
            available_questions = self.questions
        
        if num_questions > len(available_questions):
            num_questions = len(available_questions)
            print(f"Only {num_questions} questions available.")
        
        quiz_questions = random.sample(available_questions, num_questions)
        score = 0
        
        print(f"\n===== AWS Solutions Architect Professional Quiz =====")
        if domain:
            print(f"Domain: {self.domains.get(domain, domain)}")
        print(f"Number of questions: {num_questions}")
        print("=====================================================\n")
        
        for i, question in enumerate(quiz_questions):
            print(f"\nQuestion {i+1} of {num_questions}:")
            question.display_question()
            
            while True:
                user_answer = input("\nYour answer (A/B/C/D): ").strip().upper()
                if user_answer in ["A", "B", "C", "D"]:
                    break
                print("Invalid input. Please enter A, B, C, or D.")
            
            is_correct = question.check_answer(user_answer)
            if is_correct:
                print("\n✓ Correct!")
                score += 1
            else:
                print("\n✗ Incorrect.")
            
            question.display_explanation()
            print("\n-----------------------------------------------------")
        
        print(f"\nQuiz complete! Your score: {score}/{num_questions} ({score/num_questions*100:.1f}%)")
        return (score, num_questions)
    
    def export_questions_to_json(self, filename: str) -> None:
        """
        Export all questions to a JSON file.
        
        Args:
            filename: The name of the file to export to
        """
        questions_data = []
        for q in self.questions:
            questions_data.append({
                "question_text": q.question_text,
                "options": q.options,
                "correct_answer": q.correct_answer,
                "explanation": q.explanation,
                "domain": q.domain
            })
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(questions_data, f, ensure_ascii=False, indent=2)
        
        print(f"Exported {len(questions_data)} questions to {filename}")
    
    def _create_question_bank(self) -> List[AWSQuestion]:
        """
        Create and return a list of AWS SAP exam questions.
        
        Returns:
            List[AWSQuestion]: A list of AWS exam questions
        """
        questions = []
        
        # Question 1 - Networking
        questions.append(AWSQuestion(
            question_text="A company is designing a multi-region architecture and needs to ensure that users are routed to the closest AWS region with the lowest latency. Which AWS service should they use?",
            options={
                "A": "AWS Global Accelerator",
                "B": "Amazon CloudFront",
                "C": "AWS Transit Gateway",
                "D": "Amazon Route 53 with latency-based routing"
            },
            correct_answer="D",
            explanation="Amazon Route 53 with latency-based routing helps route users to the AWS region that provides the lowest latency. It makes routing decisions based on network conditions between users and AWS regions. AWS Global Accelerator improves availability and performance using the AWS global network but doesn't specifically route to the lowest latency region. CloudFront is a CDN service, and Transit Gateway connects VPCs and on-premises networks.",
            domain="networking"
        ))
        
        # Question 2 - Security
        questions.append(AWSQuestion(
            question_text="A Solutions Architect needs to design a solution that allows an application running in a private subnet to access DynamoDB while preventing the traffic from traversing the internet. What is the MOST secure and cost-effective solution?",
            options={
                "A": "Configure a NAT Gateway and route DynamoDB traffic through the internet",
                "B": "Use VPC peering between the VPC and DynamoDB",
                "C": "Configure a VPC endpoint for DynamoDB",
                "D": "Deploy a proxy server in a public subnet to forward requests to DynamoDB"
            },
            correct_answer="C",
            explanation="A VPC endpoint for DynamoDB provides a private connection between your VPC and DynamoDB without requiring an internet gateway, NAT device, VPN, or AWS Direct Connect. Traffic between your VPC and DynamoDB does not leave the Amazon network. This is the most secure and cost-effective solution as it doesn't require additional infrastructure like NAT Gateways or proxy servers, and doesn't incur data transfer charges.",
            domain="security"
        ))
        
        # Question 3 - High Availability
        questions.append(AWSQuestion(
            question_text="A company has a critical application that must have an RPO (Recovery Point Objective) of 1 minute and an RTO (Recovery Time Objective) of 5 minutes. Which disaster recovery strategy should they implement?",
            options={
                "A": "Backup and Restore",
                "B": "Pilot Light",
                "C": "Warm Standby",
                "D": "Multi-site Active/Active"
            },
            correct_answer="D",
            explanation="Multi-site Active/Active is the only option that can meet such aggressive RPO and RTO requirements. In this approach, the application is deployed and actively serving traffic from multiple regions simultaneously. This provides near-zero RPO and RTO as traffic can be immediately redirected to the functioning region if one region fails. Backup and Restore typically has RPO/RTO in hours or days. Pilot Light has RPO in minutes but RTO in tens of minutes. Warm Standby has better RPO/RTO than Pilot Light but still typically can't achieve 5-minute RTO consistently.",
            domain="ha"
        ))
        
        # Question 4 - Storage
        questions.append(AWSQuestion(
            question_text="A company needs to store large video files that are accessed frequently for the first 30 days, occasionally for the next 60 days, and rarely after 90 days. What is the MOST cost-effective Amazon S3 storage configuration?",
            options={
                "A": "Store all objects in S3 Standard and use Cross-Region Replication",
                "B": "Store all objects in S3 Standard-IA and use lifecycle policies to move to Glacier after 90 days",
                "C": "Store in S3 Standard, move to S3 Standard-IA after 30 days, and move to Glacier Deep Archive after 90 days",
                "D": "Store in S3 Standard, move to S3 One Zone-IA after 30 days, and move to Glacier after 90 days"
            },
            correct_answer="C",
            explanation="The most cost-effective solution is to use S3 lifecycle policies to automatically transition objects between storage classes based on their age. S3 Standard is appropriate for the first 30 days when access is frequent. S3 Standard-IA is suitable for the next 60 days when access is infrequent. After 90 days, when access is rare, Glacier Deep Archive provides the lowest cost for long-term archival. Option D uses One Zone-IA which is cheaper than Standard-IA but offers less durability by storing data in only one AZ, which may not be appropriate for important video files.",
            domain="storage"
        ))
        
        # Question 5 - Migration
        questions.append(AWSQuestion(
            question_text="A company is planning to migrate a large on-premises Oracle database to AWS. The database is 20TB in size and has high transaction volumes. The company wants to minimize downtime during migration. Which AWS service or feature should they use?",
            options={
                "A": "AWS Database Migration Service (DMS) with full load and CDC",
                "B": "AWS Snowball to transfer the database and then set up replication",
                "C": "AWS Application Migration Service",
                "D": "Export/Import using Oracle Data Pump and Amazon S3"
            },
            correct_answer="A",
            explanation="AWS Database Migration Service (DMS) with full load and change data capture (CDC) is the best option for migrating large databases with minimal downtime. DMS can perform the initial full load of the database while the source database remains operational. Once the full load is complete, CDC captures ongoing changes and applies them to the target database, allowing for near-zero downtime cutover when ready. Snowball is good for large data transfers but doesn't handle continuous replication by itself. Application Migration Service is for migrating applications, not specifically databases. Manual export/import would cause significant downtime for a 20TB database.",
            domain="migration"
        ))
        
        # Question 6 - Compute
        questions.append(AWSQuestion(
            question_text="A company runs a batch processing workload on EC2 instances. The jobs run for 1-2 hours and can be interrupted and restarted. The workload needs to process 100 instances but is not time-sensitive. Which EC2 purchasing option is MOST cost-effective?",
            options={
                "A": "On-Demand Instances",
                "B": "Reserved Instances",
                "C": "Spot Instances",
                "D": "Dedicated Hosts"
            },
            correct_answer="C",
            explanation="Spot Instances are the most cost-effective option for flexible, interruptible workloads that are not time-sensitive. Spot Instances offer up to 90% discount compared to On-Demand pricing but can be interrupted with a 2-minute notification when EC2 needs the capacity back. Since the batch jobs can be interrupted and restarted, and the workload is not time-sensitive, Spot Instances are ideal. Reserved Instances provide discounts but require 1 or 3-year commitments and are better for steady-state workloads. On-Demand Instances are more expensive. Dedicated Hosts are the most expensive option and are used for licensing or compliance requirements.",
            domain="compute"
        ))
        
        # Question 7 - Database
        questions.append(AWSQuestion(
            question_text="A company has an application that requires a highly available database with automatic failover, read replicas for read scaling, and storage that automatically grows. The database will store structured data and needs to support complex SQL queries. Which AWS database service best meets these requirements?",
            options={
                "A": "Amazon DynamoDB with Global Tables",
                "B": "Amazon RDS Multi-AZ with Read Replicas",
                "C": "Amazon ElastiCache with Redis Cluster Mode",
                "D": "Amazon Aurora with Multi-AZ and Aurora Replicas"
            },
            correct_answer="D",
            explanation="Amazon Aurora is the best choice for this scenario. It provides high availability with automatic failover across multiple Availability Zones, read replicas (Aurora Replicas) for read scaling, and storage that automatically grows from 10GB to 128TB. Aurora is fully compatible with MySQL and PostgreSQL, supporting complex SQL queries and structured data. Aurora also offers better performance and lower cost than standard RDS. DynamoDB is a NoSQL database not optimized for complex SQL queries. Standard RDS Multi-AZ provides high availability but Aurora has additional benefits. ElastiCache is an in-memory caching service, not a primary database.",
            domain="database"
        ))
        
        # Question 8 - Serverless
        questions.append(AWSQuestion(
            question_text="A company wants to build a new application using a serverless architecture. The application will consist of APIs that trigger business logic, store data, and send notifications. Which combination of AWS services should they use?",
            options={
                "A": "Amazon API Gateway, AWS Lambda, Amazon DynamoDB, and Amazon SNS",
                "B": "Elastic Load Balancer, Amazon EC2, Amazon RDS, and Amazon SQS",
                "C": "Amazon CloudFront, AWS Lambda@Edge, Amazon S3, and Amazon SES",
                "D": "AWS AppSync, Amazon EC2, Amazon ElastiCache, and Amazon SNS"
            },
            correct_answer="A",
            explanation="The combination of Amazon API Gateway, AWS Lambda, Amazon DynamoDB, and Amazon SNS creates a fully serverless architecture that meets all the requirements. API Gateway provides the API endpoints, Lambda runs the business logic without provisioning servers, DynamoDB offers serverless database storage, and SNS handles notifications. Option B uses EC2 and RDS which require server management. Option C is serverless but focused on content delivery rather than general application architecture. Option D includes EC2 which is not serverless.",
            domain="serverless"
        ))
        
        # Question 9 - Cost Optimization
        questions.append(AWSQuestion(
            question_text="A company has multiple AWS accounts and wants to optimize costs across the organization. Which combination of AWS services and features should they implement?",
            options={
                "A": "AWS Organizations with consolidated billing, AWS Budgets, and AWS Cost Explorer",
                "B": "Amazon CloudWatch, AWS Trusted Advisor, and AWS Shield",
                "C": "AWS Control Tower, Amazon GuardDuty, and AWS Config",
                "D": "AWS IAM, Amazon Inspector, and AWS Systems Manager"
            },
            correct_answer="A",
            explanation="AWS Organizations with consolidated billing, AWS Budgets, and AWS Cost Explorer is the best combination for cost optimization across multiple accounts. AWS Organizations with consolidated billing combines usage across accounts to share volume pricing discounts. AWS Budgets helps set custom cost and usage budgets with alerts. AWS Cost Explorer provides visualization and analysis of costs and usage patterns. The other options focus on security, governance, and operational management rather than cost optimization.",
            domain="cost"
        ))
        
        # Question 11 - Security
        questions.append(AWSQuestion(
            question_text="A company needs to implement a security solution that inspects all traffic to and from their VPCs, including traffic between VPCs. Which AWS service or feature should they use?",
            options={
                "A": "AWS Network Firewall",
                "B": "Security Groups",
                "C": "Network ACLs",
                "D": "AWS WAF"
            },
            correct_answer="A",
            explanation="AWS Network Firewall is the correct choice as it can inspect all traffic to and from VPCs, including traffic between VPCs. It provides stateful, managed network firewall and intrusion detection for VPCs. Security Groups operate at the instance level and can't inspect traffic between VPCs. Network ACLs are stateless and operate at the subnet level. AWS WAF is designed to protect web applications from common web exploits and doesn't inspect all VPC traffic.",
            domain="security"
        ))
        
        # Question 12 - Networking
        questions.append(AWSQuestion(
            question_text="A company has multiple VPCs across different AWS accounts and regions. They need to implement a solution that provides centralized network management and connectivity between all VPCs. Which combination of AWS services should they use?",
            options={
                "A": "AWS Transit Gateway with AWS Resource Access Manager",
                "B": "VPC peering connections with AWS Organizations",
                "C": "AWS Direct Connect with AWS Site-to-Site VPN",
                "D": "Amazon Route 53 with AWS Global Accelerator"
            },
            correct_answer="A",
            explanation="AWS Transit Gateway with AWS Resource Access Manager (RAM) is the correct solution. Transit Gateway acts as a network transit hub to connect multiple VPCs and on-premises networks. AWS RAM allows the Transit Gateway to be shared across multiple AWS accounts within an organization. This combination provides centralized network management and connectivity between all VPCs, even across different accounts and regions. VPC peering doesn't scale well for many VPCs as it requires point-to-point connections. Direct Connect and Site-to-Site VPN are for connecting to on-premises networks. Route 53 and Global Accelerator are for routing and accelerating user traffic, not for VPC connectivity.",
            domain="networking"
        ))
        
        # Question 13 - Database
        questions.append(AWSQuestion(
            question_text="A company has a mission-critical application that uses Amazon RDS for PostgreSQL. They need to ensure the database can recover from a regional failure with minimal data loss and downtime. Which solution should they implement?",
            options={
                "A": "Enable Multi-AZ deployment with automated backups",
                "B": "Set up RDS read replicas in multiple regions",
                "C": "Use RDS Multi-AZ with a cross-region read replica",
                "D": "Implement Amazon Aurora Global Database"
            },
            correct_answer="D",
            explanation="Amazon Aurora Global Database is designed for globally distributed applications, allowing a single Aurora database to span multiple AWS regions. It provides fast local reads with low latency in each region, and supports global write forwarding. In the event of a regional outage, one of the secondary regions can be promoted to take full read/write responsibilities in less than 1 minute. This provides the minimal data loss and downtime required for mission-critical applications. Multi-AZ deployments protect against AZ failures, not regional failures. Read replicas alone don't provide automated failover. RDS Multi-AZ with cross-region read replica requires manual intervention for failover and doesn't guarantee minimal data loss.",
            domain="database"
        ))
        
        # Question 14 - Storage
        questions.append(AWSQuestion(
            question_text="A company needs to store large amounts of infrequently accessed data that must be retained for compliance reasons for 7 years. The data might need to be retrieved within 12 hours. Which S3 storage class is most cost-effective for this requirement?",
            options={
                "A": "S3 Standard",
                "B": "S3 Standard-IA",
                "C": "S3 Glacier",
                "D": "S3 Glacier Deep Archive"
            },
            correct_answer="C",
            explanation="S3 Glacier is the most cost-effective storage class for this scenario. It's designed for data archiving with retrieval times ranging from minutes to hours (3-5 hours for standard retrieval), which meets the 12-hour retrieval requirement. S3 Glacier is significantly cheaper than S3 Standard and S3 Standard-IA for long-term storage. S3 Glacier Deep Archive is even cheaper but has longer retrieval times (up to 12 hours for standard retrieval), which would still meet the requirement but might be cutting it close. Given the 7-year retention period and infrequent access pattern, S3 Glacier provides the best balance of cost and retrieval time for this use case.",
            domain="storage"
        ))
        
        # Question 15 - Serverless
        questions.append(AWSQuestion(
            question_text="A company is building a serverless application that processes images uploaded to S3. The processing involves multiple steps including validation, resizing, and applying filters. Which AWS service should they use to coordinate these processing steps?",
            options={
                "A": "AWS Lambda with S3 event notifications",
                "B": "Amazon SQS with Lambda polling",
                "C": "AWS Step Functions",
                "D": "Amazon EventBridge"
            },
            correct_answer="C",
            explanation="AWS Step Functions is the best choice for coordinating multiple processing steps in a serverless application. It allows you to define and run workflows that coordinate multiple AWS services into serverless applications. Step Functions provides a visual workflow that shows the state of each step, making it easy to build and monitor multi-step applications. It manages state, checkpoints, and restarts, making it ideal for complex workflows like image processing pipelines. Lambda with S3 event notifications is good for simple processing but doesn't manage complex workflows. SQS with Lambda is good for decoupling but doesn't provide visual workflow management. EventBridge is an event bus service that routes events between services but doesn't manage workflow state.",
            domain="serverless"
        ))
        
        return questions