import { IMatchRepository, IMatch } from '@interfaces/iMatch'
import { Match } from '@entities/matchs'

export class MatchRepository implements IMatchRepository {
  /**
   * Get All Matchs in the database
   * @example getAllMatch()
   * @returns {Promise<IMatch[] | null>} IMatch[] | null
   */
  async getAllMatch(): Promise<IMatch[] | null> {
    const ret = await Match.find()
    return ret
  }

  /**
   * Get a Match in the database by id
   * @param {string} id ObjectId
   * @example getOneMatch("11bf9688-699f-49a4-9d8e-b0cc57301bff")
   * @returns {Promise<IMatch | null>} IMatch | null
   */
  async getOneMatch(id: string): Promise<IMatch | null> {
    const ret = await Match.findById(id)
    return ret
  }

  /**
   * Get a limit X of Matchs in the database by id in desc order
   * @param {number} limit number
   * @example getLastMatch(2)
   * @returns {Promise<IMatch[] | null>} IMatch[2] | null
   */
  async getLastMatch(limit: number): Promise<IMatch[] | null> {
    const ret = await Match.find({}).sort({ createdAt: 'desc' }).limit(limit)
    return ret
  }

  /**
   * save a new Match in the database
   * @param {IMatch[]} data IMatch[]
   * @example createMatch(IMatch[] "without id" )
   * @returns {Promise<IMatch[]>} IMatch[] with id
   */
  async createMatch(data: IMatch[]): Promise<IMatch[]> {
    const ret = await Match.create(data)
    return ret
  }

  /**
   * update a saved Match in the database
   * @param {string} id ObjectId
   * @param {IMatch} data IMatch
   * @example updateMatch("11bf9688-699f-49a4-9d8e-b0cc57301bff", IMatch)
   * @returns {Promise<IMatch | null>} IMatch | null
   */
  async updateMatch(id: string, data: IMatch): Promise<IMatch | null> {
    const ret = await Match.findByIdAndUpdate(id, data)
    return ret
  }

  /**
   * delete a saved Match in the database
   * @param {string} id ObjectId
   * @example deleteMatch('11bf9688-699f-49a4-9d8e-b0cc57301bff')
   * @returns {Promise<IMatch | null>} IMatch | null
   */
  async deleteMatch(id: string): Promise<IMatch | null> {
    const ret = await Match.findByIdAndDelete(id)
    return ret
  }
}
