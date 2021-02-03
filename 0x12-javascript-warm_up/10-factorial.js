#!/usr/bin/node
const num = Number.parseInt(process.argv[2]);
function factorial (number) {
  if (!number) {
    return 1;
  }
  return number * factorial(number - 1);
}
console.log(factorial(num));
