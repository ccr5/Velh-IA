import { status } from '@shared/enums/status'
import { symbolEnvironment } from '@shared/enums/symbols'
import { winner } from '@shared/enums/winners'
import { Schema, model } from 'mongoose'
import iMatchDB from '../interfaces/iMatchDB'

const matchSchema: Schema = new Schema<iMatchDB> (
  {
    begin: { type: Date, required: true },
    end: { type: Date },
    time: { type: Number, required: true },
    sa: {
      playerId: { type: String, required: true },
      symbol: {
        type: String,
        required: true,
        enum: Object.values(symbolEnvironment)
      }
    },
    mas: {
      family: [{
        playerId: { type: String, required: true },
        symbol: {
          type: String,
          required: true,
          enum: Object.values(symbolEnvironment)
        }
      }],
      religion: [{
        playerId: { type: String, required: true },
        symbol: {
          type: String,
          required: true,
          enum: Object.values(symbolEnvironment)
        }
      }],
      education: [{
        playerId: { type: String, required: true },
        symbol: {
          type: String,
          required: true,
          enum: Object.values(symbolEnvironment)
        }
      }]
    },
    plays: [{
      seq: { type: Number, required: true },
      player: { type: String, required: true },
      time: { type: Number, required: true },
      position: { type: Number, required: true }
    }],
    status: {
      type: String,
      required: true,
      enum: Object.values(status)
    },
    winner: {
      type: String,
      enum: Object.values(winner)
    }
  },
  {
    timestamps: true
  }
)

const MatchDB = model<iMatchDB>('match', matchSchema)

export default  MatchDB
