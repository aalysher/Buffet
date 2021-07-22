from rest_framework import serializers

from .models import User, Course, Student, Buffet, OperationDetail, Pin, Operation
from .service import create_pin, get_debt_and_change, get_total_sum, get_status


class UserSerializer(serializers.ModelSerializer):
    pin = serializers.IntegerField(required=False)
    active = serializers.BooleanField(required=False)

    class Meta:
        model = User
        fields = ('phone', 'name', 'pin', 'active')

    def create(self, validated_data):
        pin = create_pin(validated_data['phone'], self.Meta.model)
        return self.Meta.model.objects.create(**validated_data, pin=pin)


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone', 'pin')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class StudentSerializer(UserSerializer):
    class Meta:
        model = Student
        fields = ('phone', 'name', 'course_id')


class BuffetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buffet
        fields = '__all__'



class OperationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationDetail
        fields = ('amount', 'buffet')


class OperationSerializer(serializers.Serializer):
    pin = serializers.CharField(max_length=6)
    payment = serializers.IntegerField()
    basket = OperationDetailSerializer(many=True)

    def create(self, validated_data):
        pin = Pin.objects.get(pin=validated_data['pin'])
        total_sum = get_total_sum(validated_data)
        debt_sum, change = get_debt_and_change(validated_data, total_sum)
        status = get_status(validated_data, total_sum)

        operation = Operation(total_sum=total_sum, debt_sum=debt_sum, pin=pin, status=status)
        operation.save()

        pin.debt += debt_sum
        pin.save()

        for item in validated_data["basket"]:
            food = Buffet.objects.get(pk=item['buffet'].id)
            op_detail = OperationDetail(amount=item['amount'], buffet=food, operations=operation)
            op_detail.save()
        return {
            "id": operation.id,
            "add_date": operation.add_date,
            "editDate": operation.edit_date,
            "pin": {
                "pin": pin.pin,
                "debt": pin.debt
            },
            "total": total_sum,
            "debt": debt_sum,
            "status": status,
            "change": change
        }


class PinSerializer(serializers.ModelSerializer):
    payment = serializers.IntegerField(required=False)

    class Meta:
        model = Pin
        fields = '__all__'

    def update(self, instance, validated_data):
        debt, change, = get_debt_and_change(validated_data, instance.debt)
        instance.debt = debt
        instance.save()
        return {
            'payment': validated_data['payment'],
            'debt': instance.debt,
            'change': change
        }
