import { Router } from 'express'

import { matchRoutes } from './v1/matchRoutes'
import { algorithmRoutes } from './v1/algorithmRoutes'
import { familyRoutes } from './v1/familyRoutes'
import { educationRoutes } from './v1/educationRoutes'
import { religionRoutes } from './v1/religionRoutes'

import { matchTestRoutes } from './v1/matchTestRoutes'
import { algorithmTestRoutes } from './v1/algorithmTestRoutes'
import { familyTestRoutes } from './v1/familyTestRoutes'
import { educationTestRoutes } from './v1/educationTestRoutes'
import { religionTestRoutes } from './v1/religionTestRoutes'

import { webRoutes } from './v1/webRoutes'

const routes = Router()

routes.use('/api/v1/matchs', matchRoutes)
routes.use('/api/v1/algorithms', algorithmRoutes)
routes.use('/api/v1/families', familyRoutes)
routes.use('/api/v1/educations', educationRoutes)
routes.use('/api/v1/religions', religionRoutes)
routes.use('/api/v1/web', webRoutes)

routes.use('/test/v1/matchs', matchTestRoutes)
routes.use('/test/v1/algorithms', algorithmTestRoutes)
routes.use('/test/v1/families', familyTestRoutes)
routes.use('/test/v1/educations', educationTestRoutes)
routes.use('/test/v1/religions', religionTestRoutes)

export { routes }
