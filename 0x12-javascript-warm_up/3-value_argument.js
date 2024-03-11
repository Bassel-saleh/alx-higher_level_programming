#!/usr/bin/node
const x = process.argv[2]
if (x != undefined) {
  console.log(x);
} else {
  console.log('No argument');
}