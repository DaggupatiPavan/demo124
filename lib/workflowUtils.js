const { execSync } = require('child_process');

function getWorkflowDetails(loggingLevel) {
  const startTime = new Date();
  
  // Capture input parameters
  const inputs = process.env.GITHUB_EVENT_PATH;  // This will be JSON containing inputs/parameters
  const inputsData = require(inputs);
  
  // Log level mapping
  const logLevels = {
    'debug': 'DEBUG',
    'info': 'INFO',
    'error': 'ERROR'
  };

  const logOutput = `Logging Level: ${logLevels[loggingLevel] || 'INFO'}\n`;

  // Capture stdout and stderr
  const workflowOutput = captureWorkflowOutput();

  const endTime = new Date();
  const duration = endTime - startTime; // duration in ms

  const result = `
    === Workflow Details ===
    Start Time: ${startTime}
    End Time: ${endTime}
    Duration: ${duration}ms
    ${logOutput}
    Inputs: ${JSON.stringify(inputsData)}
    Workflow Output:
    ${workflowOutput}
  `;

  return result;
}

function captureWorkflowOutput() {
  try {
    // Capture the stdout and stderr
    const stdout = execSync('echo "Workflow Executed Successfully"'); // Replace with actual workflow command
    const stderr = execSync('echo "Error: Sample stderr"'); // Replace with actual error capturing
    return `STDOUT: ${stdout.toString()}\nSTDERR: ${stderr.toString()}`;
  } catch (error) {
    return `Error during execution: ${error.message}`;
  }
}

module.exports = { getWorkflowDetails };
