import IAgent from "@entities/multiAgentSystem/iAgent";

export default interface IAgentRepository {
  getAgent(
    filters:string | undefined, 
    fields: string | undefined, 
    sort: string | undefined, 
    offset: string | undefined, 
    limit: string | undefined): Promise<IAgent[] | null>
  createAgent(data: IAgent[]): Promise<IAgent[]>
  updateAgent(id: string, data: IAgent): Promise<IAgent | null>
  deleteAgent(id: string): Promise<IAgent | null>
}
