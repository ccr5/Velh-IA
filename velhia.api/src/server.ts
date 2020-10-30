import * as dotenv from 'dotenv'
// import './config/container'
import { database } from '@config/databaseConfig'
import { app } from './app'

dotenv.config({
  path: process.env.NODE_ENV === 'test' ? '.env.test' : '.env'
})

const port = process.env.PORT || 3000

database
  .then(() => {
    console.log('Successfully connected to the database')
  })
  .catch((err) => {
    console.log('Could not connect to the database. Exiting now...\n', err)
    process.exit()
  })

app.listen(port, () => {
  console.log(`Listening on port: ${port}`)
})
