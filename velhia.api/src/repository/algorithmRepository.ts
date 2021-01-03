import { IAlgorithmRepository, IAlgorithm } from '@interfaces/iAlgorithm'
import { Algorithm } from 'src/domain/entities/algorithm'

export class AlgorithmRepository implements IAlgorithmRepository {
  /**
   * Get All Statistical Algorithm in the database
   * @example getAllAlgorithm()
   * @returns {Promise<IAlgorithm[] | null>} IAlgorithm[] | null
   */
  async getAlgorithm(
    filters:string | undefined, 
    fields: string | undefined, 
    sort: string | undefined, 
    offset: string | undefined, 
    limit: string| undefined): Promise<IAlgorithm[] | null> {

      let fieldsString = ''
      if (fields != undefined) {
        fields.split(',').forEach((field: string) => {
          fieldsString += ` ${field}`
        })
      } 

      let sortList = new Array
      if (sort != undefined) {
        sort.split(':').forEach((field: string) => {
          if (field == 'asc') {
            sortList.push(1)
          } else if (field == 'desc') {
            sortList.push(-1)
          } else {
            sortList.push(field)
          }
        })
      }

      const ret = await Algorithm.find(
        filters != undefined ? JSON.parse(filters) : {},
        fieldsString
      )
      .sort([sortList])
      .skip(offset != undefined ? +offset : +'')
      .limit(limit != undefined ? +limit : +'')

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
