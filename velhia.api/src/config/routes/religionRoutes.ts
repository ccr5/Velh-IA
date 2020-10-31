import { Router } from 'express'
import { container } from 'tsyringe'
import { ReligionController } from '@useCases/religion/religionController'

const religionRoutes = Router()
const religionController = container.resolve(ReligionController)

religionRoutes.get('/', (req, res) => religionController.getAll(req, res))
religionRoutes.get('/:id', (req, res) => religionController.getOne(req, res))
religionRoutes.get('/limit/:limit', (req, res) => religionController.getLast(req, res))
religionRoutes.post('/', (req, res) => religionController.create(req, res))
religionRoutes.put('/:id', (req, res) => religionController.update(req, res))
religionRoutes.delete('/:id', (req, res) => religionController.delete(req, res))

export { religionRoutes }
