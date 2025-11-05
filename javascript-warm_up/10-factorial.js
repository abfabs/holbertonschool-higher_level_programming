#!/usr/bin/node
function factorial (n) {
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const num = Number.parseInt(process.argv[2]);
const result = Number.isNaN(num) ? 1 : factorial(num);
console.log(result);
