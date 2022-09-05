#!/usr/bin/node
const arg = parseInt(process.argv[2]);
const c = 'C is fun';
if (Number.isNaN(arg)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < arg; i++) {
    console.log(c);
  }
}
