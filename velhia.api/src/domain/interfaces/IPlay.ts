import { Document } from 'mongoose'

export interface IPlay extends Document {
  seq: number,
  player: string,
  time: number,
  position: number
}
