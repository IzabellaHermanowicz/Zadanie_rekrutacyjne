'use strict';

const fs = require('fs');

function getItems(X){
fs.readFile('12.json', (err, data) => {
    let n=0
    if (err) throw err;
    let real_json = JSON.parse(data);
    for(let key1 in real_json) {
        for(let key2 in real_json[key1]) {
          for(let key3 in real_json[key1][key2]) {
            n+=1
            if (n%4==0)  {
                if(real_json[key1][key2][key3]<X){
                    console.log(real_json[key1][key2]);
                }
            }
          }
        }
      }
});}

getItems(5);
