# Generated by Django 5.0.3 on 2024-05-22 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(db_comment='Patient ID', db_index=True, help_text='Patient ID', max_length=36)),
                ('gmt_reg', models.DateTimeField(db_comment='患者登记时间', help_text='患者登记时间', verbose_name='患者登记时间')),
                ('id_no', models.CharField(db_comment='证件号码', max_length=36, verbose_name='证件号码')),
                ('id_code', models.CharField(db_comment='证件类型代码', max_length=2, verbose_name='证件类型代码')),
                ('patient_name', models.CharField(db_comment='患者姓名', max_length=36, verbose_name='患者姓名')),
                ('tel_no', models.CharField(db_comment='联系电话', max_length=36, verbose_name='联系电话')),
                ('sex_code', models.CharField(db_comment='性别代码', max_length=36, verbose_name='性别代码')),
                ('gmt_birth', models.DateField(db_comment='出生日期', verbose_name='出生日期')),
                ('addr_sal', models.CharField(db_comment='完整地址描述', max_length=128, verbose_name='完整地址描述')),
                ('addr_sta', models.CharField(blank=True, db_comment='自治区、直辖市', max_length=36, null=True, verbose_name='自治区、直辖市')),
                ('addr_cty', models.CharField(blank=True, db_comment='地址-市（地区）', max_length=36, null=True, verbose_name='地址-市（地区）')),
                ('addr_cnt', models.CharField(blank=True, db_comment='地址-县（区）', max_length=36, null=True, verbose_name='地址-县（区）')),
                ('addr_stb', models.CharField(blank=True, db_comment='地址-乡（镇、街道办事处）', max_length=36, null=True, verbose_name='地址-乡（镇、街道办事处）')),
                ('addr_str', models.CharField(blank=True, db_comment='地址-村（街、路、弄等）', max_length=36, null=True, verbose_name='地址-村（街、路、弄等）')),
                ('addr_bnr', models.CharField(blank=True, db_comment='地址-门牌号码', max_length=36, null=True, verbose_name='地址-门牌号码')),
                ('addr_zip', models.CharField(blank=True, db_comment='邮政编码', max_length=36, null=True, verbose_name='邮政编码')),
                ('marital_status_code', models.CharField(db_comment='婚姻状况代码', max_length=36, verbose_name='婚姻状况代码')),
                ('ethnic_group_code', models.CharField(db_comment='民族代码', max_length=36, verbose_name='民族代码')),
                ('occupation_code', models.CharField(db_comment='职业类别代码', max_length=36, verbose_name='职业类别代码')),
                ('work_org', models.CharField(blank=True, db_comment='工作单位', max_length=36, null=True, verbose_name='工作单位')),
                ('work_org_tel', models.CharField(blank=True, db_comment='工作单位联系电话', max_length=36, null=True, verbose_name='工作单位联系电话')),
                ('hcard_no', models.CharField(blank=True, db_comment='健康卡号', max_length=36, null=True, verbose_name='健康卡号')),
                ('hcard_org_code', models.CharField(blank=True, db_comment='健康卡发放机构代码', max_length=36, null=True, verbose_name='健康卡发放机构代码')),
                ('gcard_no', models.CharField(blank=True, db_comment='城乡居民健康档案编号', max_length=36, null=True, verbose_name='城乡居民健康档案编号')),
                ('gcard_org_code', models.CharField(blank=True, db_comment='建档医疗机构组织机构代码', max_length=36, null=True, verbose_name='建档医疗机构组织机构代码')),
                ('contact_code', models.CharField(db_comment='联系人关系代码', max_length=36, verbose_name='联系人关系代码')),
                ('contact_tel', models.CharField(db_comment='联系人电话', max_length=36, verbose_name='联系人电话')),
                ('contact_cname', models.CharField(db_comment='联系人姓名', max_length=36, verbose_name='联系人姓名')),
                ('org_code', models.CharField(db_comment='组织机构代码', max_length=36, verbose_name='组织机构代码')),
                ('org_name', models.CharField(db_comment='组织机构名称', max_length=36, verbose_name='组织机构名称')),
                ('ins_code', models.CharField(db_comment='医疗保险类别代码', max_length=36, verbose_name='医疗保险类别代码')),
                ('author_id', models.CharField(db_comment='登记人ID', max_length=36, verbose_name='登记人ID')),
                ('author', models.CharField(db_comment='登记人', max_length=36, verbose_name='登记人')),
                ('from_src', models.CharField(db_comment='来源系统', max_length=36, verbose_name='来源系统')),
                ('empi', models.CharField(blank=True, db_comment='EMPI号', max_length=36, null=True, verbose_name='EMPI号')),
            ],
            options={
                'verbose_name': '患者信息',
                'verbose_name_plural': '患者信息',
                'db_table': 'patient',
            },
        ),
    ]