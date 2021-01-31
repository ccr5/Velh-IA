import { Router } from 'express'
import { container } from 'tsyringe'
import { ReligionTestController } from '@useCases/religion/religionTestController'

const religionTestRoutes = Router()
const religionTestController = container.resolve(ReligionTestController)

religionTestRoutes.get('/', (req, res) => religionTestController.get(req, res))
religionTestRoutes.post('/', (req, res) => religionTestController.create(req, res))
religionTestRoutes.put('/:id', (req, res) => religionTestController.update(req, res))
religionTestRoutes.delete('/:id', (req, res) => religionTestController.delete(req, res))

export { religionTestRoutes }
