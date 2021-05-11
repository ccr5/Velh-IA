import { Document } from 'mongoose'
import IMatch from '@entities/match/iMatch';

export default interface IMatchDB extends IMatch, Document {
  
}