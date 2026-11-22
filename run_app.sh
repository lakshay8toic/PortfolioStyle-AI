#!/bin/bash
# -------------------------------------------------------------
# PortfolioStyle AI - One-Click Launcher Script for macOS/Linux
# Double-click or run: ./run_app.sh
# -------------------------------------------------------------

# Move to the script's directory
cd "$(dirname "$0")"

echo "============================================================"
echo " Starting PortfolioStyle AI Local Web Application..."
echo "============================================================"

# Launch the app and open the browser automatically
python3 app.py
