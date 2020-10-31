import { IMatchRepository, IMatch } from '@interfaces/iMatch'
import { Match } from '@entities/matchs'

export class MatchRepository implements IMatchRepository {
  async getAllMatch(): Promise<IMatch[] | null> {
    const ret = await Match.find()
    return ret
  }

  /**
   * Get a Match in the database by id
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
  async getOneMatch(id: string): Promise<IMatch | null> {
    const ret = await Match.findById(id)
    return ret
  }

  getLastMatch(limit: number): Promise<IMatch[] | null> {
    throw new Error("Method not implemented.")
  }

  /**
   * save a new Education in the database
   * @param {IMatch[]} data IEducation array
   * @example createEducation({
   *  id: hash
   *  size: Education's size,
   *  filePath: path where this file was saved,
   *  name: Education's original name
   *  format: Education's format (Ex: "PNG")
   * })
   * @returns {Promise<IMatch[]>} ret
   */
  async createMatch(data: IMatch[]): Promise<IMatch[]> {
    const ret = await Match.create(data)
    return ret
  }

  async updateMatch(data: IMatch): Promise<IMatch> {
    throw new Error('Method not implemented.')
  }

  async deleteMatch(id: string): Promise<IMatch | null> {
    throw new Error('Method not implemented.')
  }
}
