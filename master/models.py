from django.db import models

# Create your models here.


class Person(models.Model):
    """
    人员表
    """
    personnel_id = models.AutoField('personnel_id', primary_key=True)
    personnel_name = models.CharField('personnel_name', max_length=50)
    department = models.CharField('department', max_length=50)
    phone_number = models.IntegerField('phone_number', max_length=11, null=True)
    working_years = models.IntegerField('phone_number', max_length=10, null=True)
    is_delete = models.IntegerField('is_delete', default=0)
    create_time = models.DateTimeField('create_time', auto_now_add=True)
    update_time = models.DateTimeField('update_time', auto_now=True)
    delete_time = models.DateTimeField('delete_time', default=None, null=True)

    class Meta:
        db_table = "Person"


class Stage(models.Model):
    """
    阶段表
    """
    stage_id = models.AutoField('stage_id', primary_key=True)
    stage_name = models.CharField('stage_name', max_length=50)
    begin_time = models.CharField('begin_time', max_length=50, null=True)
    end_time = models.CharField('end_time', max_length=50, null=True)
    progress = models.CharField('progress', max_length=20, null=True)
    personnel_ids = models.ManyToManyField(Person, null=True)
    is_delete = models.IntegerField('is_delete', default=0)
    create_time = models.DateTimeField('create_time', auto_now_add=True)
    update_time = models.DateTimeField('update_time', auto_now=True)
    delete_time = models.DateTimeField('delete_time', default=None, null=True)

    class Meta:
        db_table = "Stage"


class Project(models.Model):
    """
    项目表
    """
    project_id = models.AutoField('project_id', primary_key=True)
    project_name = models.CharField('project_name', max_length=150)
    contract_no = models.CharField('contract_no', max_length=50, unique=True)
    project_amount = models.FloatField('project_amount', null=True)
    project_partner = models.CharField('project_partner', max_length=50, null=True)
    project_contact = models.CharField('project_contact', max_length=50, null=True)
    project_remark = models.CharField('project_remark', max_length=300, null=True)
    project_date = models.CharField('project_date', max_length=20, null=True)
    project_cycle = models.CharField('project_cycle', max_length=20, null=True)
    is_delete = models.IntegerField('is_delete', default=0)
    create_time = models.DateTimeField('create_time', auto_now_add=True)
    update_time = models.DateTimeField('update_time', auto_now=True)
    delete_time = models.DateTimeField('delete_time', default=None, null=True)

    class Meta:
        db_table = "Project"


class Plan(models.Model):
    """
    计划表
    """
    plan_id = models.AutoField('自增ID', primary_key=True)
    plan_content = models.CharField('plan_content', max_length=300)
    project_id = models.OneToOneField(Project, to_field='project_id', on_delete=models.PROTECT)
    stage_id = models.ForeignKey(Stage, to_field='stage_id', on_delete=models.PROTECT, null=True)
    is_delete = models.IntegerField('is_delete', default=0)
    create_time = models.DateTimeField('create_time', auto_now_add=True)
    update_time = models.DateTimeField('update_time', auto_now=True)
    delete_time = models.DateTimeField('delete_time', default=None, null=True)

    class Meta:
        db_table = "Plan"
