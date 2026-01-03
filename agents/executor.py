class ExecutorAgent:
    def execute(self, tasks):
        print("[Executor] Executing tasks...")
        results = []

        for task in tasks:
            results.append(f"Executed: {task}")

        return results
