#!/usr/bin/node

const fs = require('node:fs');
const path = process.argv;

fs.writeFile(path[2], path[3], 'utf-8', (error) => {
  if (error) {
    console.error(error);
  }
});
