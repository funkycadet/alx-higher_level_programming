#!/usr/bin/node
const arg = parseInt(process.argv[2]);
if (Number.isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    let j = '';
    for (let k = 0; k < arg; k++) {
      j += 'X';
    }
    console.log(j);
  }
}
