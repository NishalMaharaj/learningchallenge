# learningchallenge

Getting Started:
1. Run "docker-compose build" to initialise the container.
2. Run "docker-compose up" to start the service in the container.

Unit Tests:
1. Run pytest to execute the unit tests
2. Tests were created using TDD to test the smallest units of code in terms of functionality and error handling.

Comments:
1. I prefer to use meaningful names for classes, functions and variables instead of expansive comments. Always open for debate :).

Time Allocation:
1. Investigate and read up on Nameko - 2 Hours
2. Read up on TDD in python - 1 hour
3. Read up on error handling in python - 1 hour
4. Read up on Map-reduce in python - 30 minutes
5. Read up on Docker - 1 hour
6. Planning and design - 1 hour
7. Function 1 - 1 hour
8. Function 2 - 3  hours
9. Function 3 - 1 hour

Challenges experienced
1. Experienced issues transporting the huffman encoded bytes over the wire. I used base 64 encoding to overcome this. The function   that decodes a huffman encoded string expects a base 64 encoded input to overcome the same issue.

Frameworks:
1. I enjoyed using the Nameko framework. There's no boiler plate which makes it easy to concentrate on the logic. It makes setting up the microservices and distributed architecture simple. It also makes continuous integration and deployment easy. The different transport protocols(HTTP, RTC and event processing) makes it versatile. I will definately be using this framework going forward. The documentation is a bit high level however with google anything is possible.