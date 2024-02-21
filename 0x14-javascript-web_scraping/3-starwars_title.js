#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

request(`https://swapi-api.hbtn.io/api/films/${id}`, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const res = JSON.parse(body);
    console.log(res.title);
  }
});
