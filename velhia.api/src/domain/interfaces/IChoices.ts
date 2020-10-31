import { Document } from 'mongoose'

export interface IChoices extends Document {
  dateRequest: Date,
  gameStatus: Array<number>,
  timeToAct: number,
  action: number
}
