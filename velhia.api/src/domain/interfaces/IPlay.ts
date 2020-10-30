import { Document } from 'mongoose'

export interface IPlay extends Document {
  seq: number,
  player: number,
  time: number,
  position: number
}