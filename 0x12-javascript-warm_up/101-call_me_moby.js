#!/usr/bin/node
exports.callMeMoby = function (val, theFunction) {
  for (let i = 0; i < val; i++) {
    theFunction();
  }
};
