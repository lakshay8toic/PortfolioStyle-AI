#!/bin/bash
# -------------------------------------------------------------
# Double-click this file to launch the PortfolioStyle AI Website!
# -------------------------------------------------------------

# Resolve script directory and navigate to root project folder
DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$DIR"

echo "============================================================"
echo " 🏨 Launching PortfolioStyle AI Web Application..."
echo " Opening in your default browser at http://localhost:8000"
echo "============================================================"

python3 app.py
