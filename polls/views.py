from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer, UserAuthSerializer, CourseSerializer, StudentSerializer, BuffetSerializer, \
    OperationSerializer, PinSerializer
from .models import User, Pin, Course, Student, Buffet, Operation


@api_view(['GET'])
def find_user_by_id(request, pin):
    """Находим Администратора по id"""
    if request.method == 'GET':
        user = User.objects.get(pin=pin)
        serializer = UserSerializer(user)
        return Response(serializer.data)


@api_view(['GET'])
def find_all_users(request):
    """Находим всех администраторов"""
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def save_user(request):
    """Создает нового администратора и автоматически выдает ему пин-код"""
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_obj = serializer.save()
            pin = Pin.objects.create(pin=user_obj.pin)
            pin.save()
            data = dict(serializer.data, **{"pin": user_obj.pin})
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def auth_user(request):
    if request.method == 'POST':
        check = User.objects.filter(phone=request.data['phone'], pin=request.data['pin'])
        if check:
            join = {
                "success": True,
                "message": "Добро Пожаловать"
            }
            return Response(join)
        bad_join = {
            "success": False
        }
        return Response(bad_join)


@api_view(['PUT'])
def update_user(request, pin):
    # """Оновляем данные адинистратора"""
    try:
        user = User.objects.get(pin=pin)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def find_all_courses(request):
    """Находит все курсы"""
    if request.method == 'GET':
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def find_course_by_id(request, pk):
    """Находим курсы по id"""
    if request.method == 'GET':
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)


@api_view(['POST'])
def save_course(request):
    """Создает новые курсы"""
    if request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_course(request, pk):
    """Обновляет данные о курсах"""
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def find_student_by_id(request, pin):
    """Находим студента по id"""
    if request.method == 'GET':
        student = Student.objects.get(pin=pin)
        serializer = StudentSerializer(student)
        return Response(serializer.data)


@api_view(['GET'])
def find_all_students(request):
    """Находим всех студентов"""
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def save_student(request):
    """Создает нового студента и автоматически выдает ему пин-код"""
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            student_obj = serializer.save()
            pin = Pin.objects.create(pin=student_obj.pin)
            pin.save()
            data = dict(serializer.data, **{"pin": student_obj.pin})
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_student(request, pin):
    # """Оновляем данные студента"""
    try:
        student = Student.objects.get(pin=pin)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def find_all_products(request):
    """Находит все продукты"""
    if request.method == 'GET':
        product = Buffet.objects.all()
        serializer = BuffetSerializer(product, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def find_product_by_id(request, pk):
    """Находим продукты по id"""
    if request.method == 'GET':
        product = Buffet.objects.get(pk=pk)
        serializer = BuffetSerializer(product)
        return Response(serializer.data)


@api_view(['GET'])
def find_product_by_active(request, status):
    """Находит продукты по статусу false или true"""
    if request.method == 'GET':
        status_translate = {'true': True, 'false': False}
        product = Buffet.objects.filter(active=status_translate[status.lower()]).values()
        return Response(product)


@api_view(['POST'])
def save_products(request):
    """Создает новые проудкты"""
    print(request.data)
    if request.method == 'POST':
        serializer = BuffetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_products(request, pk):
    # """Оновляем данные продуктов"""
    try:
        product = Buffet.objects.get(pk=pk)
    except Buffet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BuffetSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def find_operation_by_pin(request, pin):
    """Получить операции по id"""
    if request.method == 'GET':
        operation = Operation.objects.filter(pin=pin).values()
        return Response(operation)


@api_view(['POST'])
def save_operation(request):
    if request.method == 'POST':
        serializer = OperationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.save()
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def find_all_operations(request):
    """Находит все операции"""
    if request.method == 'GET':
        operation = Operation.objects.all().values()
        return Response(operation)


@api_view(['GET'])
def get_debt_sum_by_pin(request, pin):
    """Получает сумму долга студента по id"""
    if request.method == 'GET':
        try:
            pin = Pin.objects.get(pin=pin)
            serializer = PinSerializer(pin)
            return Response(serializer.data)
        except Pin.DoesNotExist:
            return Response("пользователь не существует")


@api_view(['PUT'])
def make_payment(request):
    """Оплачивает долги"""
    if request.method == 'PUT':
        pin_obj = Pin.objects.get(pin=request.data['pin'])
        serializer = PinSerializer(pin_obj, data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
