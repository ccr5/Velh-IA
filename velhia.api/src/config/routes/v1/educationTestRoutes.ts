import { Router } from 'express'
import { container } from 'tsyringe'
import { EducationTestController } from '@useCases/education/educationTestController'

const educationTestRoutes = Router()
const educationTestController = container.resolve(EducationTestController)

educationTestRoutes.get('/', (req, res) => educationTestController.get(req, res))
educationTestRoutes.post('/', (req, res) => educationTestController.create(req, res))
educationTestRoutes.put('/:id', (req, res) => educationTestController.update(req, res))
educationTestRoutes.delete('/:id', (req, res) => educationTestController.delete(req, res))

export { educationTestRoutes }
