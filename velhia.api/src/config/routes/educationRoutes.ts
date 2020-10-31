import { Router } from 'express'
import { container } from 'tsyringe'

const educationRoutes = Router()

educationRoutes.post('/', (req, res) => { return res.json({ message: 'post' }) })
educationRoutes.get('/:id', (req, res) => { return res.json({ message: 'get' }) })
educationRoutes.put('/', (req, res) => { return res.json({ message: 'put' }) })
educationRoutes.delete('/:id', (req, res) => { return res.json({ message: 'delete' }) })

export { educationRoutes }
