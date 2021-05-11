import { inject, injectable } from 'tsyringe'
import IMatchUseCase from './iMatchUseCase'
import IMatch from '@entities/match/iMatch'
import TYPES from '@external/container/types'
import IMatchRepository from '@useCases/match/iMatchRepository'

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
    ): Promise<IMatch[] | null> {

    try {

      const sa: IMatch[] | null = await this.repository.getMatch(filters, fields, sort, offset, limit)
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
  async createMatch(data: IMatch[]): Promise<IMatch[]> {
    try {
      const sas: IMatch[] = await this.repository.createMatch(data)
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
  async updateMatch(id: string, data: IMatch): Promise<IMatch | null> {
    try {
      const sas: IMatch | null = await this.repository.updateMatch(id, data)
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
  async deleteMatch(id: string): Promise<IMatch | null> {
    try {
      const sas: IMatch | null = await this.repository.deleteMatch(id)
      return sas
    } catch (error) {
      throw new Error(error);
    }
  }
}