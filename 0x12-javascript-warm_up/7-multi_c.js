#!/usr/bin/node
if (isNaN(parseInt(process.argv[2])) === false) {
  const i = process.argv.length;
  for (const iterator in process.argv) {
    if (i >= iterator) {
      console.log('C is fun');
    }
  }
} else {
  console.log('Missing number of occurrences');
}
