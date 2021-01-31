import { Router } from 'express'
import { container } from 'tsyringe'
import { FamilyTestController } from '@useCases/family/familyTestController'

const familyTestRoutes = Router()
const familyTestController = container.resolve(FamilyTestController)

familyTestRoutes.get('/', (req, res) => familyTestController.get(req, res))
familyTestRoutes.post('/', (req, res) => familyTestController.create(req, res))
familyTestRoutes.put('/:id', (req, res) => familyTestController.update(req, res))
familyTestRoutes.delete('/:id', (req, res) => familyTestController.delete(req, res))

export { familyTestRoutes }
