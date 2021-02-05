import { Router } from 'express'
import { container } from 'tsyringe'
import { MatchController } from 'src/adapters/controllers/matchController'

const matchRoutes = Router()
const matchController = container.resolve(MatchController)

matchRoutes.get('/', (req, res) => matchController.get(req, res))
matchRoutes.post('/', (req, res) => matchController.create(req, res))
matchRoutes.put('/:id', (req, res) => matchController.update(req, res))
matchRoutes.delete('/:id', (req, res) => matchController.delete(req, res))

export { matchRoutes }
