import { Document } from 'mongoose'
import { status } from '@enums/status'
import { winner } from '@enums/winners'
import { IPlay } from '@interfaces/iPlay'
import { IMultiAgentSystem } from '@interfaces/iMultiAgentSystem'
import { IPlayer } from '@interfaces/iPlayer'

interface IMatch extends Document {
  begin: Date,
  end?: Date,
  time: number,
  sa: IPlayer,
  mas: IMultiAgentSystem
  plays: IPlay[],
  status: status,
  winner?: winner
}

interface IMatchRepository {
  getMatch(
    filters:string | undefined, 
    fields: string | undefined, 
    sort: string | undefined, 
    offset: string | undefined, 
    limit: string | undefined): Promise<IMatch[] | null>
  createMatch(data: IMatch[]): Promise<IMatch[]>
  updateMatch(id: string, data: IMatch): Promise<IMatch | null>
  deleteMatch(id: string): Promise<IMatch | null>
}

export { IMatch, IMatchRepository }
