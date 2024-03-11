#!/usr/bin/node
const x = process.argv.length;
if (x === 2) {
  console.log('No arguments');
} else if (x === 3) {
  console.log('Argument Found');
} else {
  console.log('Arguments Found');
}
