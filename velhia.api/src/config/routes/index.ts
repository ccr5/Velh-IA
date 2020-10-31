import { Router } from 'express'
import { matchRoutes } from './matchRoutes'

const routes = Router()

routes.use('/api/v1/matchs', matchRoutes)
routes.use('/api/v1/algorithms', matchRoutes)
routes.use('/api/v1/families', matchRoutes)
routes.use('/api/v1/educations', matchRoutes)
routes.use('/api/v1/religions', matchRoutes)

export { routes }
