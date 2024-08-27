#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(filmUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;
	fetchCharacter(0); // start from index 0


  function fetchCharacter(index) {
    if (index >= characterUrls.length) {
      return; // Base case - If the index is out of bounds, stop the recursion
    }

    request(characterUrls[index], (error, response, body) => {
      if (error) {
				console.log(error);
				return;
			}

      const characterContent = JSON.parse(body);
      console.log(characterContent.name);

      fetchCharacter(index + 1); // process next character
    });
  }
});
