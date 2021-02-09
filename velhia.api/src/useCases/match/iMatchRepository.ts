import IMatch from "@entities/match/iMatch";

export default interface IMatchRepository {
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