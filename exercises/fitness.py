class Exercise:
    def __init__(self, name, reps, difficulty):
        self.name = name
        self.reps = reps
        self.difficulty = difficulty
    
    def get_info(self):
        return f"For {self.name} must be done {self.reps} at {self.difficulty} difficulty"
    
    def calories_burned(self):
        return self.reps * self.difficulty
    
class Cardio(Exercise):
    def calories_burned(self):
        return super().calories_burned() * 1.2

class Strength(Exercise):
    def calories_burned(self):
        return super().calories_burned() * 1.5
    
class Stretching(Exercise):
    def calories_burned(self):
        return super().calories_burned() * 0.8

  
# the workout
class Workout:
    def __init__(self, name):
        self.name = name
        self.exercises = []
    
    def add_exercise(self, exercise):
            self.exercises.append(exercise)
    
    def list_exercises(self):
        for i in self.exercises:
            print(i.get_info())
    
    def total_calories(self):
        total = 0
        for j in self.exercises:
            price = j.calories_burned()
            total += price
        return total
    
e1 = Cardio("Running", 10, 3)
e2 = Strength("Push-ups", 20, 4)
e3 = Stretching("Yoga", 15, 2)

workout = Workout("Morning Routine")
workout.add_exercise(e1)
workout.add_exercise(e2)
workout.add_exercise(e3)

workout.list_exercises()
print("Total calories burned:", workout.total_calories())    