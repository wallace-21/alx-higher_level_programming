#!/usr/bin/node

const fs = require('node:fs');
const request = require('request');
const args = process.argv;

request(args[2]).pipe(fs.createWriteStream(args[3]));
