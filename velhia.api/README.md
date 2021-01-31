# Velh-IA API

Where all data is managed

### Sumary
1. [Description](https://github.com/ccr5/Velh-IA/tree/master/velhia.api#description "Description")
2. [Structure](https://github.com/ccr5/Velh-IA/tree/master/velhia.api#structure "Structure")
3. [Language and tools](https://github.com/ccr5/Velh-IA/tree/master/velhia.api#langauge-and-tools "Language and tools")
4. [Requirements](https://github.com/ccr5/Velh-IA/tree/master/velhia.api#requirements "Requirements")
5. [Usage](https://github.com/ccr5/Velh-IA/tree/master/velhia.api#usage "Usage")

------------
### Description
This is a microservice to provide a RESTFul API to save and get data to show or make analysis.

### Structure
* tests: all project's test
* src: project's root directory
* config: all project configuration (Ex: Database Connection, Routes)
* domain: all entity, model, etc to organize and use (Ex: Interfaces, Enum, Entities)
* repository: all mongodb methods
* useCases/**entityFolder**: all logic entity files
* utils: others files

### Language and Tools
1. Typescript
2. NodeJS
3. Express
4. Dotenv
5. Tsyringe
6. Mongoose
7. Jest

### Requirements
1. Mongo
2. Yarn
3. NodeJS

### Usage
1. run cd velhia.api
2. run yarn
3. Change environment variables
3. run yarn serve 
