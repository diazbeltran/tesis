# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Accidente'
        db.create_table(u'accidente', (
            ('acc_id', self.gf('django.db.models.fields.DecimalField')(unique=True, primary_key=True, decimal_places=65535, max_digits=65535)),
            ('ure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.UbicacionRelativa'])),
            ('lum_cod', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.Luminosidad'], db_column=u'lum_cod')),
            ('veh', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.Vehiculo'])),
            ('veh_patente', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('eta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.EstadoAtmosferico'])),
            ('for_numero', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.Formulario'], db_column=u'for_numero')),
            ('cac', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.ClaseAccidente'])),
            ('sec', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.SubSector'])),
            ('tca_cod', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.TipoCalzada'], db_column=u'tca_cod')),
            ('cal_cod', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.Calzada'], db_column=u'cal_cod')),
            ('com_codigo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.Comuna'], db_column=u'com_codigo')),
            ('con_cod', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.CondicionCalzada'], db_column=u'con_cod')),
            ('tac', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.TipoAccidente'])),
            ('acc_fecha', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('acc_hora', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('acc_detalle', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('acc_mensaje', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('acc_pista_ida', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=65535, decimal_places=65535, blank=True)),
            ('acc_pista_reg', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=65535, decimal_places=65535, blank=True)),
            ('acc_estado_cal', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=65535, decimal_places=65535, blank=True)),
            ('acc_muertos', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=65535, decimal_places=65535, blank=True)),
            ('acc_graves', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=65535, decimal_places=65535, blank=True)),
            ('acc_m_graves', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=65535, decimal_places=65535, blank=True)),
            ('acc_leves', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=65535, decimal_places=65535, blank=True)),
            ('acc_calle_uno', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('acc_calle_dos', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('acc_altura', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=65535, decimal_places=65535, blank=True)),
            ('acc_parte', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=65535, decimal_places=65535, blank=True)),
            ('acc_rolruta', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('acc_kilometro', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=65535, decimal_places=65535, blank=True)),
            ('acc_folio', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=65535, decimal_places=65535, blank=True)),
        ))
        db.send_create_signal(u'datos', ['Accidente'])

        # Adding model 'AuthGroup'
        db.create_table(u'auth_group', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal(u'datos', ['AuthGroup'])

        # Adding model 'AuthGroupPermissions'
        db.create_table(u'auth_group_permissions', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.AuthGroup'])),
            ('permission', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.AuthPermission'])),
        ))
        db.send_create_signal(u'datos', ['AuthGroupPermissions'])

        # Adding model 'AuthPermission'
        db.create_table(u'auth_permission', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.DjangoContentType'])),
            ('codename', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'datos', ['AuthPermission'])

        # Adding model 'AuthUser'
        db.create_table(u'auth_user', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')()),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'datos', ['AuthUser'])

        # Adding model 'AuthUserGroups'
        db.create_table(u'auth_user_groups', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.AuthUser'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.AuthGroup'])),
        ))
        db.send_create_signal(u'datos', ['AuthUserGroups'])

        # Adding model 'AuthUserUserPermissions'
        db.create_table(u'auth_user_user_permissions', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.AuthUser'])),
            ('permission', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.AuthPermission'])),
        ))
        db.send_create_signal(u'datos', ['AuthUserUserPermissions'])

        # Adding model 'BaseBase'
        db.create_table(u'base_base', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal(u'datos', ['BaseBase'])

        # Adding model 'Calzada'
        db.create_table(u'calzada', (
            ('cal_cod', self.gf('django.db.models.fields.DecimalField')(unique=True, primary_key=True, decimal_places=65535, max_digits=65535)),
            ('cal_descricpion', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'datos', ['Calzada'])

        # Adding model 'ClaseAccidente'
        db.create_table(u'clase_accidente', (
            ('cac_id', self.gf('django.db.models.fields.DecimalField')(unique=True, primary_key=True, decimal_places=65535, max_digits=65535)),
            ('cac_descripcion', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'datos', ['ClaseAccidente'])

        # Adding model 'Comisaria'
        db.create_table(u'comisaria', (
            ('cmr_codigo', self.gf('django.db.models.fields.DecimalField')(unique=True, primary_key=True, decimal_places=65535, max_digits=65535)),
            ('cmr_nombre', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'datos', ['Comisaria'])

        # Adding model 'Comuna'
        db.create_table(u'comuna', (
            ('com_codigo', self.gf('django.db.models.fields.DecimalField')(unique=True, primary_key=True, decimal_places=65535, max_digits=65535)),
            ('reg_codigo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.Region'], db_column=u'reg_codigo')),
            ('com_nombre', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'datos', ['Comuna'])

        # Adding model 'Comuna2'
        db.create_table(u'comuna2', (
            ('com_codigo2', self.gf('django.db.models.fields.DecimalField')(unique=True, primary_key=True, decimal_places=65535, max_digits=65535)),
            ('com_nombre', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'datos', ['Comuna2'])

        # Adding model 'CondicionCalzada'
        db.create_table(u'condicion_calzada', (
            ('con_cod', self.gf('django.db.models.fields.DecimalField')(unique=True, primary_key=True, decimal_places=65535, max_digits=65535)),
            ('con_ddescriocion', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'datos', ['CondicionCalzada'])

        # Adding model 'Demarcacion'
        db.create_table(u'demarcacion', (
            ('dem_id', self.gf('django.db.models.fields.DecimalField')(unique=True, primary_key=True, decimal_places=65535, max_digits=65535)),
            ('dem_descripcion', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'datos', ['Demarcacion'])

        # Adding model 'DemarcacionAccidente'
        db.create_table(u'demarcacion_accidente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dem', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.Demarcacion'])),
            ('acc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.Accidente'])),
        ))
        db.send_create_signal(u'datos', ['DemarcacionAccidente'])

        # Adding model 'DetalleUbicacionRelativa'
        db.create_table(u'detalle_ubicacion_relativa', (
            ('ure_id2', self.gf('django.db.models.fields.DecimalField')(unique=True, primary_key=True, decimal_places=65535, max_digits=65535)),
            ('acc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.Accidente'])),
            ('dur_descripcion', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'datos', ['DetalleUbicacionRelativa'])

        # Adding model 'DjangoAdminLog'
        db.create_table(u'django_admin_log', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('action_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.AuthUser'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.DjangoContentType'], null=True, blank=True)),
            ('object_id', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('object_repr', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('action_flag', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('change_message', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'datos', ['DjangoAdminLog'])

        # Adding model 'DjangoContentType'
        db.create_table(u'django_content_type', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('app_label', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'datos', ['DjangoContentType'])

        # Adding model 'DjangoSession'
        db.create_table(u'django_session', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('session_key', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('session_data', self.gf('django.db.models.fields.TextField')()),
            ('expire_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'datos', ['DjangoSession'])

        # Adding model 'DjangoSite'
        db.create_table(u'django_site', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('domain', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'datos', ['DjangoSite'])

        # Adding model 'EstadoAtmosferico'
        db.create_table(u'estado_atmosferico', (
            ('eta_id', self.gf('django.db.models.fields.DecimalField')(unique=True, primary_key=True, decimal_places=65535, max_digits=65535)),
            ('eta_descripcion', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'datos', ['EstadoAtmosferico'])

        # Adding model 'Formulario'
        db.create_table(u'formulario', (
            ('for_numero', self.gf('django.db.models.fields.DecimalField')(unique=True, primary_key=True, decimal_places=65535, max_digits=65535)),
            ('res', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.Responsable'])),
            ('for_fecha', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'datos', ['Formulario'])

        # Adding model 'GeographyColumns'
        db.create_table(u'geography_columns', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('f_table_catalog', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('f_table_schema', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('f_table_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('f_geography_column', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('coord_dimension', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('srid', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'datos', ['GeographyColumns'])

        # Adding model 'GeometryColumns'
        db.create_table(u'geometry_columns', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('f_table_catalog', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('f_table_schema', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('f_table_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('f_geometry_column', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('coord_dimension', self.gf('django.db.models.fields.IntegerField')()),
            ('srid', self.gf('django.db.models.fields.IntegerField')()),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'datos', ['GeometryColumns'])

        # Adding model 'Luminosidad'
        db.create_table(u'luminosidad', (
            ('lum_cod', self.gf('django.db.models.fields.DecimalField')(unique=True, primary_key=True, decimal_places=65535, max_digits=65535)),
            ('lum_descripcion', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'datos', ['Luminosidad'])

        # Adding model 'Maniobra'
        db.create_table(u'maniobra', (
            ('man_cod', self.gf('django.db.models.fields.DecimalField')(unique=True, primary_key=True, decimal_places=65535, max_digits=65535)),
            ('man_descripcion', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'datos', ['Maniobra'])

        # Adding model 'Personas'
        db.create_table(u'personas', (
            ('per_id', self.gf('django.db.models.fields.DecimalField')(primary_key=True, decimal_places=65535, max_digits=65535)),
            ('per_run', self.gf('django.db.models.fields.DecimalField')(max_digits=65535, decimal_places=65535)),
            ('per_calidad', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('per_genero', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=65535, decimal_places=65535, blank=True)),
            ('per_edad', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=65535, decimal_places=65535, blank=True)),
            ('per_resultado', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('per_cinturon', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=65535, decimal_places=65535, blank=True)),
            ('com_codigo2', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.Comuna2'], db_column=u'com_codigo2')),
            ('acc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.Accidente'])),
            ('veh_id2', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.Vehiculo2'], db_column=u'veh_id2')),
            ('veh_patente2', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('per_licencia', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('per_codigo', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('per_condicion', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=65535, decimal_places=65535, blank=True)),
            ('per_nacionalidad', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('per_detenido', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=65535, decimal_places=65535, blank=True)),
        ))
        db.send_create_signal(u'datos', ['Personas'])

        # Adding model 'Region'
        db.create_table(u'region', (
            ('reg_codigo', self.gf('django.db.models.fields.DecimalField')(unique=True, primary_key=True, decimal_places=65535, max_digits=65535)),
            ('reg_nombre', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'datos', ['Region'])

        # Adding model 'Responsable'
        db.create_table(u'responsable', (
            ('res_id', self.gf('django.db.models.fields.DecimalField')(unique=True, primary_key=True, decimal_places=65535, max_digits=65535)),
            ('cmr_codigo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.Comisaria'], db_column=u'cmr_codigo')),
            ('res_nombre', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('res_grado', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'datos', ['Responsable'])

        # Adding model 'Servicio'
        db.create_table(u'servicio', (
            ('ser_cod', self.gf('django.db.models.fields.DecimalField')(unique=True, primary_key=True, decimal_places=65535, max_digits=65535)),
            ('ser_descripcion', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
        ))
        db.send_create_signal(u'datos', ['Servicio'])

        # Adding model 'SpatialRefSys'
        db.create_table(u'spatial_ref_sys', (
            ('srid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('auth_name', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('auth_srid', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('srtext', self.gf('django.db.models.fields.CharField')(max_length=2048, blank=True)),
            ('proj4text', self.gf('django.db.models.fields.CharField')(max_length=2048, blank=True)),
        ))
        db.send_create_signal(u'datos', ['SpatialRefSys'])

        # Adding model 'SubSector'
        db.create_table(u'sub_sector', (
            ('sec_id', self.gf('django.db.models.fields.DecimalField')(unique=True, primary_key=True, decimal_places=65535, max_digits=65535)),
            ('sec_descripcion', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'datos', ['SubSector'])

        # Adding model 'TipoAccidente'
        db.create_table(u'tipo_accidente', (
            ('tac_id', self.gf('django.db.models.fields.DecimalField')(unique=True, primary_key=True, decimal_places=65535, max_digits=65535)),
            ('tca_descripcion', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'datos', ['TipoAccidente'])

        # Adding model 'TipoCalzada'
        db.create_table(u'tipo_calzada', (
            ('tca_cod', self.gf('django.db.models.fields.DecimalField')(unique=True, primary_key=True, decimal_places=65535, max_digits=65535)),
            ('tca_descripcion', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'datos', ['TipoCalzada'])

        # Adding model 'TipoVehiculo'
        db.create_table(u'tipo_vehiculo', (
            ('tve_id', self.gf('django.db.models.fields.DecimalField')(unique=True, primary_key=True, decimal_places=65535, max_digits=65535)),
            ('tve_descripcion', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'datos', ['TipoVehiculo'])

        # Adding model 'UbicacionRelativa'
        db.create_table(u'ubicacion_relativa', (
            ('ure_id', self.gf('django.db.models.fields.DecimalField')(unique=True, primary_key=True, decimal_places=65535, max_digits=65535)),
            ('dur_descripcion', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'datos', ['UbicacionRelativa'])

        # Adding model 'Vehiculo'
        db.create_table(u'vehiculo', (
            ('veh_id', self.gf('django.db.models.fields.DecimalField')(primary_key=True, decimal_places=65535, max_digits=65535)),
            ('veh_patente', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('tve', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.TipoVehiculo'])),
            ('man_cod', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.Maniobra'], db_column=u'man_cod')),
            ('ser_cod', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datos.Servicio'], db_column=u'ser_cod')),
            ('veh_concecuencia', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('veh_via', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=65535, decimal_places=65535, blank=True)),
            ('veh_direccion', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('veh_marca', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('veh_codigo', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'datos', ['Vehiculo'])

        # Adding model 'Vehiculo2'
        db.create_table(u'vehiculo2', (
            ('veh_id2', self.gf('django.db.models.fields.DecimalField')(primary_key=True, decimal_places=65535, max_digits=65535)),
            ('veh_patente2', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('veh_concecuencia', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('veh_via', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=65535, decimal_places=65535, blank=True)),
            ('veh_direccion', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('veh_marca', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('veh_codigo', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'datos', ['Vehiculo2'])


    def backwards(self, orm):
        # Deleting model 'Accidente'
        db.delete_table(u'accidente')

        # Deleting model 'AuthGroup'
        db.delete_table(u'auth_group')

        # Deleting model 'AuthGroupPermissions'
        db.delete_table(u'auth_group_permissions')

        # Deleting model 'AuthPermission'
        db.delete_table(u'auth_permission')

        # Deleting model 'AuthUser'
        db.delete_table(u'auth_user')

        # Deleting model 'AuthUserGroups'
        db.delete_table(u'auth_user_groups')

        # Deleting model 'AuthUserUserPermissions'
        db.delete_table(u'auth_user_user_permissions')

        # Deleting model 'BaseBase'
        db.delete_table(u'base_base')

        # Deleting model 'Calzada'
        db.delete_table(u'calzada')

        # Deleting model 'ClaseAccidente'
        db.delete_table(u'clase_accidente')

        # Deleting model 'Comisaria'
        db.delete_table(u'comisaria')

        # Deleting model 'Comuna'
        db.delete_table(u'comuna')

        # Deleting model 'Comuna2'
        db.delete_table(u'comuna2')

        # Deleting model 'CondicionCalzada'
        db.delete_table(u'condicion_calzada')

        # Deleting model 'Demarcacion'
        db.delete_table(u'demarcacion')

        # Deleting model 'DemarcacionAccidente'
        db.delete_table(u'demarcacion_accidente')

        # Deleting model 'DetalleUbicacionRelativa'
        db.delete_table(u'detalle_ubicacion_relativa')

        # Deleting model 'DjangoAdminLog'
        db.delete_table(u'django_admin_log')

        # Deleting model 'DjangoContentType'
        db.delete_table(u'django_content_type')

        # Deleting model 'DjangoSession'
        db.delete_table(u'django_session')

        # Deleting model 'DjangoSite'
        db.delete_table(u'django_site')

        # Deleting model 'EstadoAtmosferico'
        db.delete_table(u'estado_atmosferico')

        # Deleting model 'Formulario'
        db.delete_table(u'formulario')

        # Deleting model 'GeographyColumns'
        db.delete_table(u'geography_columns')

        # Deleting model 'GeometryColumns'
        db.delete_table(u'geometry_columns')

        # Deleting model 'Luminosidad'
        db.delete_table(u'luminosidad')

        # Deleting model 'Maniobra'
        db.delete_table(u'maniobra')

        # Deleting model 'Personas'
        db.delete_table(u'personas')

        # Deleting model 'Region'
        db.delete_table(u'region')

        # Deleting model 'Responsable'
        db.delete_table(u'responsable')

        # Deleting model 'Servicio'
        db.delete_table(u'servicio')

        # Deleting model 'SpatialRefSys'
        db.delete_table(u'spatial_ref_sys')

        # Deleting model 'SubSector'
        db.delete_table(u'sub_sector')

        # Deleting model 'TipoAccidente'
        db.delete_table(u'tipo_accidente')

        # Deleting model 'TipoCalzada'
        db.delete_table(u'tipo_calzada')

        # Deleting model 'TipoVehiculo'
        db.delete_table(u'tipo_vehiculo')

        # Deleting model 'UbicacionRelativa'
        db.delete_table(u'ubicacion_relativa')

        # Deleting model 'Vehiculo'
        db.delete_table(u'vehiculo')

        # Deleting model 'Vehiculo2'
        db.delete_table(u'vehiculo2')


    models = {
        u'datos.accidente': {
            'Meta': {'object_name': 'Accidente', 'db_table': "u'accidente'"},
            'acc_altura': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '65535', 'decimal_places': '65535', 'blank': 'True'}),
            'acc_calle_dos': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'acc_calle_uno': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'acc_detalle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'acc_estado_cal': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '65535', 'decimal_places': '65535', 'blank': 'True'}),
            'acc_fecha': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'acc_folio': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '65535', 'decimal_places': '65535', 'blank': 'True'}),
            'acc_graves': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '65535', 'decimal_places': '65535', 'blank': 'True'}),
            'acc_hora': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'acc_id': ('django.db.models.fields.DecimalField', [], {'unique': 'True', 'primary_key': 'True', 'decimal_places': '65535', 'max_digits': '65535'}),
            'acc_kilometro': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '65535', 'decimal_places': '65535', 'blank': 'True'}),
            'acc_leves': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '65535', 'decimal_places': '65535', 'blank': 'True'}),
            'acc_m_graves': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '65535', 'decimal_places': '65535', 'blank': 'True'}),
            'acc_mensaje': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'acc_muertos': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '65535', 'decimal_places': '65535', 'blank': 'True'}),
            'acc_parte': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '65535', 'decimal_places': '65535', 'blank': 'True'}),
            'acc_pista_ida': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '65535', 'decimal_places': '65535', 'blank': 'True'}),
            'acc_pista_reg': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '65535', 'decimal_places': '65535', 'blank': 'True'}),
            'acc_rolruta': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cac': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.ClaseAccidente']"}),
            'cal_cod': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.Calzada']", 'db_column': "u'cal_cod'"}),
            'com_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.Comuna']", 'db_column': "u'com_codigo'"}),
            'con_cod': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.CondicionCalzada']", 'db_column': "u'con_cod'"}),
            'eta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.EstadoAtmosferico']"}),
            'for_numero': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.Formulario']", 'db_column': "u'for_numero'"}),
            'lum_cod': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.Luminosidad']", 'db_column': "u'lum_cod'"}),
            'sec': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.SubSector']"}),
            'tac': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.TipoAccidente']"}),
            'tca_cod': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.TipoCalzada']", 'db_column': "u'tca_cod'"}),
            'ure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.UbicacionRelativa']"}),
            'veh': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.Vehiculo']"}),
            'veh_patente': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'datos.authgroup': {
            'Meta': {'object_name': 'AuthGroup', 'db_table': "u'auth_group'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'datos.authgrouppermissions': {
            'Meta': {'object_name': 'AuthGroupPermissions', 'db_table': "u'auth_group_permissions'"},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.AuthGroup']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'permission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.AuthPermission']"})
        },
        u'datos.authpermission': {
            'Meta': {'object_name': 'AuthPermission', 'db_table': "u'auth_permission'"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.DjangoContentType']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'datos.authuser': {
            'Meta': {'object_name': 'AuthUser', 'db_table': "u'auth_user'"},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'datos.authusergroups': {
            'Meta': {'object_name': 'AuthUserGroups', 'db_table': "u'auth_user_groups'"},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.AuthGroup']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.AuthUser']"})
        },
        u'datos.authuseruserpermissions': {
            'Meta': {'object_name': 'AuthUserUserPermissions', 'db_table': "u'auth_user_user_permissions'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'permission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.AuthPermission']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.AuthUser']"})
        },
        u'datos.basebase': {
            'Meta': {'object_name': 'BaseBase', 'db_table': "u'base_base'"},
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'datos.calzada': {
            'Meta': {'object_name': 'Calzada', 'db_table': "u'calzada'"},
            'cal_cod': ('django.db.models.fields.DecimalField', [], {'unique': 'True', 'primary_key': 'True', 'decimal_places': '65535', 'max_digits': '65535'}),
            'cal_descricpion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'datos.claseaccidente': {
            'Meta': {'object_name': 'ClaseAccidente', 'db_table': "u'clase_accidente'"},
            'cac_descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cac_id': ('django.db.models.fields.DecimalField', [], {'unique': 'True', 'primary_key': 'True', 'decimal_places': '65535', 'max_digits': '65535'})
        },
        u'datos.comisaria': {
            'Meta': {'object_name': 'Comisaria', 'db_table': "u'comisaria'"},
            'cmr_codigo': ('django.db.models.fields.DecimalField', [], {'unique': 'True', 'primary_key': 'True', 'decimal_places': '65535', 'max_digits': '65535'}),
            'cmr_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'datos.comuna': {
            'Meta': {'object_name': 'Comuna', 'db_table': "u'comuna'"},
            'com_codigo': ('django.db.models.fields.DecimalField', [], {'unique': 'True', 'primary_key': 'True', 'decimal_places': '65535', 'max_digits': '65535'}),
            'com_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'reg_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.Region']", 'db_column': "u'reg_codigo'"})
        },
        u'datos.comuna2': {
            'Meta': {'object_name': 'Comuna2', 'db_table': "u'comuna2'"},
            'com_codigo2': ('django.db.models.fields.DecimalField', [], {'unique': 'True', 'primary_key': 'True', 'decimal_places': '65535', 'max_digits': '65535'}),
            'com_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'datos.condicioncalzada': {
            'Meta': {'object_name': 'CondicionCalzada', 'db_table': "u'condicion_calzada'"},
            'con_cod': ('django.db.models.fields.DecimalField', [], {'unique': 'True', 'primary_key': 'True', 'decimal_places': '65535', 'max_digits': '65535'}),
            'con_ddescriocion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'datos.demarcacion': {
            'Meta': {'object_name': 'Demarcacion', 'db_table': "u'demarcacion'"},
            'dem_descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'dem_id': ('django.db.models.fields.DecimalField', [], {'unique': 'True', 'primary_key': 'True', 'decimal_places': '65535', 'max_digits': '65535'})
        },
        u'datos.demarcacionaccidente': {
            'Meta': {'object_name': 'DemarcacionAccidente', 'db_table': "u'demarcacion_accidente'"},
            'acc': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.Accidente']"}),
            'dem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.Demarcacion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'datos.detalleubicacionrelativa': {
            'Meta': {'object_name': 'DetalleUbicacionRelativa', 'db_table': "u'detalle_ubicacion_relativa'"},
            'acc': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.Accidente']"}),
            'dur_descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ure_id2': ('django.db.models.fields.DecimalField', [], {'unique': 'True', 'primary_key': 'True', 'decimal_places': '65535', 'max_digits': '65535'})
        },
        u'datos.djangoadminlog': {
            'Meta': {'object_name': 'DjangoAdminLog', 'db_table': "u'django_admin_log'"},
            'action_flag': ('django.db.models.fields.SmallIntegerField', [], {}),
            'action_time': ('django.db.models.fields.DateTimeField', [], {}),
            'change_message': ('django.db.models.fields.TextField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.DjangoContentType']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'object_repr': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.AuthUser']"})
        },
        u'datos.djangocontenttype': {
            'Meta': {'object_name': 'DjangoContentType', 'db_table': "u'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'datos.djangosession': {
            'Meta': {'object_name': 'DjangoSession', 'db_table': "u'django_session'"},
            'expire_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'session_data': ('django.db.models.fields.TextField', [], {}),
            'session_key': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'datos.djangosite': {
            'Meta': {'object_name': 'DjangoSite', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'datos.estadoatmosferico': {
            'Meta': {'object_name': 'EstadoAtmosferico', 'db_table': "u'estado_atmosferico'"},
            'eta_descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'eta_id': ('django.db.models.fields.DecimalField', [], {'unique': 'True', 'primary_key': 'True', 'decimal_places': '65535', 'max_digits': '65535'})
        },
        u'datos.formulario': {
            'Meta': {'object_name': 'Formulario', 'db_table': "u'formulario'"},
            'for_fecha': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'for_numero': ('django.db.models.fields.DecimalField', [], {'unique': 'True', 'primary_key': 'True', 'decimal_places': '65535', 'max_digits': '65535'}),
            'res': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.Responsable']"})
        },
        u'datos.geographycolumns': {
            'Meta': {'object_name': 'GeographyColumns', 'db_table': "u'geography_columns'"},
            'coord_dimension': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'f_geography_column': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'f_table_catalog': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'f_table_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'f_table_schema': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'srid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'datos.geometrycolumns': {
            'Meta': {'object_name': 'GeometryColumns', 'db_table': "u'geometry_columns'"},
            'coord_dimension': ('django.db.models.fields.IntegerField', [], {}),
            'f_geometry_column': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'f_table_catalog': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'f_table_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'f_table_schema': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'srid': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'datos.luminosidad': {
            'Meta': {'object_name': 'Luminosidad', 'db_table': "u'luminosidad'"},
            'lum_cod': ('django.db.models.fields.DecimalField', [], {'unique': 'True', 'primary_key': 'True', 'decimal_places': '65535', 'max_digits': '65535'}),
            'lum_descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'datos.maniobra': {
            'Meta': {'object_name': 'Maniobra', 'db_table': "u'maniobra'"},
            'man_cod': ('django.db.models.fields.DecimalField', [], {'unique': 'True', 'primary_key': 'True', 'decimal_places': '65535', 'max_digits': '65535'}),
            'man_descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'datos.personas': {
            'Meta': {'object_name': 'Personas', 'db_table': "u'personas'"},
            'acc': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.Accidente']"}),
            'com_codigo2': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.Comuna2']", 'db_column': "u'com_codigo2'"}),
            'per_calidad': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'per_cinturon': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '65535', 'decimal_places': '65535', 'blank': 'True'}),
            'per_codigo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'per_condicion': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '65535', 'decimal_places': '65535', 'blank': 'True'}),
            'per_detenido': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '65535', 'decimal_places': '65535', 'blank': 'True'}),
            'per_edad': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '65535', 'decimal_places': '65535', 'blank': 'True'}),
            'per_genero': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '65535', 'decimal_places': '65535', 'blank': 'True'}),
            'per_id': ('django.db.models.fields.DecimalField', [], {'primary_key': 'True', 'decimal_places': '65535', 'max_digits': '65535'}),
            'per_licencia': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'per_nacionalidad': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'per_resultado': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'per_run': ('django.db.models.fields.DecimalField', [], {'max_digits': '65535', 'decimal_places': '65535'}),
            'veh_id2': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.Vehiculo2']", 'db_column': "u'veh_id2'"}),
            'veh_patente2': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'datos.region': {
            'Meta': {'object_name': 'Region', 'db_table': "u'region'"},
            'reg_codigo': ('django.db.models.fields.DecimalField', [], {'unique': 'True', 'primary_key': 'True', 'decimal_places': '65535', 'max_digits': '65535'}),
            'reg_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'datos.responsable': {
            'Meta': {'object_name': 'Responsable', 'db_table': "u'responsable'"},
            'cmr_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.Comisaria']", 'db_column': "u'cmr_codigo'"}),
            'res_grado': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'res_id': ('django.db.models.fields.DecimalField', [], {'unique': 'True', 'primary_key': 'True', 'decimal_places': '65535', 'max_digits': '65535'}),
            'res_nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'datos.servicio': {
            'Meta': {'object_name': 'Servicio', 'db_table': "u'servicio'"},
            'ser_cod': ('django.db.models.fields.DecimalField', [], {'unique': 'True', 'primary_key': 'True', 'decimal_places': '65535', 'max_digits': '65535'}),
            'ser_descripcion': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        },
        u'datos.spatialrefsys': {
            'Meta': {'object_name': 'SpatialRefSys', 'db_table': "u'spatial_ref_sys'"},
            'auth_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'auth_srid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'proj4text': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'blank': 'True'}),
            'srid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'srtext': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'blank': 'True'})
        },
        u'datos.subsector': {
            'Meta': {'object_name': 'SubSector', 'db_table': "u'sub_sector'"},
            'sec_descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sec_id': ('django.db.models.fields.DecimalField', [], {'unique': 'True', 'primary_key': 'True', 'decimal_places': '65535', 'max_digits': '65535'})
        },
        u'datos.tipoaccidente': {
            'Meta': {'object_name': 'TipoAccidente', 'db_table': "u'tipo_accidente'"},
            'tac_id': ('django.db.models.fields.DecimalField', [], {'unique': 'True', 'primary_key': 'True', 'decimal_places': '65535', 'max_digits': '65535'}),
            'tca_descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'datos.tipocalzada': {
            'Meta': {'object_name': 'TipoCalzada', 'db_table': "u'tipo_calzada'"},
            'tca_cod': ('django.db.models.fields.DecimalField', [], {'unique': 'True', 'primary_key': 'True', 'decimal_places': '65535', 'max_digits': '65535'}),
            'tca_descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'datos.tipovehiculo': {
            'Meta': {'object_name': 'TipoVehiculo', 'db_table': "u'tipo_vehiculo'"},
            'tve_descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tve_id': ('django.db.models.fields.DecimalField', [], {'unique': 'True', 'primary_key': 'True', 'decimal_places': '65535', 'max_digits': '65535'})
        },
        u'datos.ubicacionrelativa': {
            'Meta': {'object_name': 'UbicacionRelativa', 'db_table': "u'ubicacion_relativa'"},
            'dur_descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ure_id': ('django.db.models.fields.DecimalField', [], {'unique': 'True', 'primary_key': 'True', 'decimal_places': '65535', 'max_digits': '65535'})
        },
        u'datos.vehiculo': {
            'Meta': {'object_name': 'Vehiculo', 'db_table': "u'vehiculo'"},
            'man_cod': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.Maniobra']", 'db_column': "u'man_cod'"}),
            'ser_cod': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.Servicio']", 'db_column': "u'ser_cod'"}),
            'tve': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datos.TipoVehiculo']"}),
            'veh_codigo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'veh_concecuencia': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'veh_direccion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'veh_id': ('django.db.models.fields.DecimalField', [], {'primary_key': 'True', 'decimal_places': '65535', 'max_digits': '65535'}),
            'veh_marca': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'veh_patente': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'veh_via': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '65535', 'decimal_places': '65535', 'blank': 'True'})
        },
        u'datos.vehiculo2': {
            'Meta': {'object_name': 'Vehiculo2', 'db_table': "u'vehiculo2'"},
            'veh_codigo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'veh_concecuencia': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'veh_direccion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'veh_id2': ('django.db.models.fields.DecimalField', [], {'primary_key': 'True', 'decimal_places': '65535', 'max_digits': '65535'}),
            'veh_marca': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'veh_patente2': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'veh_via': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '65535', 'decimal_places': '65535', 'blank': 'True'})
        }
    }

    complete_apps = ['datos']