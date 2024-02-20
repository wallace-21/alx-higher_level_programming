#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

request(`https://swapi-api.hbtn.io/api/films/${id}`, (error, body) => {
  if (error) {
    console.log(error);
  } else {
    const res = JSON.parse(body);
    console.log(res.title);
  }
});
