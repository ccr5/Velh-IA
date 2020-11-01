import { Schema, model } from 'mongoose'
import { IMatch } from '@interfaces/iMatch'
import { symbolEnvironment } from '@enums/symbols'
import { status } from '@enums/status'
import { winner } from '@enums/winners'

const matchSchema: Schema = new Schema<IMatch>(
  {
    begin: { type: Date, required: true },
    end: { type: Date, required: true },
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

const Match = model<IMatch>('match', matchSchema)

export { Match }
