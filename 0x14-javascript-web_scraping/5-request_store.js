#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];


if (!url || !filePath) {
  console.error('Usage: ./5-request_store.js <URL> <file_path>');
  process.exit(1);
}

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
