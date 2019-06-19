module.exports.get = async event => ({
  statusCode: 200,
  body: JSON.stringify({ message: event }),
});
