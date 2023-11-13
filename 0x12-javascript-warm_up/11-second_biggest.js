#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  // Convert arguments to integers and store them in an array
  const numbers = process.argv.slice(2).map(arg => parseInt(arg, 10));

  const sortedNumbers = numbers.sort((a, b) => b - a);
  console.log(sortedNumbers[1]);
}
