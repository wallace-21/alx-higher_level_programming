#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

request.get(`https://swapi-api.hbtn.io/api/films/${id}`, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  const data2 = data.characters;
  for (const i of data2) {
    request.get(i, (error, response, body1) => {
      if (error) {
        console.log(error);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
