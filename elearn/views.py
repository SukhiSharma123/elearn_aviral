from .serializers import *
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView,ListAPIView
from .models import *
from .custom_permission import AdminCheckPermission,DeveloperAdminCheckPermission
from rest_framework.permissions import IsAuthenticated


class CreateandGetClass(ListCreateAPIView):
    permission_classes = [AdminCheckPermission]
    serializer_class = CreateandShowClassSerializer
    queryset = Class.objects.all()


class UpdateClass(RetrieveUpdateDestroyAPIView):
    permission_classes = [AdminCheckPermission]
    serializer_class = CreateandShowClassSerializer
    queryset = Class.objects.all()



class CreateandGetBooks(ListCreateAPIView):
    permission_classes = [AdminCheckPermission]
    serializer_class = CreateandListBooksSerializer
    queryset = Books.objects.all()

class UpdateBooks(RetrieveUpdateDestroyAPIView):
    permission_classes = [AdminCheckPermission]
    serializer_class = CreateandShowClassSerializer
    queryset = Books.objects.all()

class CreateandGetEventNotification(ListCreateAPIView):
    permission_classes = [AdminCheckPermission]
    serializer_class = CreateandShowEventNotificationSerializer
    queryset = EventNotification.objects.all()

class UpdateEventNotification(RetrieveUpdateDestroyAPIView):
    permission_classes = [AdminCheckPermission]
    serializer_class = CreateandShowClassSerializer
    queryset = EventNotification.objects.all()



class CreateandGetFeeNotification(ListCreateAPIView):
    permission_classes = [AdminCheckPermission]
    serializer_class = CreateandShowFeeNotificationSerializer
    queryset = FeeNotification.objects.all()

class UpdateFeeNotification(RetrieveUpdateDestroyAPIView):
    permission_classes = [AdminCheckPermission]
    serializer_class = CreateandShowClassSerializer
    queryset = FeeNotification.objects.all()



class CreateSettingLimitView(ListCreateAPIView):
    permission_classes=[AdminCheckPermission]
    serializer_class = CreateBooleanLimitSettingsSerializer
    queryset = Settings.objects.all()


class UpdateSettingLimitView(RetrieveUpdateDestroyAPIView):
    permission_classes=[AdminCheckPermission]
    serializer_class = CreateBooleanLimitSettingsSerializer
    queryset = Settings.objects.all()
    
class CreateFeedbackView(CreateAPIView):
    permission_classes = [AdminCheckPermission]
    serializer_class = FeedbackSerializer
    queryset = FeedBack.objects.all()


class GetFeedBackView(ListAPIView):
    permission_classes = [DeveloperAdminCheckPermission]
    serializer_class = FeedbackSerializer
    queryset = FeedBack.objects.all()

class UpdateFeedBack(RetrieveUpdateDestroyAPIView):
    permission_classes = [DeveloperAdminCheckPermission]
    serializer_class = FeedbackSerializer
    queryset = FeedBack.objects.all()


class CreateAboutAmdinView(ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=AboutAdminSerializer
    queryset = AboutAdmin.objects.all()
