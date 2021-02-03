#!/usr/bin/node
if (isNaN(parseInt(process.argv[2])) === false) {
  const i = parseInt(process.argv[2]);
  let j = 0;
  while (j < i) {
    console.log('C is fun');
    j++;
  }
} else {
  console.log('Missing number of occurrences');
}
