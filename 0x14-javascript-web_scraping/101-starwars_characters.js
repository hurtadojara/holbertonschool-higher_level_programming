#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const getRequest = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        console.error(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};
async function actorsFunction () {
  const result = await getRequest(url);
  for (const actor of result.characters) {
    const name = await getRequest(actor);
    console.log(name.name);
  }
}
actorsFunction();
