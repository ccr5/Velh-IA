import { Router } from 'express'
import { container } from 'tsyringe'
import { AlgorithmController } from 'src/adapters/controllers/algorithmController'

const algorithmRoutes = Router()
const algorithmController = container.resolve(AlgorithmController)

algorithmRoutes.get('/', (req, res) => algorithmController.get(req, res))
algorithmRoutes.post('/', (req, res) => algorithmController.create(req, res))
algorithmRoutes.put('/:id', (req, res) => algorithmController.update(req, res))
algorithmRoutes.delete('/:id', (req, res) => algorithmController.delete(req, res))

export { algorithmRoutes }
