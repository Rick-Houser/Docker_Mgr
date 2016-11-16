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
