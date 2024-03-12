#!/usr/bin/node
const fs = require('fs');
const array1 = fs.readFileSync(process.argv[2]).toString();
const array2 = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], array1 + array2);
