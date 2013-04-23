# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.contrib.gis.db import models

class Accidente(models.Model):
    acc_id = models.DecimalField(primary_key=True,unique=True, max_digits=65535, decimal_places=65535)
    ure = models.ForeignKey('UbicacionRelativa')
    lum_cod = models.ForeignKey('Luminosidad', db_column='lum_cod')
    veh = models.ForeignKey('Vehiculo')
    veh_patente = models.CharField(max_length=20)
    eta = models.ForeignKey('EstadoAtmosferico')
    for_numero = models.ForeignKey('Formulario', db_column='for_numero')
    cac = models.ForeignKey('ClaseAccidente')
    sec = models.ForeignKey('SubSector')
    tca_cod = models.ForeignKey('TipoCalzada', db_column='tca_cod')
    cal_cod = models.ForeignKey('Calzada', db_column='cal_cod')
    com_codigo = models.ForeignKey('Comuna', db_column='com_codigo')
    con_cod = models.ForeignKey('CondicionCalzada', db_column='con_cod')
    tac = models.ForeignKey('TipoAccidente')
    acc_fecha = models.DateTimeField(null=True, blank=True)
    acc_hora = models.DateTimeField(null=True, blank=True)
    acc_detalle = models.CharField(max_length=255, blank=True)
    acc_mensaje = models.CharField(max_length=255, blank=True)
    acc_pista_ida = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    acc_pista_reg = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    acc_estado_cal = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    acc_muertos = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    acc_graves = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    acc_m_graves = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    acc_leves = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    acc_calle_uno = models.CharField(max_length=255, blank=True)
    acc_calle_dos = models.CharField(max_length=255, blank=True)
    acc_altura = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    acc_parte = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    acc_rolruta = models.CharField(max_length=255, blank=True)
    acc_kilometro = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    acc_folio = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    geom = models.PointField()
    objects = models.GeoManager()
    class Meta:
        db_table = 'accidente'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = 'auth_user_user_permissions'

class BaseBase(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    geom = models.PointField()
    objects = models.GeoManager()
    class Meta:
        db_table = 'base_base'

class Calzada(models.Model):
    cal_cod = models.DecimalField(primary_key=True,unique=True, max_digits=65535, decimal_places=65535)
    cal_descricpion = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'calzada'

class ClaseAccidente(models.Model):
    cac_id = models.DecimalField(primary_key=True,unique=True, max_digits=65535, decimal_places=65535)
    cac_descripcion = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'clase_accidente'

class Comisaria(models.Model):
    cmr_codigo = models.DecimalField(primary_key=True,unique=True, max_digits=65535, decimal_places=65535)
    cmr_nombre = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'comisaria'

class Comuna(models.Model):
    com_codigo = models.DecimalField(primary_key=True,unique=True, max_digits=65535, decimal_places=65535)
    reg_codigo = models.ForeignKey('Region', db_column='reg_codigo')
    com_nombre = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'comuna'

class Comuna2(models.Model):
    com_codigo2 = models.DecimalField(primary_key=True,unique=True, max_digits=65535, decimal_places=65535)
    com_nombre = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'comuna2'

class CondicionCalzada(models.Model):
    con_cod = models.DecimalField(primary_key=True,unique=True, max_digits=65535, decimal_places=65535)
    con_ddescriocion = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'condicion_calzada'

class Demarcacion(models.Model):
    dem_id = models.DecimalField(primary_key=True,unique=True, max_digits=65535, decimal_places=65535)
    dem_descripcion = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'demarcacion'

class DemarcacionAccidente(models.Model):
    dem = models.ForeignKey(Demarcacion)
    acc = models.ForeignKey(Accidente)
    class Meta:
        db_table = 'demarcacion_accidente'

class DetalleUbicacionRelativa(models.Model):
    ure_id2 = models.DecimalField(primary_key=True,unique=True, max_digits=65535, decimal_places=65535)
    acc = models.ForeignKey(Accidente)
    dur_descripcion = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'detalle_ubicacion_relativa'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'django_site'

class EstadoAtmosferico(models.Model):
    eta_id = models.DecimalField(primary_key=True,unique=True, max_digits=65535, decimal_places=65535)
    eta_descripcion = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'estado_atmosferico'

class Formulario(models.Model):
    for_numero = models.DecimalField(primary_key=True,unique=True, max_digits=65535, decimal_places=65535)
    res = models.ForeignKey('Responsable')
    for_fecha = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'formulario'

class GeographyColumns(models.Model):
    f_table_catalog = models.TextField(blank=True) # This field type is a guess.
    f_table_schema = models.TextField(blank=True) # This field type is a guess.
    f_table_name = models.TextField(blank=True) # This field type is a guess.
    f_geography_column = models.TextField(blank=True) # This field type is a guess.
    coord_dimension = models.IntegerField(null=True, blank=True)
    srid = models.IntegerField(null=True, blank=True)
    type = models.TextField(blank=True)
    class Meta:
        db_table = 'geography_columns'

class GeometryColumns(models.Model):
    f_table_catalog = models.CharField(max_length=256)
    f_table_schema = models.CharField(max_length=256)
    f_table_name = models.CharField(max_length=256)
    f_geometry_column = models.CharField(max_length=256)
    coord_dimension = models.IntegerField()
    srid = models.IntegerField()
    type = models.CharField(max_length=30)
    class Meta:
        db_table = 'geometry_columns'

class Luminosidad(models.Model):
    lum_cod = models.DecimalField(primary_key=True,unique=True, max_digits=65535, decimal_places=65535)
    lum_descripcion = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'luminosidad'

class Maniobra(models.Model):
    man_cod = models.DecimalField(primary_key=True,unique=True, max_digits=65535, decimal_places=65535)
    man_descripcion = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'maniobra'

class Personas(models.Model):
    per_id = models.DecimalField(primary_key=True,max_digits=65535, decimal_places=65535)
    per_run = models.DecimalField(max_digits=65535, decimal_places=65535)
    per_calidad = models.CharField(max_length=255, blank=True)
    per_genero = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    per_edad = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    per_resultado = models.CharField(max_length=255, blank=True)
    per_cinturon = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    com_codigo2 = models.ForeignKey(Comuna2, db_column='com_codigo2')
    acc = models.ForeignKey(Accidente)
    veh_id2 = models.ForeignKey('Vehiculo2', db_column='veh_id2')
    veh_patente2 = models.CharField(max_length=20)
    per_licencia = models.CharField(max_length=3, blank=True)
    per_codigo = models.CharField(max_length=255, blank=True)
    per_condicion = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    per_nacionalidad = models.CharField(max_length=100, blank=True)
    per_detenido = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    class Meta:
        db_table = 'personas'

class Region(models.Model):
    reg_codigo = models.DecimalField(primary_key=True,unique=True, max_digits=65535, decimal_places=65535)
    reg_nombre = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'region'

class Responsable(models.Model):
    res_id = models.DecimalField(primary_key=True,unique=True, max_digits=65535, decimal_places=65535)
    cmr_codigo = models.ForeignKey(Comisaria, db_column='cmr_codigo')
    res_nombre = models.CharField(max_length=255, blank=True)
    res_grado = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'responsable'

class Servicio(models.Model):
    ser_cod = models.DecimalField(primary_key=True,unique=True, max_digits=65535, decimal_places=65535)
    ser_descripcion = models.CharField(max_length=10, blank=True)
    class Meta:
        db_table = 'servicio'

class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True)
    auth_srid = models.IntegerField(null=True, blank=True)
    srtext = models.CharField(max_length=2048, blank=True)
    proj4text = models.CharField(max_length=2048, blank=True)
    class Meta:
        db_table = 'spatial_ref_sys'

class SubSector(models.Model):
    sec_id = models.DecimalField(primary_key=True,unique=True, max_digits=65535, decimal_places=65535)
    sec_descripcion = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'sub_sector'

class TipoAccidente(models.Model):
    tac_id = models.DecimalField(primary_key=True,unique=True, max_digits=65535, decimal_places=65535)
    tca_descripcion = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'tipo_accidente'

class TipoCalzada(models.Model):
    tca_cod = models.DecimalField(primary_key=True,unique=True, max_digits=65535, decimal_places=65535)
    tca_descripcion = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'tipo_calzada'

class TipoVehiculo(models.Model):
    tve_id = models.DecimalField(primary_key=True,unique=True, max_digits=65535, decimal_places=65535)
    tve_descripcion = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'tipo_vehiculo'

class UbicacionRelativa(models.Model):
    ure_id = models.DecimalField(primary_key=True,unique=True, max_digits=65535, decimal_places=65535)
    dur_descripcion = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'ubicacion_relativa'

class Vehiculo(models.Model):
    veh_id = models.DecimalField(primary_key=True,max_digits=65535, decimal_places=65535)
    veh_patente = models.CharField(max_length=20)
    tve = models.ForeignKey(TipoVehiculo)
    man_cod = models.ForeignKey(Maniobra, db_column='man_cod')
    ser_cod = models.ForeignKey(Servicio, db_column='ser_cod')
    veh_concecuencia = models.CharField(max_length=255, blank=True)
    veh_via = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    veh_direccion = models.CharField(max_length=100, blank=True)
    veh_marca = models.CharField(max_length=100, blank=True)
    veh_codigo = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'vehiculo'

class Vehiculo2(models.Model):
    veh_id2 = models.DecimalField(primary_key=True,max_digits=65535, decimal_places=65535)
    veh_patente2 = models.CharField(max_length=20)
    veh_concecuencia = models.CharField(max_length=255, blank=True)
    veh_via = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    veh_direccion = models.CharField(max_length=100, blank=True)
    veh_marca = models.CharField(max_length=100, blank=True)
    veh_codigo = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'vehiculo2'

