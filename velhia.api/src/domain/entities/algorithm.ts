import { Schema, model } from 'mongoose'
import { IAlgorithm } from '@interfaces/iAlgorithm'
import { environmentReaction } from '@enums/environmentReaction'

const AlgorithmSchema: Schema = new Schema<IAlgorithm>(
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

const Algorithm = model<IAlgorithm>('algorithm', AlgorithmSchema)

export { Algorithm }
