#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const movieContent = JSON.parse(body);
  const characterUrls = movieContent.characters;

  characterUrls.forEach(url => {
    request(url, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }

      const characterContent = JSON.parse(body);
      console.log(characterContent.name);
    });
  });
});
