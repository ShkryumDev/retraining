from rest_framework import serializers


class PhoneNumberValidator:
    def __call__(self, value):
        if not value.startswitch('7'):
            raise serializers.ValidationError('Номер должен начинаться с цифры 7')
        if len(str(value)) != 11:
            raise serializers.ValidationError('В номере должно быть 11 цифр')
