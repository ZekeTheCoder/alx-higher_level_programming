#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    let moviesCount = 0;
    const content = JSON.parse(body);
		const wedgeAntillesUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

    for (const film of content.results) {
      if (film.characters.includes(wedgeAntillesUrl)) {
        moviesCount++;
      }
    }

    console.log(moviesCount);
  }
});
