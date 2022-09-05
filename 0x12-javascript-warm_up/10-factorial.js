#!/usr/bin/node
const arg = process.argv[2];
if (!arg) {
  console.log(1);
} else {
  console.log(factorial(arg));
}
function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
