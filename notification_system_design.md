# Notification System Design

## Stage 1: API Design

GET /notifications  
POST /notifications  
PATCH /notifications/{id}/read  

---

## Stage 2: Database Design

Tables:
- users
- notifications

notifications:
- id
- user_id
- type
- message
- is_read
- created_at

---

## Stage 3: Query Optimization

Problem: Slow query due to full table scan

Solution:
CREATE INDEX idx_user_read_created
ON notifications(studentID, isRead, createdAt DESC);

---

## Stage 4: Performance

- Use caching (Redis)
- Pagination
- Lazy loading

---

## Stage 5: Reliability

Problems:
- Sequential processing is slow
- If email fails, process stops midway
- No retry mechanism
- DB and email are tightly coupled

Solution:
- Use message queue (Kafka/RabbitMQ)
- Retry failed jobs
- Decouple email & DB operations

Improved Pseudocode:

function notify_all(student_ids, message):
    for student_id in student_ids:
        save_to_db(student_id, message)

    push_to_queue(student_ids, message)

worker():
    while true:
        job = get_from_queue()
        try:
            send_email(job.student_id, job.message)
            push_to_app(job.student_id, job.message)
        except:
            retry(job)

## Stage 6: Priority Inbox

Sort by:
- Type priority (Placement > Result > Event)
- Timestamp (latest first)
