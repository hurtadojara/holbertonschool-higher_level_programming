#!/usr/bin/node
let numbers = process.argv;
if (numbers.length > 3) {
  numbers = numbers.slice(2).map(number => Number.parseInt(number)).sort((a, b) => a - b);
  console.log(numbers[numbers.length - 2]);
} else {
  console.log(0);
}
