import { Router } from 'express'
import { container } from 'tsyringe'

const religionRoutes = Router()

religionRoutes.post('/', (req, res) => { return res.json({ message: 'post' }) })
religionRoutes.get('/:id', (req, res) => { return res.json({ message: 'get' }) })
religionRoutes.put('/', (req, res) => { return res.json({ message: 'put' }) })
religionRoutes.delete('/:id', (req, res) => { return res.json({ message: 'delete' }) })

export { religionRoutes }
