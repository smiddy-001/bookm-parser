migrate((db) => {
  const collection = new Collection({
    "id": "ay9ai8xg51ystyw",
    "created": "2023-05-16 03:09:06.551Z",
    "updated": "2023-05-16 03:09:06.551Z",
    "name": "bookmark",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "lvxqgkxl",
        "name": "title",
        "type": "json",
        "required": false,
        "unique": false,
        "options": {}
      }
    ],
    "indexes": [],
    "listRule": null,
    "viewRule": null,
    "createRule": null,
    "updateRule": null,
    "deleteRule": null,
    "options": {}
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("ay9ai8xg51ystyw");

  return dao.deleteCollection(collection);
})
