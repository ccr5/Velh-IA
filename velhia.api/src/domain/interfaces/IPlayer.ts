import { Document } from 'mongoose'
import { symbolEnvironment } from '@enums/symbols';

export interface IPlayer extends Document {
  id: number,
  symbol: symbolEnvironment
}