const userTests = require("../models/User.js");

const getUsers = async (req, res) => {
  let users = await userTests.find({});

  res.status(200).json(users);
};

const postUsers = async (req, res) => {
  const { name,age,address,education } = req.body;
  const user = await userTests.create({ name,age,address,education });

  res.status(201).json({ message: "user has been created", user });
};

module.exports = {
    getUsers,
    postUsers
}