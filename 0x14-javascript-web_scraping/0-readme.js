#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (error, fileContent) => {
  if (error) {
    console.log(error);
  } else {
    console.log(fileContent);
  }
});
