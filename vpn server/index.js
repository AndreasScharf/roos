const express = require('express');
const app = express();
const expressip = require('express-ip');
app.use(expressip().getIpInfoMiddleware);

app.get('/', function (req, res) {
    console.log(req.ipInfo);
});

http.listen(8002, ()=>{
  console.log('listening on *:8002');
});
