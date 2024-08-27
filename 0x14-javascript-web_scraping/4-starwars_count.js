#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18'; // Wedge Antilles
const characterUrl = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    let moviesCount = 0;

    for (const film of films) {
      for (const characterUrl of film.characters) {
        if (characterUrl.includes(characterId)) {
          moviesCount++;
          break; // Once we find the character in this film
        }
			}}

    console.log(moviesCount);
  }
});
