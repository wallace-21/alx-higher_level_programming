#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      if (c === undefined) {
        console.log('X'.repeat(this.size));
      } else {
        console.log(c.repeat(this.size));
      }
    }
  }
}

module.exports = Square;
