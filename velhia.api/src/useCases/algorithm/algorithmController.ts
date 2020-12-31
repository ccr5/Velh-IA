import { Request, Response } from 'express'
import { inject, injectable } from 'tsyringe'
import { IAlgorithmRepository, IAlgorithm } from '@interfaces/iAlgorithm'
import { TYPES } from '@config/container/types'

@injectable()
export class AlgorithmController {
  private repository: IAlgorithmRepository

  constructor(@inject(TYPES.AlgorithmRepository) algorithmRepository: IAlgorithmRepository) {
    this.repository = algorithmRepository
  }

  /**
   * Receive a get request and
   * return all Statistical Algorithm filter by a query in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example get()
   * @returns {Promise<Response | void>} IAlgorithm[] | 404 
   */
  async get(req: Request, res: Response): Promise<Response | void> {
    try {
      const offset = req.query.offset
      const limit = req.query.limit
      const fields = req.query.fields
      const sort = req.query.sort

      const sa: IAlgorithm[] | null = await this.repository.getAllAlgorithm()
      if (sa == null) {
        return res.sendStatus(404)
      }
      return res.send(sa)
    } catch (error) {
      res.sendStatus(400).send(error)
    }
  }

  /**
   * receive a post request with data to insert a 
   * new Statistical Algorithm in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example create(IAlgorithm[])
   * @returns {Promise<Response | void>} IAlgorithm[]
   */
  async create(req: Request, res: Response): Promise<Response | void> {
    try {
      const data: IAlgorithm[] = req.body
      const sas: IAlgorithm[] = await this.repository.createAlgorithm(data)
      return res.json(sas)
    } catch (error) {
      res.sendStatus(400).send(error)
    }
  }

  /**
   * receive a put request with a id to
   * update this Statistical Algorithm in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example update(IAlgorithm)
   * @returns {Promise<Response | void>} IAlgorithm | 404
   */
  async update(req: Request, res: Response): Promise<Response | void> {
    try {
      const saId: string = req.params.id
      const data: IAlgorithm = req.body
      const sa: IAlgorithm | null = await this.repository.updateAlgorithm(saId, data)
      if (sa == null) {
        return res.sendStatus(404)
      }
      return res.json(sa)
    } catch (error) {
      res.sendStatus(400).send(error)
    }
  }

  /**
   * receive a delete request with a id to
   * delete this Statistical Algorithm in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example delete(IAlgorithm)
   * @returns {Promise<Response | void>} IAlgorithm | 404
   */
  async delete(req: Request, res: Response): Promise<Response | void> {
    try {
      const saId: string = req.params.id
      const sa: IAlgorithm | null = await this.repository.deleteAlgorithm(saId)
      if (sa == null) {
        return res.sendStatus(404)
      }
      return res.send(sa)
    } catch (error) {
      res.sendStatus(400).send(error)
    }
  }
}
