#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (this.isValidDimension(w) && this.isValidDimension(h)) {
      this.width = w;
      this.height = h;
    }
  }

  isValidDimension (value) {
    return Number.isInteger(value) && value > 0;
  }
}

module.exports = Rectangle;
