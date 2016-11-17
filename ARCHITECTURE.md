# Docker_Mgr Architecture and Tradeoffs
When building a tool such as this, there are many ways of getting the same results. While not an ideal tool to use, given the time constraints, I aimed for something very basic that meets the desired requirements. Given more time, I'd implement more software and in better ways. I summarize my decisions and tradeoffs below.

## Design Goals
The overall goal for this project was to build a foundation for a distributed job framework within 3 hours. Prior to starting the implementation, I intended to make my tool as secure and as clean as possible. The overall design would use an OOP structure and I preferred passing commands on the command line rather than using something like raw_input().

## Tradeoffs and Failures
The first requirement is to accept a bash command. This can be done in many ways. My first choice was to use Python's argparse module. This module is very user-friendly and easy to use. I went in another direction, using sys.argv instead due to time constraints.

The second sacrifice I had to face was how to pass the specified command to Docker containers. I considered the creation of Dockerfiles but ended up passing commands directly to bash to save time.

The third requirement (collecting logs) was where I encountered many options to achieve my goal. While not my preferred method and definitely not secure, I decided to create a centralized logs directory. Every container will be directed to output logs to this location. Each log will be given a unique name to make the logs easily identifiable. This method is not without flaws and should never be used in production. This method makes it difficult to move these containers and log injection attacks are still a concern.

When stopping a container, I found a couple of effective methods and implemented both. The first is simply to run the equivalent of the 'docker stop CONTAINER' command. This method sends a SIGTERM signal to the main process running inside a container. The process is given a window of time to stop or else the signal is escalated to SIGKILL. I chose to implement a second 'kill' option with this tool to allow the user to kill non-responsive containers immediately.

The final requirement was to clean up after each command finishes. After containers are ran and exited, they just sit on the hard drive. The clean up method I implemented runs automatically after running this tool. It removes containers with an 'exited' status and deletes unwanted container images as well. All logs are retained after the cleanup method runs.

## Considerations for Future Development
If given more time, I think a good implementation would be to use complimentary software such as the ELK stack. I would like to implement Elasticsearch, Logstash and Kibana. Logstash would help manage logs, Elasticsearch would make searching easier and Kibana helps provide visualizations for the data from the logs.
