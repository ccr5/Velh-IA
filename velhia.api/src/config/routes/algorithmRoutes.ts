import { Router } from 'express'
import { container } from 'tsyringe'
import { AlgorithmController } from '@useCases/algorithm/algorithmController'

const algorithmRoutes = Router()
const algorithmController = container.resolve(AlgorithmController)

algorithmRoutes.post('/', (req, res) => algorithmController.create(req, res))
algorithmRoutes.get('/', (req, res) => algorithmController.getAll(req, res))
algorithmRoutes.get('/:id', (req, res) => algorithmController.getOne(req, res))
algorithmRoutes.put('/', (req, res) => { return res.json({ message: 'put' }) })
algorithmRoutes.delete('/:id', (req, res) => { return res.json({ message: 'delete' }) })

export { algorithmRoutes }
