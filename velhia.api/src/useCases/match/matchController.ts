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
   * return all Match saved in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example getAll()
   * @returns {Promise<Response | void>} IMatch[] | 404 
   */
  async getAll(req: Request, res: Response): Promise<Response | void> {
    try {
      const mac: IMatch[] | null = await this.repository.getAllMatch()
      if (mac == null) {
        return res.sendStatus(404)
      }
      return res.send(mac)
    } catch (error) {
      res.sendStatus(400).send(error)
    }
  }

  /**
   * Receive a get request with id and
   * return this Match saved in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example getOne('5f9db3a3fc7c860a3e316712')
   * @returns {Promise<Response | void>} IMatch | 404
   */
  async getOne(req: Request, res: Response): Promise<Response | void> {
    try {
      const macId: string = req.params.id
      const mac: IMatch | null = await this.repository.getOneMatch(macId)
      if (mac == null) {
        return res.sendStatus(404)
      }
      return res.send(mac)
    } catch (error) {
      res.sendStatus(400).send(error)
    }
  }

  /**
   * receive a get request with limit X to get the  
   * X latest Match created in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example getLast(2)
   * @returns {Promise<Response | void>} IMatch[2] | 404
   */
  async getLast(req: Request, res: Response): Promise<Response | void> {
    try {
      const limit: number = +req.params.limit
      const mac: IMatch[] | null = await this.repository.getLastMatch(limit)
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
