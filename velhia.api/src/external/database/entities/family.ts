import { environmentReaction } from '@utils/enums/environmentReaction'
import { Schema, model } from 'mongoose'

const FamilySchema: Schema = new Schema (
  {
    progenitor: { type: String, required: true },
    birth: { type: Date, required: true },
    becomeLeader: { type: Date },
    death: { type: Date },
    life: { type: Number, required: true },
    memory: [{
      matchId: { type: String, required: true },
      isLearner: { type: Boolean, required: true },
      choices: [{
        dateRequest: { type: Date, required: true },
        gameStatus: { type: Array, required: true },
        timeToAct: { type: Number, required: true },
        action: { type: Number, required: true }
      }],
      environmentReaction: {
        type: String,
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

const FamilyDB = model('family', FamilySchema)

export default  FamilyDB
