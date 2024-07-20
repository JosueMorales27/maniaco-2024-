class LifePurposeAchiever:
    def __init__(self):
        self.goals = []
        self.finances = {
            'income': [],
            'expenses': [],
            'savings': 0,
            'debt': 0
        }

    def add_goal(self, title, description, category, deadline):
        self.goals.append({'title': title, 'description': description, 'category': category, 'deadline': deadline, 'completed': False})

    def mark_goal_completed(self, title):
        for goal in self.goals:
            if goal['title'] == title:
                goal['completed'] = True
                return f"Goal '{title}' completed!"
        return "Goal not found."

    def add_financial_record(self, type, amount, description):
        if type in self.finances:
            self.finances[type].append({'amount': amount, 'description': description})
        else:
            print("Invalid financial type")

    def calculate_net_income(self):
        total_income = sum(item['amount'] for item in self.finances['income'])
        total_expenses = sum(item['amount'] for item in self.finances['expenses'])
        return total_income - total_expenses

# Example usage:
app = LifePurposeAchiever()
app.add_goal("Graduate from college", "Complete my degree by 2025", "Education", "2025-06-15")
app.add_financial_record('income', 1250, 'Bi-weekly salary')
app.add_financial_record('expenses', 1000, 'Monthly household expenses')
print(app.mark_goal_completed("Graduate from college"))
print("Net Income:", app.calculate_net_income())
