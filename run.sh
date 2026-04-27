#!/bin/bash
# Initialize virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the FastAPI app using uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
