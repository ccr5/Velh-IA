import { Document } from 'mongoose'
import { IMemory } from '@interfaces/IMemory'

export interface IAlgorithm extends Document {
  id: string,
  birth: Date,
  memory: IMemory[]
  matchs: number,
  victories: number,
  defeats: number,
  draw: number
}
