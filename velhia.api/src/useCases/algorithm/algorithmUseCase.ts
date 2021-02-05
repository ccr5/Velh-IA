import { inject, injectable } from 'tsyringe'
import TYPES from '@utils/types'
import Algorithm from 'src/entities/algorithm/algorithm'
import IAlgorithmUseCase from './iAlgorithmUseCase'
import IAlgorithmRepository from 'src/adapters/repository/interfaces/iAlgorithmRepository'

@injectable()
export default class AlgorithmUseCase implements IAlgorithmUseCase {
  private repository: IAlgorithmRepository

  constructor(@inject(TYPES.AlgorithmRepository) algorithmRepository: IAlgorithmRepository) {
    this.repository = algorithmRepository
  }

  /** 
   * Receive a get request and
   * return all Statistical Algorithm filter by a query in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example get()
   * @returns {Promise<Response | void>} IAlgorithm[] | 404 
   */
  async getAlgorithm(
    filters: string | undefined, 
    fields: string | undefined, 
    sort: string | undefined, 
    offset: string | undefined, 
    limit: string | undefined
    ): Promise<Algorithm[] | null> {

    try {

      const sa: Algorithm[] | null = await this.repository.getAlgorithm(filters, fields, sort, offset, limit)
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
  async createAlgorithm(data: Algorithm[]): Promise<Algorithm[]> {
    try {
      const sas: Algorithm[] = await this.repository.createAlgorithm(data)
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
  async updateAlgorithm(id: string, data: Algorithm): Promise<Algorithm | null> {
    try {
      const sas: Algorithm | null = await this.repository.updateAlgorithm(id, data)
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
  async deleteAlgorithm(id: string): Promise<Algorithm | null> {
    try {
      const sas: Algorithm | null = await this.repository.deleteAlgorithm(id)
      return sas
    } catch (error) {
      throw new Error(error);
    }
  }
}
