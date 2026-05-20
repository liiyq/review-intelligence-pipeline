# Review Intelligence Pipeline

A production-grade LLM-powered analytics pipeline on 6M Amazon reviews.

## Project Goal
Analyze Amazon Electronics review data and automatically extract 
competitive insights using AI, helping product teams quickly understand 
user pain points and market opportunities.

## Dataset
- Amazon Reviews 2023 (Electronics subset)
- Source: HuggingFace `McAuley-Lab/Amazon-Reviews-2023`
- Scale: ~6M reviews

## Tech Stack
- Python 3.11
- DuckDB (local data warehouse)
- LangChain + OpenAI (LLM analysis layer)
- Prefect (workflow orchestration)
- Streamlit (visualization)

## Progress
- [x] Environment setup & GitHub initialization
- [x] Stage 1: Architecture design
- [ ] Stage 2: Data ingestion
- [ ] Stage 3: Core engineering
- [ ] Stage 4: Production hardening
- [ ] Stage 5: Full-stack delivery