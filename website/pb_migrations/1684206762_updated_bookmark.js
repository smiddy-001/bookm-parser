migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("ay9ai8xg51ystyw")

  collection.name = "user"

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "lvxqgkxl",
    "name": "bookmarks",
    "type": "json",
    "required": false,
    "unique": false,
    "options": {}
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("ay9ai8xg51ystyw")

  collection.name = "bookmark"

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "lvxqgkxl",
    "name": "title",
    "type": "json",
    "required": false,
    "unique": false,
    "options": {}
  }))

  return dao.saveCollection(collection)
})
