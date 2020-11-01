import { Router } from 'express'
import { container } from 'tsyringe'
import { MatchController } from '@useCases/match/matchController'

const matchRoutes = Router()
const matchController = container.resolve(MatchController)

matchRoutes.get('/', (req, res) => matchController.getAll(req, res))
matchRoutes.get('/:id', (req, res) => matchController.getOne(req, res))
matchRoutes.get('/limit/:limit', (req, res) => matchController.getLast(req, res))
matchRoutes.post('/', (req, res) => matchController.create(req, res))
matchRoutes.put('/:id', (req, res) => matchController.update(req, res))
matchRoutes.delete('/:id', (req, res) => matchController.delete(req, res))

export { matchRoutes }
