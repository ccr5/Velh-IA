import { Document } from 'mongoose'
import { status } from '@enums/status'
import { winner } from '@enums/winners'
import { IPlay } from '@interfaces/IPlay'
import { IMultiAgentSystem } from '@interfaces/IMultiAgentSystem'
import { IPlayer } from '@interfaces/IPlayer'

export interface IMatch extends Document {
  id: string,
  begin: Date,
  end: Date,
  time: number,
  sa: IPlayer,
  mas: IMultiAgentSystem
  plays: IPlay[],
  status: status,
  winner: winner
}
