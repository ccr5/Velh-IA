import { Router } from 'express'
import { container } from 'tsyringe'

const matchRoutes = Router()

matchRoutes.post('/', (req, res) => { return res.json({ message: 'post' }) })
matchRoutes.get('/:id', (req, res) => { return res.json({ message: 'get' }) })
matchRoutes.put('/', (req, res) => { return res.json({ message: 'put' }) })
matchRoutes.delete('/:id', (req, res) => { return res.json({ message: 'delete' }) })

export { matchRoutes }
