#!/usr/bin/node
const n = parseInt(process.argv[2]);
let i, j;
if (!isNaN(n)) {
  for (i = 0; i < n; i++) {
    let r = '';
    for (j = 0; j < n; j++) {
      r += 'X';
    }
    console.log(r);
  }
} else {
  console.log('Missing size');
}
