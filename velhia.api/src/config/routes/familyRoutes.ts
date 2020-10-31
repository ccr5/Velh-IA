import { Router } from 'express'
import { container } from 'tsyringe'

const familyRoutes = Router()

familyRoutes.post('/', (req, res) => { return res.json({ message: 'post' }) })
familyRoutes.get('/:id', (req, res) => { return res.json({ message: 'get' }) })
familyRoutes.put('/', (req, res) => { return res.json({ message: 'put' }) })
familyRoutes.delete('/:id', (req, res) => { return res.json({ message: 'delete' }) })

export { familyRoutes }
