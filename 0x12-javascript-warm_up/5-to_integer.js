#!/usr/bin/bash
console.log(isNaN(parseInt(process.argv[2])) ? 'Not a number' : 'My number: ' + parseInt(process.argv[2]));
