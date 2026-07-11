# 10 AWS DevOps and AI Automation Projects

This workspace contains 10 portfolio-style projects that combine AWS, DevOps, and AI automation concepts. Each project is scaffolded as a learning starter with a simple Python entrypoint, supporting docs, and example environment configuration.

## Project Overview

1. Password-Reset-Automation
   - Automates password reset workflows and related identity operations.
   - Good for practicing AWS IAM, notifications, and automation logic.

2. AWS-Inventory-Tool
   - Collects AWS inventory data such as EC2, S3, and RDS resources.
   - Supports CLI-based collection and reporting outputs.

3. EC2-Scheduler
   - Helps schedule EC2 instance start/stop actions to save costs.
   - Useful for learning automation, scheduling, and AWS resource control.

4. IAM-Automation
   - Focuses on identity and access management workflows.
   - Great for experimenting with users, roles, policies, and access automation.

5. Terraform-Generator
   - Generates Terraform templates from prompts or structured input.
   - Useful for learning infrastructure-as-code generation patterns.

6. Cloud-Cost-Optimizer
   - Helps analyze AWS usage and identify cost-saving opportunities.
   - A good fit for cost optimization and reporting workflows.

7. AWS-Chatbot
   - Provides a chatbot-style interface for AWS operations and support tasks.
   - Ideal for exploring conversational automation and AI-assisted workflows.

8. AI-Documentation-Search
   - Implements a documentation search experience using embeddings and retrieval concepts.
   - Useful for AI search, vector-based retrieval, and knowledge exploration.

9. Incident-RCA-Agent
   - Supports incident analysis and root cause investigation workflows.
   - Good for building automation around logs, alerts, and incident reporting.

10. DevOps-AI-Assistant
    - A multi-agent style assistant for DevOps tasks and automation workflows.
    - Useful for experimenting with AI orchestration and operational helpers.

## AWS Profile Support
The AWS-enabled projects now support credentials from shared AWS profiles in ~/.aws/credentials or ~/.aws/config. You can either set AWS_PROFILE in each project .env file or rely on the default boto3 credential chain.

## Getting Started
- Review each project folder individually.
- Copy the relevant .env.example to .env and update values.
- Install dependencies with pip install -r requirements.txt.
- Run the project entrypoint to begin development.
