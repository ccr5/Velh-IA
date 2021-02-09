import { Router } from 'express'
import { container } from 'tsyringe'
import { EducationController } from '@adapters/controllers/educationController'

const educationRoutes = Router()
const educationController = container.resolve(EducationController)

educationRoutes.get('/', (req, res) => educationController.get(req, res))
educationRoutes.post('/', (req, res) => educationController.create(req, res))
educationRoutes.put('/:id', (req, res) => educationController.update(req, res))
educationRoutes.delete('/:id', (req, res) => educationController.delete(req, res))

export { educationRoutes }
