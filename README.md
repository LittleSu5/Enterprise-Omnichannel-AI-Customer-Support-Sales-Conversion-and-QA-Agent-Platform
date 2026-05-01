# Enterprise Omnichannel AI Customer Support, Sales Conversion, and QA Agent Platform

An enterprise-grade multi-agent platform for omnichannel customer support, sales conversion, workflow execution, conversation summarization, and QA automation.

## Overview
This project simulates a large-scale AI agent platform designed for enterprise service scenarios. It coordinates multiple agents for intent understanding, customer profiling, retrieval, response generation, workflow execution, and quality assurance.

## Core Capabilities
- Omnichannel customer support workflow
- Sales follow-up and conversion assistance
- QA scoring and compliance review
- Conversation summarization
- Mock CRM, order, and ticket integration
- Token usage metrics and monitoring endpoints

## Agent Architecture
- Intent Agent: identifies user intent and issue type
- Profile Agent: enriches customer context from behavior and attributes
- Retrieval Agent: fetches FAQ, policy, and product knowledge
- Response Agent: generates support or sales responses
- Execution Agent: simulates CRM, order, and ticket actions
- QA Agent: scores quality, compliance, and conversion opportunity
- Summary Agent: produces structured conversation summaries

## Tech Stack
- Python
- FastAPI
- Pydantic
- Pytest

## Run Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
