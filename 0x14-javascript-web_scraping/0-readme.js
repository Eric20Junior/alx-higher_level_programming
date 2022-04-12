#!/usr/bin/node

let filename = process.argv[2];
const f = require('f');
f.readfile(filename, 'utf8', function (err, data) {
	if (data) {
		console.log(data);
	} else {
		console.log(err);
	}
});
