const http = require('http');

const sv = http.createServer((req, res) => {
    res.end('This is a attach test.');
});

sv.listen(3000, () => {
    console.log("Server is on listening on 3k.");
});