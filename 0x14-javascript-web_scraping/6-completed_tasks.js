#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Request error:', error);
    process.exit(1);
  }

  try {
    const tasks = JSON.parse(body);
    const completedTaskCount = {};

    // Process the data to count completed tasks per user
    tasks.forEach(task => {
      if (task.completed) {
        if (!completedTaskCount[task.userId]) {
          completedTaskCount[task.userId] = 0;
        }
        completedTaskCount[task.userId]++;
      }
    });

    console.log(completedTaskCount);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
    process.exit(1);
  }
});
