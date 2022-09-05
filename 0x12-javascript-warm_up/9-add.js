#!/usr/bin/node
const arg = parseInt(process.argv[2]);
const arg1 = parseInt(process.argv[3]);
if (!arg) {
    console.log('NaN');
} else if (!arg1) {
    console.log('NaN');
} else {
    add(arg, arg1);
}

function add(a, b) {
    console.log(a + b);
}
