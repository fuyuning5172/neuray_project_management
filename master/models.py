from django.db import models

# Create your models here.


class Default(models.Model):
    """
    通用属性
    """
    is_delete = models.IntegerField('is_delete', default=0)
    create_time = models.DateTimeField('create_time', auto_now_add=True)
    update_time = models.DateTimeField('update_time', auto_now=True)
    delete_time = models.DateTimeField('delete_time', default=None)


class Person(Default):
    """
    人员表
    """
    personnel_id = models.AutoField('personnel_id', primary_key=True)
    personnel_name = models.CharField('personnel_name', max_length=50)
    department = models.CharField('department', max_length=50)

    class Meta:
        db_table = "Person"


class Stage(Default):
    """
    阶段表
    """
    stage_id = models.AutoField('stage_id', primary_key=True)
    stage_name = models.CharField('stage_name', max_length=50)
    begin_time = models.CharField('begin_time', max_length=50)
    end_time = models.CharField('end_time', max_length=50)
    progress = models.CharField('progress', max_length=20)
    personnel_ids = models.ManyToManyField(Person)

    class Meta:
        db_table = "Stage"


class Project(Default):
    """
    项目表
    """
    project_id = models.AutoField('project_id', primary_key=True)
    project_name = models.CharField('project_name', max_length=150)
    contract_no = models.CharField('contract_no', max_length=50, unique=True)
    project_amount = models.FloatField('project_amount')
    project_partner = models.CharField('project_partner', max_length=50)
    project_contact = models.CharField('project_contact', max_length=50)
    project_remark = models.CharField('project_remark', max_length=300)
    project_date = models.CharField('project_date',max_length=20)
    project_cycle = models.CharField('project_cycle', max_length=20)

    class Meta:
        db_table = "Project"


class Plan(Default):
    """
    计划表
    """
    plan_id = models.AutoField('自增ID', primary_key=True)
    plan_content = models.CharField('plan_content', max_length=300)
    project_id = models.ForeignKey(Project, to_field='project_id', on_delete=models.PROTECT)
    stage_id = models.ForeignKey(Stage, to_field='stage_id', on_delete=models.PROTECT)

    class Meta:
        db_table = "Plan"
