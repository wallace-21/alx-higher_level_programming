#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    let charToPrint;
    if (c !== undefined) {
      charToPrint = c;
    } else {
      charToPrint = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(charToPrint.repeat(this.width));
    }
  }
}

module.exports = Square;
