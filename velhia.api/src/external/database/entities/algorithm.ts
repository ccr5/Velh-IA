import { Schema, model, Document, Model } from 'mongoose'
import IAlgorithmDB from '../interfaces/iAlgorithmDB'

const AlgorithmSchema: Schema = new Schema<IAlgorithmDB>(
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

const AlgorithmDB = model<IAlgorithmDB>('algorithm', AlgorithmSchema)

export default AlgorithmDB
