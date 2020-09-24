'use strict';

const fs = require('fs');

fs.readFile('12.json', (err, data) => {
    if (err) throw err;
    let real_json = JSON.parse(data);
});

