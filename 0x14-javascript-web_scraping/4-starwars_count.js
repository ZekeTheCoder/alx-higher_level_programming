#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18'; // Wedge Antilles

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let moviesCount = 0;
    const films = JSON.parse(body).results;

    films.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(characterId)) {
          moviesCount += 1;
        }
      });
    });

    console.log(moviesCount);
  }
});
