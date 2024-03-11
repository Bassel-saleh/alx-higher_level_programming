#!/usr/bin/node
const n = parseInt(process.argv[2]);
let i;
if (!isNaN(n)) {
  for (i = 0; i < n; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
