const axios = require("axios");

const LOG_API = "http://20.207.122.201/evaluation-service/logs";

async function Log(stack, level, pkg, message, token) {
  try {
    const response = await axios.post(
      LOG_API,
      {
        stack: stack.toLowerCase(),
        level: level.toLowerCase(),
        package: pkg.toLowerCase(),
        message: message
      },
      {
        headers: {
          Authorization: `Bearer ${token}`
        }
      }
    );

    console.log("Log sent:", response.data);
  } catch (error) {
    console.error("Log failed:", error.message);
  }
}

module.exports = Log;