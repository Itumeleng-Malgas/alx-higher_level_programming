#!/usr/bin/node

const number = parseInt(process.argv[2]);

if (!isNaN(number)) {
  for (let i = 0; i < number; i++) {
    console.log('X'.repeat(number));
  }
} else {
  console.log('Missing size');
}
