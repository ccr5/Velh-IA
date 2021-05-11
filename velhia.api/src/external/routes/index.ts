import { Router } from 'express'
import { matchRoutes } from './matchRoutes'
import { algorithmRoutes } from './algorithmRoutes'

const routes = Router()

routes.use('/api/v1/matchs', matchRoutes)
routes.use('/api/v1/algorithms', algorithmRoutes)

export { routes }
