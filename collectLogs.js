const fs = require('fs');
const core = require('@actions/core');
const path = require('path');

async function run() {
  try {
    const startTime = core.getInput('start_time');
    const loggingLevel = core.getInput('logging_level') || 'info';
    const stepsLog = core.getInput('steps_log') || ''; // Get the logs from the workflow
    const outputFile = core.getInput('output_file') || 'workflow_output.txt';

    const endTime = new Date().toISOString();
    const duration = (new Date() - new Date(startTime)) / 1000; // Duration in seconds

    let logData = `=== Workflow Details ===\n`;
    logData += `Start Time: ${startTime}\n`;
    logData += `End Time: ${endTime}\n`;
    logData += `Duration: ${duration} seconds\n`;
    logData += `Logging Level: ${loggingLevel}\n`;
    logData += `Steps Output:\n${stepsLog}\n`;

    // Write log data to a file
    fs.writeFileSync(outputFile, logData, { flag: 'w' });

    core.info('Logs collected and written to output file!');
  } catch (error) {
    core.setFailed(`Action failed: ${error.message}`);
  }
}

run();
