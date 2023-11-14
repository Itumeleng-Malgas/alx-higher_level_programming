#!/usr/bin/node

const dict = require('./100-data.js').list;

console.log(dict);
console.log(dict.map((item, index) => item * index));
