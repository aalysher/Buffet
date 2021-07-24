from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:pin>/', views.find_user_by_id),
    path('user/all/', views.find_all_users),
    path('user/save/', views.save_user),
    path('user/auth/', views.auth_user),
    path('user/update/<int:pin>/', views.update_user),

    path('course/all/', views.find_all_courses),
    path('course/<int:pk>/', views.find_course_by_id),
    path('course/save/', views.save_course),
    path('course/update/<int:pk>/', views.update_course),

    path('student/<int:pin>/', views.find_student_by_id),
    path('student/all/', views.find_all_students),
    path('student/save/', views.save_student),
    path('student/update/<int:pin>/', views.update_student),

    path('product/all/', views.find_all_products),
    path('product/<int:pk>/', views.find_product_by_id),
    path('product/save/', views.save_products),
    path('product/update/<int:pk>/', views.update_products),
    path('product/<str:status>/', views.find_product_by_active),

    path('operation/<int:pin>/', views.find_operation_by_pin),
    path('operation/append/', views.save_operation),
    path('operation/all/', views.find_all_operations),

    path('payment/<int:pin>/', views.get_debt_sum_by_pin),
    path('payment/make/', views.make_payment),

]
