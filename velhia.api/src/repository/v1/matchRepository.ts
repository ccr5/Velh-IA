import { IMatchRepository, IMatch } from '@interfaces/iMatch'
import { Match } from '@entities/matchs'

export class MatchRepository implements IMatchRepository {
  /**
   * Get All Matchs in the database
   * @example getAllMatch()
   * @returns {Promise<IMatch[] | null>} IMatch[] | null
   */
  async getMatch(
    filters:string | undefined, 
    fields: string | undefined, 
    sort: string | undefined, 
    offset: string | undefined, 
    limit: string| undefined): Promise<IMatch[] | null> {

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

      const ret = await Match.find(
        filters != undefined ? JSON.parse(filters) : {},
        fieldsString
      )
      .sort([sortList])
      .skip(offset != undefined ? +offset : +'')
      .limit(limit != undefined ? +limit : +'')

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
