const express = require('express')
const serveStatic = require('serve-static')

const staticBasePath = './public';

const app = express()
const port = 3000

app.use(serveStatic(staticBasePath, {
    'index': 'index.html'
}))
app.listen(port, () => 
    console.log(`Listening on port ${port}!`)
)
