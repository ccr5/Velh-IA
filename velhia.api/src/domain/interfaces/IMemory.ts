import { Document } from 'mongoose'
import { environmentReaction } from '@enums/environmentReaction'
import { IChoices } from './IChoices'

export interface IMemory extends Document {
  isLearner: boolean,
  choices: IChoices[],
  environmentReaction: environmentReaction
}
