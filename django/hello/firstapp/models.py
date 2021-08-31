# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class UpnGnssProject100(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    number = models.BigIntegerField(blank=True, null=True)
    region = models.CharField(max_length=254, blank=True, null=True)
    nameua = models.CharField(max_length=254, blank=True, null=True)
    nameen = models.CharField(max_length=254, blank=True, null=True)
    coatuu_code = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    y = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    x = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status_np_za_admin_podil = models.CharField(max_length=254, blank=True, null=True)
    districtce = models.CharField(max_length=254, blank=True, null=True)
    meteo = models.BigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    norway_project = models.BigIntegerField(blank=True, null=True)
    grounding = models.BigIntegerField(blank=True, null=True)
    site_repor = models.BigIntegerField(blank=True, null=True)
    reconaissa = models.BigIntegerField(blank=True, null=True)
    cabinet = models.BigIntegerField(blank=True, null=True)
    statusid = models.BigIntegerField(blank=True, null=True)
    dgk = models.BigIntegerField(blank=True, null=True)
    dgk_contac = models.CharField(max_length=254, blank=True, null=True)
    agreement = models.BigIntegerField(blank=True, null=True)
    primary_co = models.CharField(max_length=254, blank=True, null=True)
    rigc_ready = models.BigIntegerField(blank=True, null=True)
    sitechange = models.BigIntegerField(blank=True, null=True)
    installati = models.BigIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UPN_GNSS_project100'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FirstappArticle(models.Model):
    id = models.BigAutoField(primary_key=True)
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'firstapp_article'


class FirstappComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    author_name = models.CharField(max_length=50)
    comment_text = models.CharField(max_length=200)
    article = models.ForeignKey(FirstappArticle, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'firstapp_comment'


class Layer(models.Model):
    topology = models.OneToOneField('Topology', models.DO_NOTHING, primary_key=True)
    layer_id = models.IntegerField()
    schema_name = models.CharField(max_length=100)
    table_name = models.CharField(max_length=100)
    feature_column = models.CharField(max_length=100)
    feature_type = models.IntegerField()
    level = models.IntegerField()
    child_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layer'
        unique_together = (('topology', 'layer_id'), ('schema_name', 'table_name', 'feature_column'),)


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class Topology(models.Model):
    name = models.CharField(unique=True, max_length=100)
    srid = models.IntegerField()
    precision = models.FloatField()
    hasz = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'topology'

        def __str__(self):
        	return self.title
