import { Router } from 'express'
import { container } from 'tsyringe'

const algorithmRoutes = Router()

algorithmRoutes.post('/', (req, res) => { return res.json({ message: 'post' }) })
algorithmRoutes.get('/:id', (req, res) => { return res.json({ message: 'get' }) })
algorithmRoutes.put('/', (req, res) => { return res.json({ message: 'put' }) })
algorithmRoutes.delete('/:id', (req, res) => { return res.json({ message: 'delete' }) })

export { algorithmRoutes }
