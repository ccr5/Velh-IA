import { inject, injectable } from 'tsyringe'
import IAgentUseCase from './iAgentUseCase'
import IAgentRepository from 'src/adapters/repository/iAgentRepository'
import Agent from 'src/entities/multiAgentSystem/agent'
import TYPES from '@utils/types'

@injectable()
export default class ReligionUseCase implements IAgentUseCase {
  private repository: IAgentRepository

  constructor(@inject(TYPES.ReligionRepository) agentRepository: IAgentRepository) {
    this.repository = agentRepository
  }

  /**
   * Get All Agents in the database
   * @example getAllAgent()
   * @returns {Promise<IAgent[] | null>} IAgent[] | null
   */
  async getAgent(
    filters:string | undefined, 
    fields: string | undefined, 
    sort: string | undefined, 
    offset: string | undefined, 
    limit: string| undefined): Promise<Agent[] | null> {

      try {
        const ret: Agent[] | null = await this.repository.getAgent(filters,fields,sort,offset,limit)
        return ret
      } catch (error) {
        throw new Error(error);
      }   
  }

  /**
   * save a new Agent in the database
   * @param {IAgent[]} data IAgent[]
   * @example createAgent(IAgent[] "without id" )
   * @returns {Promise<IAgent[]>} IAgent[] with id
   */
  async createAgent(data: Agent[]): Promise<Agent[]> {
    try {
      const ret: Agent[] = await this.repository.createAgent(data)
      return ret
    } catch (error) {
      throw new Error(error);
    }
    
  }

  /**
   * update a saved Agent in the database
   * @param {string} id ObjectId
   * @param {IAgent} data IAgent
   * @example updateAgent("11bf9688-699f-49a4-9d8e-b0cc57301bff", IAgent)
   * @returns {Promise<IAgent | null>} IAgent | null
   */
  async updateAgent(id: string, data: Agent): Promise<Agent | null> {
    try {
      const ret: Agent | null = await this.repository.updateAgent(id, data)
      return ret
    } catch (error) {
      throw new Error(error);
    }
  }

  /**
   * delete a saved Agent in the database
   * @param {string} id ObjectId
   * @example deleteAgent('11bf9688-699f-49a4-9d8e-b0cc57301bff')
   * @returns {Promise<IAgent | null>} IAgent | null
   */
  async deleteAgent(id: string): Promise<Agent | null> {
    try {
      const ret: Agent | null = await this.repository.deleteAgent(id)
      return ret
    } catch (error) {
      throw new Error(error);    
    }
  }
}