#!/usr/bin/node

const fs = require('fs');
if (process.argv.length !== 4) {
  console.error('Usage: node 1-writeme.js <file-path> <string-to-write>');
  process.exit(1);
}

function handleFileWrite (err) {
  if (err) {
    console.log(err);
  }
}

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf-8', handleFileWrite);
