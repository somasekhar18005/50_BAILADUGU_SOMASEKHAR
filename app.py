# from agents.planner import PlannerAgent
# from agents.executor import ExecutorAgent
# from agents.validator import ValidatorAgent
# from agents.memory import AgentMemory


# def main():
#     print("=== Autonomous Multi-Agent Task Orchestrator ===\n")

#     user_goal = input("Enter your goal: ")

#     planner = PlannerAgent()
#     executor = ExecutorAgent()
#     validator = ValidatorAgent()
#     memory = AgentMemory()

#     memory.add(f"User goal: {user_goal}")

#     tasks = planner.plan(user_goal)
#     memory.add(f"Planned tasks: {tasks}")

#     results = executor.execute(tasks)
#     memory.add(f"Execution results: {results}")

#     final_output = validator.validate(results)
#     memory.add(f"Validation output: {final_output}")

#     print("\n--- FINAL OUTPUT ---")
#     for item in final_output:
#         print(item)

#     print("\n--- AGENT MEMORY ---")
#     for log in memory.show():
#         print(log)


# if __name__ == "__main__":
#     main()
from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.validator import ValidatorAgent
from agents.memory import AgentMemory


def main():
    print("=== Autonomous Multi-Agent Task Orchestrator ===\n")

    user_goal = input("Enter your goal: ")

    planner = PlannerAgent()
    executor = ExecutorAgent()
    validator = ValidatorAgent()
    memory = AgentMemory()

    # Store user goal
    memory.add(f"User goal: {user_goal}")

    # Planner phase
    tasks = planner.plan(user_goal)
    memory.add(f"Planned tasks: {tasks}")

    # Executor phase
    results = executor.execute(tasks)
    memory.add("Tasks executed")

    # Validator phase
    final_output = validator.validate(results)
    memory.add("Results validated")

    print("\n--- FINAL OUTPUT ---")
    for item in final_output:
        print(item)

    print("\n--- AGENT MEMORY LOG ---")
    for log in memory.show():
        print(log)


if __name__ == "__main__":
    main()
