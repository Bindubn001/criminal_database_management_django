from django.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Crime(models.Model):
    crime_id = models.IntegerField(primary_key=True)
    crime_date = models.DateField()
    crime_type = models.CharField(max_length=30)
    crime_level = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    punishment = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crime'


class Criminal(models.Model):
    criminal_id = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=30)
    birthdate = models.DateField()
    address = models.CharField(max_length=30)
    dependent_name = models.CharField(max_length=30, blank=True, null=True)
    crime_id = models.IntegerField()
    prison = models.ForeignKey('Prison', models.DO_NOTHING)
    prison_term = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'criminal'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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

class Prison(models.Model):
    prison_id = models.IntegerField(primary_key=True)
    prison_name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    prison_level = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'prison'


class Trial(models.Model):
    case_id = models.IntegerField(primary_key=True)
    evidence = models.CharField(max_length=30)
    section_of_law = models.CharField(max_length=10)
    case_status = models.CharField(max_length=30)
    lawyer_id = models.IntegerField(blank=True, null=True)
    criminal = models.ForeignKey(Criminal, models.DO_NOTHING)
    victim = models.ForeignKey('Victim', models.DO_NOTHING)
    crime = models.ForeignKey(Crime, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'trial'


class Victim(models.Model):
    victim_id = models.IntegerField(primary_key=True)
    vname = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=10, blank=True, null=True)
    crime = models.ForeignKey(Crime, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'victim'


