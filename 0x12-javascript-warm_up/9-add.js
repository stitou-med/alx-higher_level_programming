#!/usr/bin/node
function add (a, b) {
  return (a + b);
}

const vare1 = Number(process.argv[2]);
const vare2 = Number(process.argv[3]);

console.log(add(vare1, vare2));
