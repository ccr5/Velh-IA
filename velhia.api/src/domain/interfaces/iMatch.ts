import { Document } from 'mongoose'
import { status } from '@enums/status'
import { winner } from '@enums/winners'
import { IPlay } from '@interfaces/iPlay'
import { IMultiAgentSystem } from '@interfaces/iMultiAgentSystem'
import { IPlayer } from '@interfaces/iPlayer'

interface IMatch extends Document {
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

interface IMatchRepository {
  getAllMatch(): Promise<IMatch[] | null>
  getOneMatch(id: string): Promise<IMatch | null>
  getLastMatch(limit: number): Promise<IMatch[] | null>
  createMatch(data: IMatch[]): Promise<IMatch[]>
  updateMatch(data: IMatch): Promise<IMatch | null>
  deleteMatch(id: string): Promise<IMatch | null>
}

export { IMatch, IMatchRepository }
