const fs = require("fs").promises
const http = require("http")
const path = require("path")

const basePath = path.join(__dirname, process.env.BASE || "swagger")

http.createServer(async (req, res) => {
  try {
    const url = path.join(basePath, req.url)
    if (!url.startsWith(basePath))
      throw new Error(`Possible injection catched ${url}!`)
    const data = await fs.readFile(url)
    res.setHeader("Access-Control-Allow-Origin", "*")
    res.writeHead(200)
    res.end(data)
  } catch (e) {
    res.writeHead(404)
    res.end()
    console.log(e)
  }
}).listen(process.env.PORT || 8000)