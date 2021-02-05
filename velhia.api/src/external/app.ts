import 'reflect-metadata'
import express from 'express'
import cors from 'cors'
import bodyParser from 'body-parser'
import { routes } from 'src/external/routes'

const app = express()
const options: cors.CorsOptions = {
  allowedHeaders: [
    'Origin',
    'X-Requested-With',
    'Content-Type',
    'Accept',
    'X-Access-Token'
  ],
  credentials: true,
  methods: 'GET,HEAD,OPTIONS,PUT,PATCH,POST,DELETE',
  origin: '*',
  preflightContinue: true
}

app.use(bodyParser.urlencoded({ limit: '5mb', extended: true }))
app.use(bodyParser.json({ limit: '5mb' }))
app.use(cors(options))
app.use(routes)
app.get('*', (req, res) => {
  res.send({ message: 'Welcome Velh-IA API' })
})

export { app }
