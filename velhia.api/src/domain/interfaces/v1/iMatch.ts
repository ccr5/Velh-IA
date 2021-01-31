import { Document } from 'mongoose'
import { status } from '@enums/status'
import { winner } from '@enums/winners'
import { IPlay } from '@interfaces/v1/iPlay'
import { IMultiAgentSystem } from '@interfaces/v1/iMultiAgentSystem'
import { IPlayer } from '@interfaces/v1/iPlayer'

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
