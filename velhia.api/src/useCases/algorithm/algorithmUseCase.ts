import { inject, injectable } from 'tsyringe'
import TYPES from '@external/container/types'
import IAlgorithm from '@entities/algorithm/iAlgorithm'
import IAlgorithmUseCase from './iAlgorithmUseCase'
import IAlgorithmRepository from '@useCases/algorithm/iAlgorithmRepository'

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
    ): Promise<IAlgorithm[] | null> {

    try {

      const sa: IAlgorithm[] | null = await this.repository.getAlgorithm(filters, fields, sort, offset, limit)
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
  async createAlgorithm(data: IAlgorithm[]): Promise<IAlgorithm[]> {
    try {
      const sas: IAlgorithm[] = await this.repository.createAlgorithm(data)
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
  async updateAlgorithm(id: string, data: IAlgorithm): Promise<IAlgorithm | null> {
    try {
      const sas: IAlgorithm | null = await this.repository.updateAlgorithm(id, data)
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
  async deleteAlgorithm(id: string): Promise<IAlgorithm | null> {
    try {
      const sas: IAlgorithm | null = await this.repository.deleteAlgorithm(id)
      return sas
    } catch (error) {
      throw new Error(error);
    }
  }
}
