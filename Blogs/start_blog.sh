#!/bin/bash

echo "========================================"
echo "   Personal Blog - Quick Start"
echo "========================================"
echo ""
echo "Starting blog server..."
echo ""

cd "$(dirname "$0")"

if [ ! -d "venv" ]; then
    echo "ERROR: Virtual environment not found!"
    exit 1
fi

source venv/Scripts/activate

echo "✓ Virtual environment activated"
echo ""
echo "Your blog URLs:"
echo "  🏠 Homepage:     http://localhost:5000/"
echo "  ✍️  Create Post:  http://localhost:5000/create"
echo "  ⚙️  Admin Panel:  http://localhost:5000/admin"
echo ""
echo "Press CTRL+C to stop the server"
echo "========================================"
echo ""

# Start server
python run.py
