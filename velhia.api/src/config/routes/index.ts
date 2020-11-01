import { Router } from 'express'
import { matchRoutes } from './matchRoutes'
import { algorithmRoutes } from './algorithmRoutes'
import { familyRoutes } from './familyRoutes'
import { educationRoutes } from './educationRoutes'
import { religionRoutes } from './religionRoutes'

const routes = Router()

routes.use('/api/v1/matchs', matchRoutes)
routes.use('/api/v1/algorithms', algorithmRoutes)
routes.use('/api/v1/families', familyRoutes)
routes.use('/api/v1/educations', educationRoutes)
routes.use('/api/v1/religions', religionRoutes)

export { routes }
