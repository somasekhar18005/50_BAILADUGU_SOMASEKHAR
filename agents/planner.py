class PlannerAgent:
    def plan(self, user_goal: str):
        print("[Planner] Planning tasks...")

        goal = user_goal.lower()

        if "onboard" in goal:
            tasks = [
                "Prepare onboarding checklist",
                "Create company email",
                "Schedule orientation session"
            ]
        elif "hackathon" in goal:
            tasks = [
                "Define problem statement",
                "Allocate team roles",
                "Prepare submission"
            ]
        else:
            tasks = [
                "Understand the requirement",
                "Break into steps",
                "Execute plan"
            ]

        return tasks
          