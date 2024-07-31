#!/usr/bin/node

'use strict';

const fs = require('fs');
const filename = process.argv[2];

fs.readFile(filename, 'utf-8', (error, content) => {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
