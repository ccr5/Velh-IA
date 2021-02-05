import Match from "src/entities/match/match";

export default interface IMatchUseCase {
  getMatch(
    filters:string | undefined, 
    fields: string | undefined, 
    sort: string | undefined, 
    offset: string | undefined, 
    limit: string | undefined): Promise<Match[] | null>
  createMatch(data: Match[]): Promise<Match[]>
  updateMatch(id: string, data: Match): Promise<Match | null>
  deleteMatch(id: string): Promise<Match | null>
}