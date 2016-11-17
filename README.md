# Whale_Watcher
A rudimentary Python tool used to manage the execution of software within Docker containers on a single machine. This is done in an encapsulated manner, allowing multiple containers to be run simultaneously and independently. See ARCHITECTURE.md for my thoughts on tradeoffs when implementing this tool under a 3 hour time constraint.

## Requirements:

1. Accept a bash command.
1. Launch a Docker container to run the command.
1. Collect logs real-time (STDOUT/STDERR) while the command runs.
1. The logs should be saved and identifiable in a logs directory.
1. Clean up when the command finishes and handle expected failures.
1. Have the ability to stop a specified container (without losing any logs).

## **_Usage_**

* Make the file executable

```bash
chmod +x <script_name>
```

* Run some command inside a container

```bash
./script_name -r 'my command'
  ```

* To have more control over bash and run longer commands

```bash
./script_name -b 'my super long command with -options'
```

* To stop a specified container

```bash
./script_name stop 'container_name_or_id'
```

* To kill a container

```bash
./script_name kill 'container_name_or_id'
```
