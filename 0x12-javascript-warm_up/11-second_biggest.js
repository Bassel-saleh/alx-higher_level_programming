#!/usr/bin/node
const num = process.argv.length;
const a = process.argv.slice(2).map(Number);
let x = -Infinity; let y = -Infinity; let i;
if (num <= 3) {
  console.log(0);
} else {
  for (i = 0; i < (num - 2); i++) {
    if (a[i] > x) {
      y = x;
      x = a[i];
    } else if (a[i] > y) {
      y = a[i];
    }
  }
  console.log(y);
}
