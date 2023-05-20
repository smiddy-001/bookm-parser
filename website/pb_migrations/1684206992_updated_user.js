migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("ay9ai8xg51ystyw")

  collection.name = "data"

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "va9xjnax",
    "name": "config",
    "type": "json",
    "required": false,
    "unique": false,
    "options": {}
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("ay9ai8xg51ystyw")

  collection.name = "user"

  // remove
  collection.schema.removeField("va9xjnax")

  return dao.saveCollection(collection)
})
