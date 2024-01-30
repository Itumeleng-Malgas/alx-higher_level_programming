#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./2-statuscode.js <url>');
  process.exit(1);
}
const url = process.argv[2];

function handleRequestCallback (err, res) {
  if (!err) {
    console.log(`code: ${res.statusCode}`);
  } else {
    console.log(err);
  }
}

request(url, handleRequestCallback);
