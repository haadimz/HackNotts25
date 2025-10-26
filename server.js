const express = require('express');//uses express package to create server
const path = require('path');//uses path package to let the user interact with files
const app = express();//actually creates the server using express
const port = 3000;//the port i chose to run server from - can be changed if used on a host using multiple ports already

app.use(express.static(path.join(__dirname, 'public')));//serves static files from public folder - html files,css

//const routes = require('/Routers'); // add this after the routing is needed - if not delete
//app.use('/', routes);

app.get('/', (req, res) => { //route for the home page
    res.sendFile(path.join(__dirname, 'public', 'index.html'));//sends the html of the home page
});



app.listen(port, () => {//Checks server is running properly - if msg no appear server no worky
    console.log(`Server is running at http://localhost:${port}`);
});