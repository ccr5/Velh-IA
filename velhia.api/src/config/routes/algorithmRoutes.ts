import { Router } from 'express'
import { container } from 'tsyringe'
import { AlgorithmController } from '@useCases/algorithm/algorithmController'

const algorithmRoutes = Router()
const algorithmController = container.resolve(AlgorithmController)

algorithmRoutes.get('/', (req, res) => algorithmController.getAll(req, res))
algorithmRoutes.get('/:id', (req, res) => algorithmController.getOne(req, res))
algorithmRoutes.get('/limit/:limit', (req, res) => algorithmController.getLast(req, res))
algorithmRoutes.post('/', (req, res) => algorithmController.create(req, res))
algorithmRoutes.put('/:id', (req, res) => algorithmController.update(req, res))
algorithmRoutes.delete('/:id', (req, res) => algorithmController.delete(req, res))

export { algorithmRoutes }
