#!/usr/bin/node
const line = 'C is fun';
if (isNaN(Math.floor(Number(process.argv[2])))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Math.floor(Number(process.argv[2])); i++) {
    console.log(line);
  }
}
