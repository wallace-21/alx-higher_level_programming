#!/usr/bin/node

const request = require('request');
const url = process.argv;

request(url[2], (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
