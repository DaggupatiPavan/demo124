#!/bin/bash

LOG_FILE="workflowdata.txt"

# 1. Start Time
echo "Start Time: $(date -u '+%Y-%m-%dT%H:%M:%SZ')" >> $LOG_FILE

# 2. Input parameters
echo "Input Parameters:" >> $LOG_FILE
env | grep '^INPUT_' >> $LOG_FILE

# 3. Logging Level
echo "Log Level: $INPUT_LOG_LEVEL" >> $LOG_FILE

# 4. stdout/stderr capture
{
  echo "This is a normal message"
  echo "This is an error message" >&2
} >> $LOG_FILE 2>&1

# 5. End Time
echo "End Time: $(date -u '+%Y-%m-%dT%H:%M:%SZ')" >> $LOG_FILE
