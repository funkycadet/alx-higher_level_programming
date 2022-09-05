#!/usr/bin/node
const arg = process.argv;
if (!arg[2]) {
  console.log(arg[2] + ' is ' + arg[2]);
} else if (arg[2]) {
  console.log(arg[2] + ' is ' + arg[3]);
}
