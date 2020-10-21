const express = require('express');
const app = express();
const http = require('http').Server(app);
const cors = require('cors');
const bodyParser = require('body-parser');
const mysql = require('mysql');
const axios = require('axios');
const execSync = require('child_process').execSync;


var corsOptions = {
  origin: '*',
  optionsSuccessStatus: 200 // some legacy browsers (IE11, various SmartTVs) choke on 204
}

const con = mysql.createConnection({
  host: "localhost",
  user: "admin",
  password: "12345",
  database:"ro",
  multipleStatements: true
});
con.connect((err) => {
  if (err)
    console.log(err)


});
app.use('/', express.static('client'));
app.get('/', (req, res)=>{
    res.sendFile(__dirname + '/client/index.html');

});
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.all('*', cors(corsOptions),function(req, res, next) {
  next();
});
app.post('/login', (req, res)=>{
  const body = req.body;
  axios({
    method: 'post',
    url: 'https://license.enwatmon.de/login',
    data: {
      email: body.email,
      password: body.password
    }
  }).then((e) => {
    res.send({token: e.data.token});
    console.log('nice');
  }).catch(e => console.log(e));

})
app.post('/setvalue', (req, res)=>{
  const body = req.body;
  const id = body.id;
  const value = body.value;
  let sql = `
    UPDATE ro.values SET value=` + con.escape(value) + ` WHERE ID=` + con.escape(id) + ` AND not manual AND not not_set_by_network;
  `
  var ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
//  console.log('von: ' + ip);
  //console.log(sql);
  con.query(sql, (err)=>{
    if (err)
      console.log(err);
    res.send({text:'bit set'})
  })
});
app.post('/getfixedvalue', (req, res)=>{
  let sql = 'SELECT ID as id, Name as name, value, comment FROM ro.values WHERE ID >= 128'

  con.query(sql, (err, result)=>{
    if(err)
      console.log(err);
    if(result)
      res.send({table:result});
  });
});
app.post('/getvalue', (req, res)=>{
  const body = req.body;
  const id = body.id;
  if(!id){
    res.send({value: 0});
    return
  }
  let sql = `
    SELECT value FROM ro.values WHERE ID=` + con.escape(id) + `
  `
  con.query(sql, (err, result)=>{
    if (err)
      console.log(err);

    if(!result){
      console.log('Error', sql);
      res.send({value: 0});

    }

    if(result.length==0)
      console.log(sql);
    res.send({value: result[0].value});
  })
});
app.post('/getsensors', (req, res)=>{
  const body = req.body;
  const token = body.token;

  let sql = `
    SELECT ID as id, type, barcode, name, number FROM sensors;
  `
  con.query(sql, (err, result)=>{
    if(err)
      console.log(err);
    res.send({sensors: result});
  });
});
app.post('/setsensors', (req, res)=>{
  const body = req.body;
  const token = body.token;
  const sensors = body.sensors;

  let sql = ''
  for (var sensor of sensors) {
    sql += `
      UPDATE sensors SET type=` + con.escape(sensor.type) + `,
      barcode=` + con.escape(sensor.barcode) + `,
      name=` + con.escape(sensor.type) + `,
      number=` + con.escape(sensor.number) + `
      WHERE ID=` + con.escape(sensor.id)  + `;
    `
  }
  con.query(sql, (err, result)=>{
    if(err)
      console.log(err);

    res.send('');
  });
});
app.post('/reset', (req, res)=>{
  const to_zero = [2,3,4,44,47,50,37]
  const to_one = [97]
  let to_zero_sql = ''
  let to_one_sql = ''
  for (const item of to_zero) {
    to_zero_sql += ' OR ID=' + con.escape(item)
  }
  for (const item of to_one) {
    to_one_sql += ' OR ID=' + con.escape(item)
  }


  let sql = `
    UPDATE ro.values SET value=0 WHERE ID=-1 ` + to_zero_sql + `;
    UPDATE ro.values SET value=1 WHERE ID=-1 ` + to_one_sql + `;
  `
  con.query(sql, (err, result)=>{
    if(err)
      console.log(err);
  })
});
app.post('/getcurrentstatus', (req, res)=>{
  let sql = `
    SELECT ID, value, comment FROM ro.values WHERE (ID BETWEEN 90 AND 99) AND value=1
  `
  con.query(sql, (err, result)=>{
    if(err)
      console.log(err);
    if(!result)
      return
    const row = result[0]
    res.send({id: row.ID, status:row.comment});
  })
})
app.post('/reboot', (req, res)=>{
  execSync('sudo reboot', (err, stdout, stderr) => {
    if(err)
      console.log('err', err);
    if(stdout)
      console.log(stdout);
  });
})

http.listen(8000, ()=>{
  console.log('listening on *:8000');
});
