import { IAlgorithmRepository, IAlgorithm } from '@interfaces/iAlgorithm'
import { Algorithm } from 'src/domain/entities/algorithm'

export class AlgorithmRepository implements IAlgorithmRepository {
  async getAllAlgorithm (): Promise<IAlgorithm[] | null> {
    const ret = await Algorithm.find()
    return ret
  }

  /**
   * Get a Algorithm in the database by id
   * @param {string} id Algorithm hash already saved in the database
   * @example getOneAlgorithm("11bf9688-699f-49a4-9d8e-b0cc57301bff") // {
   *  id: hash
   *  size: Algorithm's size,
   *  filePath: path where this file was saved,
   *  name: Algorithm's original name
   *  format: Algorithm's format (Ex: "PNG")
   * }
   * @returns {Promise<IAlgorithm | null>} ret
   */
  async getOneAlgorithm (id: string): Promise<IAlgorithm | null> {
    const ret = await Algorithm.findById(id)
    return ret
  }

  /**
   * save a new Algorithm in the database
   * @param {IAlgorithm[]} data IAlgorithm array
   * @example createAlgorithm({
   *  id: hash
   *  size: Algorithm's size,
   *  filePath: path where this file was saved,
   *  name: Algorithm's original name
   *  format: Algorithm's format (Ex: "PNG")
   * })
   * @returns {Promise<IAlgorithm[]>} ret
   */
  async createAlgorithm (data: IAlgorithm[]): Promise<IAlgorithm[]> {
    const ret = await Algorithm.create(data)
    return ret
  }

  async updateAlgorithm (data: IAlgorithm): Promise<IAlgorithm> {
    throw new Error('Method not implemented.')
  }

  async deleteAlgorithm (id: string): Promise<IAlgorithm | null> {
    throw new Error('Method not implemented.')
  }
}
