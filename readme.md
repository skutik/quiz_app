### Project description 
Game is my variation based on online quiz games like Kahoot.com or myQuiz.

---

#### API description

Description of API endpoints:
##### ping
 - Accepts only `GET` method
 - Implemented for API check, if everything works fine then should be returned status code `200` with 
 content JSON content `{"ping": "pong"}`
 
 ##### create_quiz
 - Accepts only `POST` method
 - Endpoint is used for storing newly created / updated quiz into database (with check of format). 
 - Status code `201` with JSON content `{"status": "ok", "data": {"quiz_id": quizId}}` is returned
 - When posted data payload have empty/wrong content then status code `400` with JSON content `{"status": "failed"}`
 
 #### status
 - Accepts only `GET` method
 - Provides info about running games.
 - Request require one parameter `gameId`. Without this parameter is returned status code `400` with JSON content 
 `{"status": "failed", "message"": "missing required param gameId}`