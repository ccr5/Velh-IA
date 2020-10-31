import { Document } from 'mongoose'
import { IPlayer } from './IPlayer'

export interface IMultiAgentSystem extends Document {
  family: IPlayer[],
  religion: IPlayer[],
  education: IPlayer[]
}
