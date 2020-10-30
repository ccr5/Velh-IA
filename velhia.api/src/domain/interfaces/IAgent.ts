import { Document } from 'mongoose'
import { IMemory } from './IMemory';

export interface IAgent extends Document {
  birth: Date,
  becomeLeader: Date,
  death: Date,
  life: number,
  memory: IMemory[],
  matchsAsLearner: number, 
  matchsAsLeader: number,
  victories: number,
  defeats: number
}