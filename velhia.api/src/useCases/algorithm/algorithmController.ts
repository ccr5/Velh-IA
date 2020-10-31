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
   * Receive a get request without id and
   * return all Statistical Algorithm saved in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example getAll()
   * @returns {Promise<Response | void>} IAlgorithm[]
   */
  async getAll(req: Request, res: Response): Promise<Response | void> {
    try {
      const archive: IAlgorithm[] | null = await this.repository.getAllAlgorithm()
      if (archive == null) {
        return res.sendStatus(404)
      }
      return res.send(archive)
    } catch (error) {
      res.sendStatus(400).send(error)
    }
  }

  /**
   * Receive a get request with id and
   * return a Statistical Algorithm saved in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example getOne('5f9db3a3fc7c860a3e316712')
   * @returns {Promise<Response | void>} IAlgorithm
   */
  async getOne(req: Request, res: Response): Promise<Response | void> {
    try {
      const archiveId: string = req.params.id
      const archive: IAlgorithm | null = await this.repository.getOneAlgorithm(archiveId)
      if (archive == null) {
        return res.sendStatus(404)
      }
      return res.send(archive)
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
   * @returns {Promise<Response | void>} IAlgorithm[] with id
   */
  async create(req: Request, res: Response): Promise<Response | void> {
    try {
      const archives: IAlgorithm[] = req.body
      const ret: IAlgorithm[] = await this.repository.createAlgorithm(archives)
      return res.json(ret)
    } catch (error) {
      res.sendStatus(400).send(error)
    }
  }

  /**
   * receive a put request with a id to
   * update a Statistical Algorithm in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example delete(IAlgorithm[])
   * @returns {Promise<Response | void>} IAlgorithm
   */
  async update(req: Request, res: Response): Promise<Response | void> {
    try {
      const algorithmId: string = req.params.id
      const algorithm: IAlgorithm = req.body
      const ret: IAlgorithm | null = await this.repository.updateAlgorithm(algorithmId, algorithm)
      if (ret == null) {
        return res.sendStatus(404)
      }
      return res.json(ret)
    } catch (error) {
      res.sendStatus(400).send(error)
    }
  }

  /**
   * receive a delete request with a id to
   * delete a Statistical Algorithm in the db
   * @param {Request} req request
   * @param {Response} res response
   * @example delete(IAlgorithm[])
   * @returns {Promise<Response | void>} IAlgorithm[] with id
   */
  async delete(req: Request, res: Response): Promise<Response | void> {
    try {
      const archiveId: string = req.params.id
      const archive: IAlgorithm | null = await this.repository.deleteAlgorithm(archiveId)
      if (archive == null) {
        return res.sendStatus(404)
      }
      return res.send(archive)
    } catch (error) {
      res.sendStatus(400).send(error)
    }
  }
}
