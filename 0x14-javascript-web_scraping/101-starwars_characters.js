#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

let characterUrls = [];

// Fetch and print character names from the given index.
function fetchCharacter(index) {
  if (index >= characterUrls.length) {
    return;
  }

  request(characterUrls[index], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }

    const characterContent = JSON.parse(body);
    console.log(characterContent.name);

    fetchCharacter(index + 1);
  });
}

request.get(filmUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const filmData = JSON.parse(body);
  characterUrls = filmData.characters;
  fetchCharacter(0);
});
