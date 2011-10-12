var assert = require('assert');
var cheque = require('./cheque');

exports['lendo cheque de um centavo'] = function() {
    assert.equal(0.01, cheque.ler('um centavo'))
}();

exports['lendo cheque de nove centavos'] = function() {
    assert.equal(0.09, cheque.ler('nove centavos'))
}();

exports['lendo cheque de dez centavos'] = function() {
    assert.equal(0.10, cheque.ler('dez centavos'))
}();

exports['lendo cheque de vinte e um centavos'] = function() {
    assert.equal(0.21, cheque.ler('vinte e um centavos'))
}();

exports['lendo cheque de noventa e cinco centavos'] = function() {
    assert.equal(0.95, cheque.ler('noventa e cinco centavos'))
}();

exports['lendo cheque de um real'] = function() {
    assert.equal(1, cheque.ler('um real'))
}();
