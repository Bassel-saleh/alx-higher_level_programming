#!/usr/bin/node
let len = 0;
exports.logMe = function (item) {
  console.log(`${len}: ${item}`);
  len++;
};
