#!/bin/bash

JOB_URL=$1
LOG_LEVEL=$2
LOG_FILE="file.txt"

echo "Job URL: $JOB_URL" >> $LOG_FILE

# Extract owner, repo, and run_id
if [[ $JOB_URL =~ github\.com/([^/]+)/([^/]+)/actions/runs/([0-9]+) ]]; then
  OWNER="${BASH_REMATCH[1]}"
  REPO="${BASH_REMATCH[2]}"
  RUN_ID="${BASH_REMATCH[3]}"
else
  echo "Invalid GitHub Actions job URL!" >> $LOG_FILE
  exit 1
fi

# GitHub API URL
API_URL="https://api.github.com/repos/$OWNER/$REPO/actions/runs/$RUN_ID"

# Query GitHub API
RESPONSE=$(curl -s -H "Authorization: Bearer $GH_TOKEN" -H "Accept: application/vnd.github+json" "$API_URL")

# Parse values
START_TIME=$(echo "$RESPONSE" | jq -r '.run_started_at')
END_TIME=$(echo "$RESPONSE" | jq -r '.updated_at')
STATUS=$(echo "$RESPONSE" | jq -r '.status')
CONCLUSION=$(echo "$RESPONSE" | jq -r '.conclusion')
EVENT=$(echo "$RESPONSE" | jq -r '.event')

echo "Start Time: $START_TIME" >> $LOG_FILE
echo "End Time: $END_TIME" >> $LOG_FILE
echo "Status: $STATUS" >> $LOG_FILE
echo "Conclusion: $CONCLUSION" >> $LOG_FILE
echo "Trigger Event: $EVENT" >> $LOG_FILE

# Optional: Logging level
echo "Log Level: $LOG_LEVEL" >> $LOG_FILE
