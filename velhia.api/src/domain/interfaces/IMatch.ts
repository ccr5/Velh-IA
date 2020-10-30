import { Document } from 'mongoose'
import { status } from '@enums/status'
import { winner } from '@enums/winners'
import { IPlayer } from './IPlayer'
import { IPlay } from './IPlay'

export interface IMatch extends Document {
  begin: Date,
  end: Date,
  players: {
    sa: IPlayer,
    mas: {
      family: IPlayer[],
      religion: IPlayer[],
      education: IPlayer[]
    }
  },
  plays: IPlay[],
  status: status,
  winner: winner
}
