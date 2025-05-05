from django.db import models

class User(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[("M", "Masculino"), ("F", "Feminino"), ("O", "Outro")])
    height_cm = models.PositiveIntegerField()
    weight_kg = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)  # Ex: Corrida, Musculação, Yoga
    duration_minutes = models.IntegerField()
    calories_burned = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

class AIRecommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recommendation_text = models.TextField()
    generated_at = models.DateTimeField(auto_now_add=True)

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=50)  # Ex: Café da manhã, Almoço
    food_items = models.TextField()  # Ex: "Banana, Aveia, Leite"
    calories = models.FloatField()
    carbs = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)


class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_type = models.CharField(max_length=50)  # Ex: Peso, Caminhada diária
    target_value = models.FloatField()
    current_value = models.FloatField()
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)


class HealthReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    period_start = models.DateField()
    period_end = models.DateField()
    average_calories_consumed = models.FloatField()
    average_calories_burned = models.FloatField()
    weight_change = models.FloatField()
    summary_text = models.TextField()
    generated_at = models.DateTimeField(auto_now_add=True)


class StepRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    steps = models.IntegerField()
    recorded_at = models.DateTimeField()


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    daily_step_goal = models.IntegerField(default=10000)
    preferred_units = models.CharField(max_length=10, default='metric')  # metric/imperial
    notifications_enabled = models.BooleanField(default=True)


class PredictionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prediction_type = models.CharField(max_length=50)  # Ex: perda de peso, risco de lesão
    input_data = models.JSONField()
    prediction_result = models.TextField()
    predicted_at = models.DateTimeField(auto_now_add=True)
