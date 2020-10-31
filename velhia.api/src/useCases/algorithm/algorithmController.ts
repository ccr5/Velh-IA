import { Request, Response } from 'express'
import { inject, injectable } from 'tsyringe'
import { v4 as uuidv4 } from 'uuid'
import { IAlgorithmRepository, IAlgorithm } from '@interfaces/iAlgorithm'
import { TYPES } from '@config/container/types'

@injectable()
export class AlgorithmController {
  private pictureRepository: IAlgorithmRepository

  constructor (@inject(TYPES.AlgorithmRepository) pictureRepository: IAlgorithmRepository) {
    this.pictureRepository = pictureRepository
  }

  /**
   * Receive a request with files to save in the database
   * @param {Request} req request with byte array files
   * @param {Response} res response
   * @returns {Promise<void>} Promise
   */
  async getAll (req: Request, res: Response): Promise<Response | void> {
    try {
      const archive: IAlgorithm[] | null = await this.pictureRepository.getAllAlgorithm()
      if (archive == null) {
        return res.sendStatus(404)
      }
      return res.send(archive)
    } catch (error) {
      res.sendStatus(400).send(error)
    }
  }

  /**
   * Receive an request with an id to get the picture on the database.
   * @param {Request} req request with an id
   * @param {Response} res response
   * @returns {Promise<Response | void>} Promise
   */
  async getOne (req: Request, res: Response): Promise<Response | void> {
    try {
      const archiveId: string = req.params.id
      const archive: IAlgorithm | null = await this.pictureRepository.getOneAlgorithm(archiveId)
      if (archive == null) {
        return res.sendStatus(404)
      }
      return res.send(archive)
    } catch (error) {
      res.sendStatus(400).send(error)
    }
  }

  async create (req: Request, res: Response): Promise<Response | void> {
    try {
      const archives: IAlgorithm[] = await this.pictureRepository.createAlgorithm(req.body)
      return res.send(archives)
    } catch (error) {
      res.sendStatus(400).send(error)
    }
  }
}
