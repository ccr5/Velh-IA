import { inject, injectable } from 'tsyringe'
import IMatchUseCase from './iMatchUseCase'
import IMatchRepository from 'src/adapters/repository/interfaces/iMatchRepository'
import Match from 'src/entities/match/match'
import TYPES from '@utils/types'

@injectable()
export default class MatchUseCase implements IMatchUseCase {
  private repository: IMatchRepository

  constructor(@inject(TYPES.MatchRepository) matchRepository: IMatchRepository) {
    this.repository = matchRepository
  }

  /** 
   * Receive a get request and
   * return all Statistical Match filter by a query in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example get()
   * @returns {Promise<Response | void>} IMatch[] | 404 
   */
  async getMatch(
    filters: string | undefined, 
    fields: string | undefined, 
    sort: string | undefined, 
    offset: string | undefined, 
    limit: string | undefined
    ): Promise<Match[] | null> {

    try {

      const sa: Match[] | null = await this.repository.getMatch(filters, fields, sort, offset, limit)
      return sa
      
    } catch (error) {
      throw new Error(error);
    }
  }

  /**
   * receive a post request with data to insert a 
   * new Statistical Algorithm in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example create(IAlgorithm[])
   * @returns {Promise<Response | void>} IAlgorithm[]
   */
  async createMatch(data: Match[]): Promise<Match[]> {
    try {
      const sas: Match[] = await this.repository.createMatch(data)
      return sas
    } catch (error) {
      throw new Error(error);
    }
  }

  /**
   * receive a post request with data to insert a 
   * new Statistical Match in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example create(Match[])
   * @returns {Promise<Response | void>} Match[]
   */
  async updateMatch(id: string, data: Match): Promise<Match | null> {
    try {
      const sas: Match | null = await this.repository.updateMatch(id, data)
      return sas
    } catch (error) {
      throw new Error(error);
    }
  }

  /**
   * receive a post request with data to insert a 
   * new Statistical Algorithm in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example create(IAlgorithm[])
   * @returns {Promise<Response | void>} IAlgorithm[]
   */
  async deleteMatch(id: string): Promise<Match | null> {
    try {
      const sas: Match | null = await this.repository.deleteMatch(id)
      return sas
    } catch (error) {
      throw new Error(error);
    }
  }
}