#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

/**
 * Processes an array of tasks and computes the number of completed tasks per user.
 */
function processData(tasks) {
  const completedTaskCount = {};

  tasks.forEach(task => {
    if (task.completed) {
      if (!completedTaskCount[task.userId]) {
        completedTaskCount[task.userId] = 0;
      }
      completedTaskCount[task.userId]++;
    }
  });

  return completedTaskCount;
}

request(url, (error, response, body) => {
  if (error) {
    console.error('Request error:', error);
    process.exit(1);
  }

  try {
    const tasks = JSON.parse(body);
    const result = processData(tasks);

    console.log(result);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
    process.exit(1);
  }
});
