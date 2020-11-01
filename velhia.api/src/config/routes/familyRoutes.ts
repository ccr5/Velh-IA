import { Router } from 'express'
import { container } from 'tsyringe'
import { FamilyController } from '@useCases/family/familyController'

const familyRoutes = Router()
const familyController = container.resolve(FamilyController)

familyRoutes.get('/', (req, res) => familyController.getAll(req, res))
familyRoutes.get('/:id', (req, res) => familyController.getOne(req, res))
familyRoutes.get('/limit/:limit', (req, res) => familyController.getLast(req, res))
familyRoutes.post('/', (req, res) => familyController.create(req, res))
familyRoutes.put('/:id', (req, res) => familyController.update(req, res))
familyRoutes.delete('/:id', (req, res) => familyController.delete(req, res))

export { familyRoutes }
