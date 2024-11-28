class HistoryManager:
    def __init__(self):
        self.history = []

    def add_to_history(self, action, result):
        self.history.append({"action": action, "result": result})

    def display_history(self):
        if not self.history:
            print("No history available.")
        else:
            for idx, entry in enumerate(self.history, 1):
                print(f"\nQuery #{idx}: {entry['action']}")
                print(f"Result: {entry['result']}\n")