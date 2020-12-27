import { Document } from 'mongoose'
import { environmentReaction } from '@enums/environmentReaction'
import { IChoices } from './iChoices'

export interface IMemory extends Document {
  matchId: string,
  isLearner: boolean,
  choices: IChoices[],
  environmentReaction: environmentReaction
}
