import { IAgentRepository, IAgent } from '@interfaces/iAgent'
import { Education } from '@entities/education'

export class EducationRepository implements IAgentRepository {
  /**
   * Get All Agents in the database
   * @example getAllAgent()
   * @returns {Promise<IAgent[] | null>} IAgent[] | null
   */
  async getAgent(
    filters:string | undefined, 
    fields: string | undefined, 
    sort: string | undefined, 
    offset: string | undefined, 
    limit: string| undefined): Promise<IAgent[] | null> {

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

      const ret = await Education.find(
        filters != undefined ? JSON.parse(filters) : {},
        fieldsString
      )
      .sort([sortList])
      .skip(offset != undefined ? +offset : +'')
      .limit(limit != undefined ? +limit : +'')

      return ret
  }

  /**
   * save a new Agent in the database
   * @param {IAgent[]} data IAgent[]
   * @example createAgent(IAgent[] "without id" )
   * @returns {Promise<IAgent[]>} IAgent[] with id
   */
  async createAgent(data: IAgent[]): Promise<IAgent[]> {
    const ret = await Education.create(data)
    return ret
  }

  /**
   * update a saved Agent in the database
   * @param {string} id ObjectId
   * @param {IAgent} data IAgent
   * @example updateAgent("11bf9688-699f-49a4-9d8e-b0cc57301bff", IAgent)
   * @returns {Promise<IAgent | null>} IAgent | null
   */
  async updateAgent(id: string, data: IAgent): Promise<IAgent | null> {
    const ret = await Education.findByIdAndUpdate(id, data)
    return ret
  }

  /**
   * delete a saved Agent in the database
   * @param {string} id ObjectId
   * @example deleteAgent('11bf9688-699f-49a4-9d8e-b0cc57301bff')
   * @returns {Promise<IAgent | null>} IAgent | null
   */
  async deleteAgent(id: string): Promise<IAgent | null> {
    const ret = await Education.findByIdAndDelete(id)
    return ret
  }
}
