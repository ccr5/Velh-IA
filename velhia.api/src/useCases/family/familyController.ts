import { Request, Response } from 'express'
import { inject, injectable } from 'tsyringe'
import { TYPES } from '@config/container/types'
import { IAgentRepository, IAgent } from '@interfaces/iAgent'

@injectable()
export class FamilyController {
  private repository: IAgentRepository

  constructor(@inject(TYPES.FamilyRepository) familyRepository: IAgentRepository) {
    this.repository = familyRepository
  }

  /**
   * Receive a get request and
   * return all Agent filter by a query in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example get()
   * @returns {Promise<Response | void>} IAgent[] | 404 
   */
  async get(req: Request, res: Response): Promise<Response | void> {
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
