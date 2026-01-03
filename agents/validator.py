class ValidatorAgent:
    def validate(self, results):
        print("[Validator] Validating results...")
        validated = []

        for result in results:
            validated.append(f"Validated: {result}")

        return validated
