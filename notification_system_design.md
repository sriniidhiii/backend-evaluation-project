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

Problem: Notify all is slow

Solution:
- Use message queue
- Async processing

---

## Stage 6: Priority Inbox

Sort by:
- Type priority (Placement > Result > Event)
- Timestamp (latest first)
