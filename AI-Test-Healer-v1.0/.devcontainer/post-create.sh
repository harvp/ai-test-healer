#!/bin/bash
set -e

echo "=== Configuring Codespace for GitHub and Python ==="

# 1️⃣ Clear Codespaces temporary token
unset GITHUB_TOKEN

# 2️⃣ GitHub CLI authentication
if ! gh auth status >/dev/null 2>&1; then
    echo "No GitHub CLI auth found. Please sign in:"
    gh auth login -h github.com -w
else
    echo "Already authenticated as:"
    gh auth status
fi

# 3️⃣ Set Git username/email (replace with your own)
git config --global user.name "Harvey Petersen"
git config --global user.email "harvp@example.com"

# 4️⃣ Install Python dependencies
if [ -f "/workspaces/codespaces-blank/AI-Test-Healer-v1.0/requirements.txt" ]; then
    echo "Installing Python dependencies..."
    pip install --no-cache-dir -r /workspaces/codespaces-blank/AI-Test-Healer-v1.0/requirements.txt
fi

echo "✅ Codespace setup complete."
