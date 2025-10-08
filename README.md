# Debricked Pip Trust Test 🧠

This repo is designed to test how **Debricked** evaluates Python dependencies when the **Trust Score** is missing.  
It includes both active and inactive dependencies to help you analyze **contribution** and **popularity** metrics.

### 🧩 Steps to Try
1. Push this repo to GitHub.
2. Connect it to your **Debricked** workspace.
3. Run a dependency scan.
4. Compare metrics for:
   - `requests` (very active)
   - `beautifulsoup4` (moderate)
   - `PySimpleGUI` (less maintained)

### 🧪 Goal
Observe how Debricked compensates for missing **trust scores** with other indicators like:
- Contribution activity
- Popularity
- Vulnerability history
