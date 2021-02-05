import Agent from "src/entities/multiAgentSystem/agent";

export default interface IAgentUseCase {
  getAgent(
    filters:string | undefined, 
    fields: string | undefined, 
    sort: string | undefined, 
    offset: string | undefined, 
    limit: string | undefined): Promise<Agent[] | null>
  createAgent(data: Agent[]): Promise<Agent[]>
  updateAgent(id: string, data: Agent): Promise<Agent | null>
  deleteAgent(id: string): Promise<Agent | null>
}
