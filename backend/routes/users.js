const router = require('express').Router();
let User = require('../models/user.model');

router.route('/').get((req, res) => {
    // mongoose method to scan all users and return, find all users then
    //  return in json obtained from database and if error then the catch
    User.find()
    .then(users => res.json(users))
    .catch(err => res.status(400).json('Hmm, that is bad: ' + err));
});

router.route('/add').post((req, res) => {
    const username = req.body.username;

    const newUser = new User({username});

    // saved it to the db
    newUser.save()
    .then(() => res.json('User added!'))
    // if else it will return an error
    .catch(err => res.status(400).json('Hmm, that is bad: ' + err));
});

router.route('/:id').get((req, res) => {
  User.findById(req.params.id)
    .then(exercise => res.json(exercise))
    .catch(err => res.status(400).json('Error: ' + err));
});

router.route('/:id').delete((req, res) => {
  User.findByIdAndDelete(req.params.id)
    .then(() => res.json('User deleted.'))
    .catch(err => res.status(400).json('Error: ' + err));
});

router.route('/update/:id').post((req, res) => {
  Exercise.findById(req.params.id)
    .then(user => {
      user.username = req.body.username;

      user.save()
        .then(() => res.json('Exercise updated!'))
        .catch(err => res.status(400).json('Error: ' + err));
    })
    .catch(err => res.status(400).json('Error: ' + err));
});

// to export the router
module.exports = router;