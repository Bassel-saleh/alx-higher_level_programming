#!/usr/bin/node
exports.esrever = function (list) {
  const tmp = []; let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    tmp[j] = list[i]; j++;
  }
  return tmp;
};
