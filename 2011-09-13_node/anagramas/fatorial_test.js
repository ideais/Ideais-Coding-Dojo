var assert = require('assert');
var fatorial = require('./fatorial');

exports['testa n menor ou igual a 2'] = function() {
    assert.equal(2, fatorial.calcula(2))
    assert.equal(1, fatorial.calcula(1))
}();

exports['testa fatorial de 3'] = function() {
    assert.equal(6, fatorial.calcula(3))
}();

exports['testa fatorial de 4'] = function() {
    assert.equal(24, fatorial.calcula(4))
}();
