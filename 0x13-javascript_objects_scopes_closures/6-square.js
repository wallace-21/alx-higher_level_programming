#!/usr/bin/node
const Square2 = require('./5-square');

class Square extends Square2 {

  charPrint (c) {
    let charToPrint;
    if (c != undefined) {
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
