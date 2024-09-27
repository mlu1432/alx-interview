#!/usr/bin/node
/*
 * A script that prints all characters of a Star Wars movie:
 * The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
 * Display one character name per line in the same order as the “characters” list in the /films/ endpoint
 * You must use the Star Wars API and the request module.
 */


const request = require('request');


function fetchCharacterName(url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body.name);
      }
    });
  });
}

function fetchMovieCharacters(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  request(url, { json: true }, async (error, response, body) => {
    if (error) {
      return console.error(error);
    }

    for (const characterUrl of body.characters) {
      const name = await fetchCharacterName(characterUrl);
      console.log(name);
    }
  });
}

const movieId = process.argv[2];
fetchMovieCharacters(movieId);
