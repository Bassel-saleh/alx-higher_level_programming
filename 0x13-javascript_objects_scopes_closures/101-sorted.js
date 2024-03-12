#!/usr/bin/node
const dict = require('./101-data').dict;
const entries = Object.entries(dict);
const values = Object.values(dict);
const UniqueV = [...new Set(values)];
const newDict = {};
for (const i in UniqueV) {
  const list = [];
  for (const j in entries) {
    if (entries[j][1] === UniqueV[i]) {
      list.unshift(entries[j][0]);
    }
  }
  newDict[UniqueV[i]] = list;
}
console.log(newDict);
