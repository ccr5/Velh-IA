import { IAgentRepository, IAgent } from '@interfaces/iAgent'
import { Education } from '@entities/education'

export class EducationRepository implements IAgentRepository {
  async getAllAgent (): Promise<IAgent[] | null> {
    const ret = await Education.find()
    return ret
  }

  /**
   * Get a agent in the database by id
   * @param {string} id Education hash already saved in the database
   * @example getOneEducation("11bf9688-699f-49a4-9d8e-b0cc57301bff") // {
   *  id: hash
   *  size: Education's size,
   *  filePath: path where this file was saved,
   *  name: Education's original name
   *  format: Education's format (Ex: "PNG")
   * }
   * @returns {Promise<IEducation | null>} ret
   */
  async getOneAgent (id: string): Promise<IAgent | null> {
    const ret = await Education.findById(id)
    return ret
  }

  /**
   * save a new Education in the database
   * @param {IAgent[]} data IEducation array
   * @example createEducation({
   *  id: hash
   *  size: Education's size,
   *  filePath: path where this file was saved,
   *  name: Education's original name
   *  format: Education's format (Ex: "PNG")
   * })
   * @returns {Promise<IAgent[]>} ret
   */
  async createAgent (data: IAgent[]): Promise<IAgent[]> {
    const ret = await Education.create(data)
    return ret
  }

  async updateAgent (data: IAgent): Promise<IAgent> {
    throw new Error('Method not implemented.')
  }

  async deleteAgent (id: string): Promise<IAgent | null> {
    throw new Error('Method not implemented.')
  }
}