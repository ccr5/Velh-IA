import { Schema, model } from 'mongoose'
import { IAlgorithm } from '@interfaces/iAlgorithm'
import { environmentReaction } from '@enums/environmentReaction'

const AlgorithmSchema: Schema = new Schema<IAlgorithm>(
  {
    birth: { type: Date, required: true },
    memory: [{
      isLearner: { type: Boolean, required: true },
      choices: [{
        dateRequest: { type: Date, required: true },
        gameStatus: { type: Array, required: true },
        timeToAct: { type: Number, required: true },
        action: { type: Number, required: true }
      }],
      environmentReaction: {
        type: String,
        required: true,
        enum: Object.values(environmentReaction)
      }
    }],
    matchs: { type: Number, required: true },
    victories: { type: Number, required: true },
    defeats: { type: Number, required: true },
    draw: { type: Number, required: true }
  }
)

const Algorithm = model<IAlgorithm>('algorithm', AlgorithmSchema)

export { Algorithm }