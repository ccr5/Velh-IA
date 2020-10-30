import mongoose from 'mongoose'
import * as dotenv from 'dotenv'

dotenv.config({
  path: process.env.NODE_ENV === 'test' ? '.env.test' : '.env'
})

const connectionString =
  process.env.DATABASE_CONNECTION_STRING ||
  'mongodb://localhost:27017/Velhia'

const database = mongoose.connect(connectionString, {
  useNewUrlParser: true,
  useUnifiedTopology: true
})

export { database }
