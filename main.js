const fs = require('fs');
const core = require('@actions/core');

async function run() {
  try {
    const outputFile = core.getInput('output_file') || 'workflow_output.txt';
    const startTime = core.getInput('start_time');
    const endTime = new Date().toISOString();
    const duration = (new Date() - new Date(startTime)) / 1000; // Duration in seconds
    const loggingLevel = core.getInput('logging_level') || 'info';
    const stepsLog = core.getInput('steps_log') || '';  // Collect logs from previous steps

    let logData = `=== Workflow Details ===\n`;
    logData += `Start Time: ${startTime}\n`;
    logData += `End Time: ${endTime}\n`;
    logData += `Duration: ${duration} seconds\n`;
    logData += `Logging Level: ${loggingLevel}\n`;
    logData += `Steps Output:\n${stepsLog}\n`;

    // Save log data to file
    fs.writeFileSync(outputFile, logData, { flag: 'w' });

    core.info('Workflow details collected successfully!');
  } catch (error) {
    core.setFailed(`Action failed: ${error.message}`);
  }
}

run();
