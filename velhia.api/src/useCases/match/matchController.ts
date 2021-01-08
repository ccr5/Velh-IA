import { Request, Response } from 'express'
import { inject, injectable } from 'tsyringe'
import { TYPES } from '@config/container/types'
import { IMatchRepository, IMatch } from '@interfaces/iMatch'

@injectable()
export class MatchController {
  private repository: IMatchRepository

  constructor(@inject(TYPES.MatchRepository) matchRepository: IMatchRepository) {
    this.repository = matchRepository
  }

  /**
   * Receive a get request and
   * return all Match filter by a query in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example get()
   * @returns {Promise<Response | void>} IMatch[] | 404 
   */
  async get(req: Request, res: Response): Promise<Response | void> {
    try {
      const offset: string | undefined = req.query.offset?.toString()
      const limit: string | undefined = req.query.limit?.toString()
      const filters: string | undefined = req.query.filters?.toString()
      const fields: string | undefined = req.query.fields?.toString()
      const sort: string | undefined = req.query.sort?.toString()

      const mac: IMatch[] | null = await this.repository.getMatch(filters, fields, sort, offset, limit)
      if (mac == null) {
        return res.sendStatus(404)
      }
      return res.send(mac)
    } catch (error) {
      res.sendStatus(400).send(error)
    }
  }

  /**
   * receive a post request with data to insert a 
   * new Match in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example create(IMatch[])
   * @returns {Promise<Response | void>} IMatch[]
   */
  async create(req: Request, res: Response): Promise<Response | void> {
    try {
      const data: IMatch[] = req.body
      const mac: IMatch[] = await this.repository.createMatch(data)
      return res.json(mac)
    } catch (error) {
      res.sendStatus(400).send(error)
    }
  }

  /**
   * receive a put request with a id to
   * update this Match in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example update(IMatch)
   * @returns {Promise<Response | void>} IMatch | 404
   */
  async update(req: Request, res: Response): Promise<Response | void> {
    try {
      const macId: string = req.params.id
      const data: IMatch = req.body
      const mac: IMatch | null = await this.repository.updateMatch(macId, data)
      if (mac == null) {
        return res.sendStatus(404)
      }
      return res.json(mac)
    } catch (error) {
      res.sendStatus(400).send(error)
    }
  }

  /**
   * receive a delete request with a id to
   * delete this Match in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example delete(IMatch)
   * @returns {Promise<Response | void>} IMatch | 404
   */
  async delete(req: Request, res: Response): Promise<Response | void> {
    try {
      const macId: string = req.params.id
      const mac: IMatch | null = await this.repository.deleteMatch(macId)
      if (mac == null) {
        return res.sendStatus(404)
      }
      return res.send(mac)
    } catch (error) {
      res.sendStatus(400).send(error)
    }
  }
}
