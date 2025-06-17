const core = require('@actions/core');
const fs = require('fs');
const path = require('path');
const { getWorkflowDetails } = require('./lib/workflowUtils');

async function run() {
  try {
    // Input parameters from the workflow file
    const loggingLevel = core.getInput('logging_level') || 'info';
    const outputFile = core.getInput('output_file') || './workflow_output.txt';

    // Get Workflow Details: start time, input params, etc.
    const workflowDetails = await getWorkflowDetails(loggingLevel);
    
    // Write the captured details to the output file
    fs.writeFileSync(path.resolve(outputFile), workflowDetails, 'utf8');
    
    core.info('Workflow details captured successfully!');
  } catch (error) {
    core.setFailed(error.message);
  }
}

run();
