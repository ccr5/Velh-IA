import { Schema, model } from 'mongoose'
import { IMatch } from '@interfaces/IMatch'

const matchSchema: Schema = new Schema<IMatch>(
  {
    _id: Number,
    begin: { type: Date, required: true },
    end: { type: Date, required: true },
    name: { type: String, required: true },
    size: { type: Number, required: true },
    format: { type: String, required: true },
    filePath: { type: String, required: true }
  }
)

const Match = model<IMatch>('match', matchSchema)

export { Match }
