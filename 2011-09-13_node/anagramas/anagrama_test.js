var assert = require('assert');
var clazz = require('./anagrama');

exports['testa menor anagrama possivel'] = function() {
    assert.deepEqual(['ab', 'ba'].sort(), clazz.anagrama('ab'))
}();

exports['testa primeiro anagrama de 3 letras'] = function() {
    assert.deepEqual(["bac","cab","cba","bca","abc","acb"].sort(), clazz.anagrama('abc'))
}();

exports['teste do biro'] = function() {
    assert.deepEqual(["biro","bior","brio","broi",
    "boir","bori","ibro","ibor",
    "irbo","irob","iobr","iorb","rbio",
    "rboi","ribo","riob","roib",
    "robi","obir","obri","oibr",
    "oirb","orbi","orib"].sort(), clazz.anagrama("biro"))
}();
