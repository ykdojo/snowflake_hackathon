#!/bin/bash

# Check if the virtual environment exists
if [ ! -d "venv" ]; then
  # Create a virtual environment
  python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Install the required packages using the requirements.txt file
pip install -r requirements.txt
