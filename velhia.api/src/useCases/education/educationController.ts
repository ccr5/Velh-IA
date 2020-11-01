import { Request, Response } from 'express'
import { inject, injectable } from 'tsyringe'
import { TYPES } from '@config/container/types'
import { IAgentRepository, IAgent } from '@interfaces/iAgent'

@injectable()
export class EducationController {
  private repository: IAgentRepository

  constructor(@inject(TYPES.EducationRepository) educationRepository: IAgentRepository) {
    this.repository = educationRepository
  }

  /**
   * Receive a get request and
   * return all Agent saved in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example getAll()
   * @returns {Promise<Response | void>} IAgent[] | 404 
   */
  async getAll(req: Request, res: Response): Promise<Response | void> {
    try {
      const mas: IAgent[] | null = await this.repository.getAllAgent()
      if (mas == null) {
        return res.sendStatus(404)
      }
      return res.send(mas)
    } catch (error) {
      res.sendStatus(400).send(error)
    }
  }

  /**
   * Receive a get request with id and
   * return this Agent saved in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example getOne('5f9db3a3fc7c860a3e316712')
   * @returns {Promise<Response | void>} IAgent | 404
   */
  async getOne(req: Request, res: Response): Promise<Response | void> {
    try {
      const masId: string = req.params.id
      const mas: IAgent | null = await this.repository.getOneAgent(masId)
      if (mas == null) {
        return res.sendStatus(404)
      }
      return res.send(mas)
    } catch (error) {
      res.sendStatus(400).send(error)
    }
  }

  /**
   * receive a get request with limit X to get the  
   * X latest Agent created in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example getLast(2)
   * @returns {Promise<Response | void>} IAgent[2] | 404
   */
  async getLast(req: Request, res: Response): Promise<Response | void> {
    try {
      const limit: number = +req.params.limit
      const mas: IAgent[] | null = await this.repository.getLastAgent(limit)
      if (mas == null) {
        return res.sendStatus(404)
      }
      return res.send(mas)
    } catch (error) {
      res.sendStatus(400).send(error)
    }
  }

  /**
   * receive a post request with data to insert a 
   * new Agent in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example create(IAgent[])
   * @returns {Promise<Response | void>} IAgent[]
   */
  async create(req: Request, res: Response): Promise<Response | void> {
    try {
      const data: IAgent[] = req.body
      const mas: IAgent[] = await this.repository.createAgent(data)
      return res.json(mas)
    } catch (error) {
      res.sendStatus(400).send(error)
    }
  }

  /**
   * receive a put request with a id to
   * update this Agent in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example update(IAgent)
   * @returns {Promise<Response | void>} IAgent | 404
   */
  async update(req: Request, res: Response): Promise<Response | void> {
    try {
      const masId: string = req.params.id
      const data: IAgent = req.body
      const mas: IAgent | null = await this.repository.updateAgent(masId, data)
      if (mas == null) {
        return res.sendStatus(404)
      }
      return res.json(mas)
    } catch (error) {
      res.sendStatus(400).send(error)
    }
  }

  /**
   * receive a delete request with a id to
   * delete this Agent in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example delete(IAgent)
   * @returns {Promise<Response | void>} IAgent | 404
   */
  async delete(req: Request, res: Response): Promise<Response | void> {
    try {
      const masId: string = req.params.id
      const mas: IAgent | null = await this.repository.deleteAgent(masId)
      if (mas == null) {
        return res.sendStatus(404)
      }
      return res.send(mas)
    } catch (error) {
      res.sendStatus(400).send(error)
    }
  }
}
