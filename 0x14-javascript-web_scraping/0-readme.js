#!/usr/bin/node

const fs = require('node:fs');
const path = process.argv;

fs.readFile(path[2], 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
  } else {
    console.log(data);
  }
});
