import { IAgentRepository, IAgent } from '@interfaces/iAgent'
import { Family } from '@entities/family'

export class FamilyRepository implements IAgentRepository {
  /**
   * Get All Agents in the database
   * @example getAllAgent()
   * @returns {Promise<IAgent[] | null>} IAgent[] | null
   */
  async getAllAgent(): Promise<IAgent[] | null> {
    const ret = await Family.find()
    return ret
  }

  /**
   * Get a Agent in the database by id
   * @param {string} id ObjectId
   * @example getOneAgent("11bf9688-699f-49a4-9d8e-b0cc57301bff")
   * @returns {Promise<IAgent | null>} IAgent | null
   */
  async getOneAgent(id: string): Promise<IAgent | null> {
    const ret = await Family.findById(id)
    return ret
  }

  /**
   * Get a limit X of Agents in the database by id in desc order
   * @param {number} limit number
   * @example getLastAgent(2)
   * @returns {Promise<IAgent[] | null>} IAgent[2] | null
   */
  async getLastAgent(limit: number): Promise<IAgent[] | null> {
    const ret = await Family.find({}).sort({ createdAt: 'desc' }).limit(limit)
    return ret
  }

  /**
   * save a new Agent in the database
   * @param {IAgent[]} data IAgent[]
   * @example createAgent(IAgent[] "without id" )
   * @returns {Promise<IAgent[]>} IAgent[] with id
   */
  async createAgent(data: IAgent[]): Promise<IAgent[]> {
    const ret = await Family.create(data)
    return ret
  }

  /**
   * update a saved Agent in the database
   * @param {string} id ObjectId
   * @param {IAgent} data IAgent
   * @example updateAgent("11bf9688-699f-49a4-9d8e-b0cc57301bff", IAgent)
   * @returns {Promise<IAgent | null>} IAgent | null
   */
  async updateAgent(id: string, data: IAgent): Promise<IAgent | null> {
    const ret = await Family.findByIdAndUpdate(id, data)
    return ret
  }

  /**
   * delete a saved Agent in the database
   * @param {string} id ObjectId
   * @example deleteAgent('11bf9688-699f-49a4-9d8e-b0cc57301bff')
   * @returns {Promise<IAgent | null>} IAgent | null
   */
  async deleteAgent(id: string): Promise<IAgent | null> {
    const ret = await Family.findByIdAndDelete(id)
    return ret
  }
}
