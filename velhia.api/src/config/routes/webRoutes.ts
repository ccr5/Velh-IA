import { Router } from 'express'
import { container } from 'tsyringe'
import { WebController } from '@useCases/web/webController'

const webRoutes = Router()
const webController = container.resolve(WebController)

webRoutes.get('/general', (req, res) => webController.getGeneralData(req, res))
webRoutes.get('/sa', (req, res) => webController.getSAData(req, res))
webRoutes.get('/mas', (req, res) => webController.getMASData(req, res))
webRoutes.get('/camp', (req, res) => webController.getCampData(req, res))

export { webRoutes }
