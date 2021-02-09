import { inject, injectable } from 'tsyringe'
import IAgentUseCase from './iAgentUseCase'
import IAgentRepository from '@useCases/multiAgentSystem/iAgentRepository'
import IAgent from '@entities/multiAgentSystem/iAgent'
import TYPES from '@external/container/types'

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
    limit: string| undefined): Promise<IAgent[] | null> {

      try {
        const ret: IAgent[] | null = await this.repository.getAgent(filters,fields,sort,offset,limit)
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
  async createAgent(data: IAgent[]): Promise<IAgent[]> {
    try {
      const ret: IAgent[] = await this.repository.createAgent(data)
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
  async updateAgent(id: string, data: IAgent): Promise<IAgent | null> {
    try {
      const ret: IAgent | null = await this.repository.updateAgent(id, data)
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
  async deleteAgent(id: string): Promise<IAgent | null> {
    try {
      const ret: IAgent | null = await this.repository.deleteAgent(id)
      return ret
    } catch (error) {
      throw new Error(error);    
    }
  }
}