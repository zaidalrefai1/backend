

class DifficultyModel:
    def __init__(self):
        self.streak = 0
    def record(self, correct):
        self.streak = self.streak + 1 if correct else max(0, self.streak - 1)
    def extra(self):
        return self.streak

class Game:
    def __init__(self):
        self.scene = "hub"
        self.level = 1
        self.model = DifficultyModel()
        self.time_left = 90

    def get_state(self):
        return {
            "scene": self.scene,
            "level": self.level,
            "timeLeft": self.time_left,
            "background": f"/assets/{self.scene}.png",
            "extraChallenge": self.model.extra()
        }

    def handle_action(self, action):
        if self.scene == "hub" and action == "enter_forest":
            self.scene = "dna_forest"
        elif self.scene == "dna_forest" and action == "enter_lab":
            self.scene = "dna_lab"
        elif action == "exit_to_hub":
            self.scene = "hub"
        elif action == "complete_level":
            self.level += 1
            if self.level > 3:
                self.scene = "win"
        elif action == "record_correct":
            self.model.record(True)
        elif action == "record_wrong":
            self.model.record(False)