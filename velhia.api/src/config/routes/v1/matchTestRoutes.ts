import { Router } from 'express'
import { container } from 'tsyringe'
import { MatchTestController } from '@useCases/match/matchTestController'

const matchTestRoutes = Router()
const matchTestController = container.resolve(MatchTestController)

matchTestRoutes.get('/', (req, res) => matchTestController.get(req, res))
matchTestRoutes.post('/', (req, res) => matchTestController.create(req, res))
matchTestRoutes.put('/:id', (req, res) => matchTestController.update(req, res))
matchTestRoutes.delete('/:id', (req, res) => matchTestController.delete(req, res))

export { matchTestRoutes }
