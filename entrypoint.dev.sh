#!/bin/bash

echo "Running app"
python -m uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload