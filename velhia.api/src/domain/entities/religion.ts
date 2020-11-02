import { Schema, model } from 'mongoose'
import { environmentReaction } from '@enums/environmentReaction'
import { IAgent } from '@interfaces/iAgent'

const ReligionSchema: Schema = new Schema<IAgent>(
  {
    progenitor: { type: String, required: true },
    birth: { type: Date, required: true },
    becomeLeader: { type: Date },
    death: { type: Date },
    life: { type: Number, required: true },
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
    matchsAsLearner: { type: Number, required: true },
    matchsAsLeader: { type: Number, required: true },
    victories: { type: Number, required: true },
    defeats: { type: Number, required: true },
    draw: { type: Number, required: true }
  },
  {
    timestamps: true
  }
)

const Religion = model<IAgent>('religion', ReligionSchema)

export { Religion }
