import { IAlgorithmRepository, IAlgorithm } from '@interfaces/iAlgorithm'
import { Algorithm } from 'src/domain/entities/algorithm'

export class AlgorithmRepository implements IAlgorithmRepository {
  /**
   * Get All Statistical Algorithm in the database
   * @example getAllAlgorithm()
   * @returns {Promise<IAlgorithm[] | null>} IAlgorithm[] | null
   */
  async getAllAlgorithm(): Promise<IAlgorithm[] | null> {
    const ret = await Algorithm.find()
    return ret
  }

  /**
   * Get a Statistical Algorithm in the database by id
   * @param {string} id ObjectId
   * @example getOneAlgorithm("11bf9688-699f-49a4-9d8e-b0cc57301bff")
   * @returns {Promise<IAlgorithm | null>} IAlgorithm | null
   */
  async getOneAlgorithm(id: string): Promise<IAlgorithm | null> {
    const ret = await Algorithm.findById(id)
    return ret
  }

  /**
   * Get a limit X of Statistical Algorithms in the database by id in desc order
   * @param {number} limit number
   * @example getLastAlgorithm(2)
   * @returns {Promise<IAlgorithm[] | null>} IAlgorithm[2] | null
   */
  async getLastAlgorithm(limit: number): Promise<IAlgorithm[] | null> {
    const ret = await Algorithm.find({}).sort({ createdAt: 'desc' }).limit(limit)
    return ret
  }

  /**
   * save a new Statistical Algorithm in the database
   * @param {IAlgorithm[]} data IAlgorithm[]
   * @example createAlgorithm(IAlgorithm[] "without id" )
   * @returns {Promise<IAlgorithm[]>} IAlgorithm[] with id
   */
  async createAlgorithm(data: IAlgorithm[]): Promise<IAlgorithm[]> {
    const ret = await Algorithm.create(data)
    return ret
  }

  /**
   * update a saved Statistical Algorithm in the database
   * @param {string} id ObjectId
   * @param {IAlgorithm} data IAlgorithm
   * @example updateAlgorithm("11bf9688-699f-49a4-9d8e-b0cc57301bff", IAlgorithm)
   * @returns {Promise<IAlgorithm | null>} IAlgorithm | null
   */
  async updateAlgorithm(id: string, data: IAlgorithm): Promise<IAlgorithm | null> {
    const ret = await Algorithm.findByIdAndUpdate(id, data)
    return ret
  }

  /**
   * delete a saved Statistical Algorithm in the database
   * @param {string} id ObjectId
   * @example deleteAlgorithm('11bf9688-699f-49a4-9d8e-b0cc57301bff')
   * @returns {Promise<IAlgorithm | null>} IAlgorithm | null
   */
  async deleteAlgorithm(id: string): Promise<IAlgorithm | null> {
    const ret = await Algorithm.findByIdAndDelete(id)
    return ret
  }
}
