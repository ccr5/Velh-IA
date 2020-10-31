import { Router } from 'express'
import { container } from 'tsyringe'
import { EducationController } from '@useCases/education/educationController'

const educationRoutes = Router()
const educationController = container.resolve(EducationController)

educationRoutes.get('/', (req, res) => educationController.getAll(req, res))
educationRoutes.get('/:id', (req, res) => educationController.getOne(req, res))
educationRoutes.get('/limit/:limit', (req, res) => educationController.getLast(req, res))
educationRoutes.post('/', (req, res) => educationController.create(req, res))
educationRoutes.put('/:id', (req, res) => educationController.update(req, res))
educationRoutes.delete('/:id', (req, res) => educationController.delete(req, res))

export { educationRoutes }
