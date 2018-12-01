var fs = require('fs');

fs.stat('file.js', function (err, stats) {
    console.log(stats.isFile());         //true
})