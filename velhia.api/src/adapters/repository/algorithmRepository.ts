import AlgorithmDB from 'src/external/database/entities/algorithm'
import Algorithm from 'src/entities/algorithm/algorithm'
import IAlgorithmRepository from './iAlgorithmRepository'


export default class AlgorithmRepository implements IAlgorithmRepository {

  /**
   * Get All Statistical Algorithm in the database
   * @example getAllAlgorithm()
   * @returns {Promise<Algorithm[] | null>} IAlgorithm[] | null
   */
  async getAlgorithm(
    filters:string | undefined, 
    fields: string | undefined, 
    sort: string | undefined, 
    offset: string | undefined, 
    limit: string| undefined): Promise<Algorithm[] | null> {

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

      const ret = await AlgorithmDB.find(
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
   * @param {Algorithm[]} data Algorithm[]
   * @example createAlgorithm(Algorithm[] "without id" )
   * @returns {Promise<Algorithm[]>} Algorithm[] with id
   */
  async createAlgorithm(data: Algorithm[]): Promise<Algorithm[]> {
    const ret = await AlgorithmDB.create(data)
    return ret
  }

  /**
   * update a saved Statistical Algorithm in the database
   * @param {string} id ObjectId
   * @param {Algorithm} data Algorithm
   * @example updateAlgorithm("11bf9688-699f-49a4-9d8e-b0cc57301bff", Algorithm)
   * @returns {Promise<Algorithm | null>} Algorithm | null
   */
  async updateAlgorithm(id: string, data: Algorithm): Promise<Algorithm | null> {
    const ret = await AlgorithmDB.findByIdAndUpdate(id, data)
    return ret
  }

  /**
   * delete a saved Statistical Algorithm in the database
   * @param {string} id ObjectId
   * @example deleteAlgorithm('11bf9688-699f-49a4-9d8e-b0cc57301bff')
   * @returns {Promise<Algorithm | null>} Algorithm | null
   */
  async deleteAlgorithm(id: string): Promise<Algorithm | null> {
    const ret = await AlgorithmDB.findByIdAndDelete(id)
    return ret
  }
}
