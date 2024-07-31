## Project: 0x03. Queuing System in JS

### **Technology Stack**

- JavaScript (ES6)
- Node.js
- Express.js
- Redis
- Kue

### **Learning Objectives**

1. Running a Redis server on your machine.
2. Using Redis client for basic operations with Node.js.
3. Storing and retrieving hash values in Redis.
4. Handling asynchronous operations with Redis.
5. Using Kue as a queue system.
6. Building a basic Express app interacting with Redis and Kue.

### **Requirements**

- All code must be compatible with Ubuntu 18.04, Node 12.x, and Redis 5.0.7.
- Use the `.js` extension for JavaScript files.
- Include a `README.md` file at the root of the project directory.

---

### **Tasks**

#### **Task 0: Install a Redis Instance**

- **Objective:** Set up and start a Redis server.
- **Steps:**
  1. [Download Redis](https://redis.io/download) and extract Redis version 6.0.10.
  2. [Compile Redis](https://redis.io/topics/quickstart) and start the server.
  3. Test the server with `redis-cli` commands.
  4. Save the `dump.rdb` file for data persistence.

#### **Task 1: Node Redis Client**

- **Objective:** Connect to a Redis server using Node.js.
- **Implementation:**
  - Write a script `0-redis_client.js` using Babel and ES6.
  - Handle successful and failed connections with console messages.
- **Resources:**
  - [Node Redis Official Documentation](https://github.com/redis/node-redis)

#### **Task 2: Node Redis Client and Basic Operations**

- **Objective:** Perform basic Redis operations.
- **Implementation:**
  - Create `1-redis_op.js`.
  - Add `setNewSchool` and `displaySchoolValue` functions.
  - Use callbacks for async operations.
- **Resources:**
  - [Node Redis Guide](https://github.com/redis/node-redis/blob/master/docs/en/Examples.md)

#### **Task 3: Node Redis Client and Async Operations**

- **Objective:** Use async/await for Redis operations.
- **Implementation:**
  - Create `2-redis_op_async.js`.
  - Modify `displaySchoolValue` to use async/await with `promisify`.
- **Resources:**
  - [Node.js util.promisify() Documentation](https://nodejs.org/dist/latest-v10.x/docs/api/util.html#util_util_promisify_original)

#### **Task 4: Node Redis Client and Advanced Operations**

- **Objective:** Store and retrieve hash values.
- **Implementation:**
  - Create `4-redis_advanced_op.js`.
  - Use `hset` to store data and `hgetall` to retrieve it.
- **Resources:**
  - [Redis Hashes Documentation](https://redis.io/topics/data-types-intro#hashes)

#### **Task 5: Node Redis Client Publisher and Subscriber**

- **Objective:** Implement a basic publish/subscribe system.
- **Implementation:**
  - Create `5-subscriber.js` and `5-publisher.js`.
  - Subscribe to a channel and publish messages.
- **Resources:**
  - [Redis Pub/Sub Documentation](https://redis.io/topics/pubsub)

#### **Task 6: Create the Job Creator**

- **Objective:** Create jobs using Kue.
- **Implementation:**
  - Create `6-job_creator.js`.
  - Define job data and push jobs to the queue.
  - Log job creation, completion, and failure.
- **Resources:**
  - [Kue Documentation](https://github.com/Automattic/kue)

#### **Task 7: Create the Job Processor**

- **Objective:** Process jobs using Kue.
- **Implementation:**
  - Create `6-job_processor.js`.
  - Define `sendNotification` function.
  - Set up the queue to process jobs.
- **Resources:**
  - [Kue Processing Jobs](https://github.com/Automattic/kue#processing-jobs)

#### **Task 8: Track Progress and Errors with Kue: Create the Job Creator**

- **Objective:** Track job progress and handle errors.
- **Implementation:**
  - Create `7-job_creator.js`.
  - Define an array of jobs and push them to the queue.
  - Track and log job progress, completion, and errors.
- **Resources:**
  - [Kue Event Handling](https://github.com/Automattic/kue#queueevents)

#### **Task 9: Track Progress and Errors with Kue: Create the Job Processor**

- **Objective:** Process jobs with error handling.
- **Implementation:**
  - Create `7-job_processor.js`.
  - Handle blacklisted phone numbers and track job progress.
- **Resources:**
  - [Kue Error Handling](https://github.com/Automattic/kue#error-handling)

### **Final Notes**

- Ensure proper setup and functioning of Redis and Kue.
- Test all functionalities and handle edge cases.
- Prepare the code for manual QA review.
