import { Router } from 'express'
import { container } from 'tsyringe'
import { AlgorithmTestController } from '@useCases/algorithm/algorithmTestController'

const algorithmTestRoutes = Router()
const algorithmTestController = container.resolve(AlgorithmTestController)

algorithmTestRoutes.get('/', (req, res) => algorithmTestController.get(req, res))
algorithmTestRoutes.post('/', (req, res) => algorithmTestController.create(req, res))
algorithmTestRoutes.put('/:id', (req, res) => algorithmTestController.update(req, res))
algorithmTestRoutes.delete('/:id', (req, res) => algorithmTestController.delete(req, res))

export { algorithmTestRoutes }
