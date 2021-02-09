import { Router } from 'express'
import { container } from 'tsyringe'
import { ReligionController } from '@adapters/controllers/religionController'

const religionRoutes = Router()
const religionController = container.resolve(ReligionController)

religionRoutes.get('/', (req, res) => religionController.get(req, res))
religionRoutes.post('/', (req, res) => religionController.create(req, res))
religionRoutes.put('/:id', (req, res) => religionController.update(req, res))
religionRoutes.delete('/:id', (req, res) => religionController.delete(req, res))

export { religionRoutes }
