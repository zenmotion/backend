from django.urls import path



from .views import (
    user_view, user_preferences_view, ai_recomendation_view, 
    goal_view, health_report_view, meal_view, notification_view, 
    prediction_history_view, step_record_view, workout_view
)
from .views.user_view import LoginView


urlpatterns = [

    # --- User ---
    path('user', user_view.UserListCreateView.as_view()),
    path('user/id/<int:pk>', user_view.UserDetailView.as_view()),
    path('user/search/', user_view.UserSearchView.as_view()),

    # --- User Preferences ---
    path('user_preferences', user_preferences_view.UserPreferencesListCreateView.as_view()),
    path('user_preferences/id/<int:pk>', user_preferences_view.UserPreferencesDetailView.as_view()),
    path('user_preferences/search/', user_preferences_view.UserPreferencesSearchView.as_view()),

    # --- AI Recommendation ---
    path('ai_recommendation', ai_recomendation_view.AIRecommendationListCreateView.as_view()),
    path('ai_recommendation/id/<int:pk>', ai_recomendation_view.AIRecommendationDetailView.as_view()),
    path('ai_recommendation/search/', ai_recomendation_view.AIRecommendationSearchView.as_view()),

    # --- Goal ---
    path('goal', goal_view.GoalListCreateView.as_view()),
    path('goal/id/<int:pk>', goal_view.GoalDetailView.as_view()),
    path('goal/search/', goal_view.GoalSearchView.as_view()),

    # --- Health Report ---
    path('health_report', health_report_view.HealthReportListCreateView.as_view()),
    path('health_report/id/<int:pk>', health_report_view.HealthReportDetailView.as_view()),
    path('health_report/search/', health_report_view.HealthReportSearchView.as_view()),

    # --- Meal ---
    path('meal', meal_view.MealListCreateView.as_view()),
    path('meal/id/<int:pk>', meal_view.MealDetailView.as_view()),
    path('meal/search/', meal_view.MealSearchView.as_view()),

    # --- Notification ---
    path('notification', notification_view.NotificationListCreateView.as_view()),
    path('notification/id/<int:pk>', notification_view.NotificationDetailView.as_view()),
    path('notification/search/', notification_view.NotificationSearchView.as_view()),

    # --- Prediction History ---
    path('prediction_history', prediction_history_view.PredictionHistoryListCreateView.as_view()),
    path('prediction_history/id/<int:pk>', prediction_history_view.PredictionHistoryDetailView.as_view()),
    path('prediction_history/search/', prediction_history_view.PredictionHistorySearchView.as_view()),

    # --- Step Record ---
    path('step_record', step_record_view.StepRecordListCreateView.as_view()),
    path('step_record/id/<int:pk>', step_record_view.StepRecordDetailView.as_view()),
    path('step_record/search/', step_record_view.StepRecordSearchView.as_view()),

    # --- Workout ---
    path('workout', workout_view.WorkoutListCreateView.as_view()),
    path('workout/id/<int:pk>', workout_view.WorkoutDetailView.as_view()),
    path('workout/search/', workout_view.WorkoutSearchView.as_view()),

    # --- Login ---
    path('login/', LoginView.as_view()),


]
