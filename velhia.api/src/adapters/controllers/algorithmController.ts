import { Request, Response } from 'express'
import { inject, injectable } from 'tsyringe'
import TYPES from '@external/container/types'
import IAlgorithmUseCase from '@useCases/algorithm/iAlgorithmUseCase'
import IAlgorithm from '@entities/algorithm/iAlgorithm'

@injectable()
export class AlgorithmController {
  private useCase: IAlgorithmUseCase

  constructor(@inject(TYPES.AlgorithmUseCase) _usecase: IAlgorithmUseCase) {
    this.useCase = _usecase
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
      const offset: string | undefined = req.query.offset?.toString()
      const limit: string | undefined = req.query.limit?.toString()
      const filters: string | undefined = req.query.filters?.toString()
      const fields: string | undefined = req.query.fields?.toString()
      const sort: string | undefined = req.query.sort?.toString()

      const sa: IAlgorithm[] | null = await this.useCase.getAlgorithm(filters, fields, sort, offset, limit)
      if (sa == null) return res.sendStatus(404)
      return res.send(sa)
      
    } catch (error) {
      res.sendStatus(400).send(error)
      res.end(error)
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
      const sas: IAlgorithm[] = await this.useCase.createAlgorithm(data)
      return res.json(sas)
    } catch (error) {
      res.sendStatus(400).send(error)
      res.end(error)
    }
  }

  /**
   * receive a put request with a id to
   * update this Statistical Algorithm in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example update(Algorithm)
   * @returns {Promise<Response | void>} Algorithm | 404
   */
  async update(req: Request, res: Response): Promise<Response | void> {
    try {
      const saId: string = req.params.id
      const data: IAlgorithm = req.body
      const sa: IAlgorithm | null = await this.useCase.updateAlgorithm(saId, data)
      if (sa == null) {
        return res.sendStatus(404)
      }
      return res.json(sa)
    } catch (error) {
      res.sendStatus(400).send(error)
      res.end(error)
    }
  }

  /**
   * receive a delete request with a id to
   * delete this Statistical Algorithm in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example delete(Algorithm)
   * @returns {Promise<Response | void>} Algorithm | 404
   */
  async delete(req: Request, res: Response): Promise<Response | void> {
    try {
      const saId: string = req.params.id
      const sa: IAlgorithm | null = await this.useCase.deleteAlgorithm(saId)
      if (sa == null) {
        return res.sendStatus(404)
      }
      return res.send(sa)
    } catch (error) {
      res.sendStatus(400).send(error)
      res.end(error)
    }
  }
}
