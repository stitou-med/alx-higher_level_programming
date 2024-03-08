#!/usr/bin/node
function nextMax (arr) {
  if (arr.length <= 3) {
    return (0);
  } else {
    const arr1 = arr.map(Number).slice(2, arr.length);
    const max1 = Math.max(...arr1);
    const newarr = arr1.filter(number => number !== max1);
    const max2 = Math.max(...newarr);
    return (max2);
  }
}

const myarr = process.argv;
console.log(nextMax(myarr));
