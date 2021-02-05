import { Schema, model, Document, Model } from 'mongoose'
import Algorithm from 'src/entities/algorithm/algorithm'

const AlgorithmSchema: Schema = new Schema<Algorithm>(
  {
    birth: { type: Date, required: true },
    matchs: { type: Number, required: true },
    victories: { type: Number, required: true },
    defeats: { type: Number, required: true },
    draw: { type: Number, required: true }
  },
  {
    timestamps: true
  }
)

const AlgorithmDB = model<Algorithm extends Document>('algorithm', AlgorithmSchema)

export default AlgorithmDB
