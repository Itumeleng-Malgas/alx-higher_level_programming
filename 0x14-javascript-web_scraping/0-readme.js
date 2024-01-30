#!/usr/bin/node

const fs = require('fs');
if (process.argv.length !== 3) {
  console.error('Usage: node 0-readme.js <file-path>');
  process.exit(1);
}

function handleFileRead (err, data) {
  if (!err) {
    console.log(data);
  }
}

const filePath = process.argv[2];
fs.readFile(filePath, 'utf-8', handleFileRead);
