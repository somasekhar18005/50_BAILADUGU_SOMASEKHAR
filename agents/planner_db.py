from backend.db import get_connection

class PlannerDBAgent:
    def create_tasks(self, workflow_id, tasks):
        conn = get_connection()
        cursor = conn.cursor()

        for task in tasks:
            cursor.execute("""
                INSERT INTO onboarding_tasks (workflow_id, task_name, status)
                VALUES (%s, %s, 'PENDING')
            """, (workflow_id, task))

        conn.commit()
        cursor.close()
        conn.close()
