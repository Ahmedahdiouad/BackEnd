# models.py
from django.db import models

class TemperatureData(models.Model):
    id = models.AutoField(primary_key=True)
    SensorID = models.TextField()
    Date_n_Time = models.TextField()
    Temperature = models.TextField()

    class Meta:
        db_table = 'Temperature_Data'  # Set the table name if it differs from the model name
        app_label = 'sensor'  # Specify the app label if necessary

class HumidityData(models.Model):
    id = models.AutoField(primary_key=True)
    SensorID = models.TextField()
    Date_n_Time = models.TextField()
    Humidity = models.TextField()

    class Meta:
        db_table = 'Humidity_Data'  # Set the table name if it differs from the model name
        app_label = 'sensor'  # Specify the app label if necessary

class FlowData(models.Model):
    id = models.AutoField(primary_key=True)
    SensorID = models.TextField()
    Date_n_Time = models.TextField()
    Flow = models.TextField()

    class Meta:
        db_table = 'Flow_Data'  # Set the table name if it differs from the model name
        app_label = 'sensor'  # Specify the app label if necessary

class PositionData(models.Model):
    id = models.AutoField(primary_key=True)
    SensorID = models.TextField()
    Date_n_Time = models.TextField()
    Position = models.TextField()

    class Meta:
        db_table = 'Position_Data'  # Set the table name if it differs from the model name
        app_label = 'sensor'  # Specify the app label if necessary

class PaintLevelData(models.Model):
    id = models.AutoField(primary_key=True)
    SensorID = models.TextField()
    Date_n_Time = models.TextField()
    PaintLevel = models.TextField()

    class Meta:
        db_table = 'PaintLevel_Data'  # Set the table name if it differs from the model name
        app_label = 'sensor'  # Specify the app label if necessary

class SurfaceQualityData(models.Model):
    id = models.AutoField(primary_key=True)
    SensorID = models.TextField()
    Date_n_Time = models.TextField()
    SurfaceQuality = models.TextField()

    class Meta:
        db_table = 'SurfaceQuality_Data'  # Set the table name if it differs from the model name
        app_label = 'sensor'  # Specify the app label if necessary

