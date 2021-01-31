import { Document } from 'mongoose'
import { IPlayer } from './iPlayer'

export interface IMultiAgentSystem extends Document {
  family: IPlayer[],
  religion: IPlayer[],
  education: IPlayer[]
}
