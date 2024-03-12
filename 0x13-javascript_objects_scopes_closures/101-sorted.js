#!/usr/bin/node
const dict = require('./101-data').dict;
const entries = Object.entries(dict);
const values = Object.values(dict);
const UniqueV = [...new Set(values)];
const newDict = {};
for (const j in UniqueV) {
  const list = [];
  for (const k in entries) {
    if (entries[k][1] === UniqueV[j]) {
      list.unshift(entries[k][0]);
    }
  }
  newDict[UniqueV[j]] = list;
}
console.log(newDict);
