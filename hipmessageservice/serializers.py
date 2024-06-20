#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""=================================================
    @Project: django_hip_service
    @File： serializers.py
    @Author：liaozhimingandy
    @Email: liaozhimingandy@gmail.com
    @Date：2024-03-26 16:17
================================================="""
from rest_framework import serializers

from cdr import models


class HIPServiceSerializer(serializers.Serializer):
    """
    标准交互服务序列化
    """
    list_service = [('PatientInfoRegister', '个人信息注册服务'),
                    ('PatientInfoUpdate', '个人信息更新服务'),
                    ('PatientInfoMerge', '个人信息合并服务'),
                    ('PatientInfoQuery', '个人信息查询服务'),
                    ('OrganizationInfoRegister', '医疗卫生机构（科室）信息注册服务'),
                    ('OrganizationInfoUpdate', '医疗卫生机构（科室）信息更新服务'),
                    ('OrganizationInfoQuery', '医疗卫生机构（科室）信息查询服务'),
                    ('ProviderInfoRegister', '医疗卫生人员信息注册服务'),
                    ('ProviderInfoUpdate', '医疗卫生人员信息更新服务'),
                    ('ProviderInfoQuery', '医疗卫生人员信息查询服务'),
                    ('TerminologyRegister', '术语注册服务'),
                    ('TerminologyUpdate', '术语更新服务'),
                    ('TerminologyQuery', '术语查询服务'),
                    ('DocumentRegister', '电子病历文档注册服务'),
                    ('DocumentAccess', '电子病历文档调阅服务'),
                    ('DocumentRetrieve', '电子病历文档检索服务'),
                    ('EncounterCardInfoAdd', '就诊卡信息新增服务'),
                    ('EncounterCardInfoUpdate', '就诊卡信息更新服务'),
                    ('EncounterCardInfoQuery', '就诊卡信息查询服务'),
                    ('OutPatientInfoAdd', '门诊挂号信息新增服务'),
                    ('OutPatientInfoUpdate', '门诊挂号信息更新服务'),
                    ('OutPatientInfoQuery', '门诊挂号信息查询服务'),
                    ('InPatientInfoAdd', '住院就诊信息登记服务'),
                    ('InPatientInfoUpdate', '住院就诊信息更新服务'),
                    ('InPatientInfoQuery', '住院就诊信息查询服务'),
                    ('TransferInfoAdd', '住院转科信息新增服务'),
                    ('TransferInfoUpdate', '住院转科信息更新服务'),
                    ('TransferInfoQuery', '住院转科信息查询服务'),
                    ('DischargeInfoAdd', '出院登记信息新增服务'),
                    ('DischargeInfoUpdate', '出院登记信息更新服务'),
                    ('DischargeInfoQuery', '出院登记信息查询服务'),
                    ('OrderInfoAdd', '医嘱信息新增服务'),
                    ('OrderInfoUpdate', '医嘱信息更新服务'),
                    ('OrderInfoQuery', '医嘱信息查询服务'),
                    ('ExamAppInfoAdd', '检验申请信息新增服务'),
                    ('ExamAppInfoUpdate', '检验申请信息更新服务'),
                    ('ExamAppInfoQuery', '检验申请信息查询服务'),
                    ('CheckAppInfoAdd', '检查申请信息新增服务'),
                    ('CheckAppInfoUpdate', '检查申请信息更新服务'),
                    ('CheckAppInfoQuery', '检查申请信息查询服务'),
                    ('PathologyAppInfoAdd', '病理申请信息新增服务'),
                    ('PathologyAppInfoUpdate', '病理申请信息更新服务'),
                    ('PathologyAppInfoQuery', '病理申请信息查询服务'),
                    ('BloodTransAppInfoAdd', '输血申请信息新增服务'),
                    ('BloodTransAppInfoUpdate', '输血申请信息更新服务'),
                    ('BloodTransAppInfoQuery', '输血申请信息查询服务'),
                    ('OperationAppInfoAdd', '手术申请信息新增服务'),
                    ('OperationAppInfoUpdate', '手术申请信息更新服务'),
                    ('OperationAppInfoQuery', '手术申请信息查询服务'),
                    ('SourceAndScheduleInfoAdd', '号源排班信息新增服务'),
                    ('SourceAndScheduleInfoUpdate', '号源排班信息更新服务'),
                    ('SourceAndScheduleInfoQuery', '号源排班信息查询服务'),
                    ('OutPatientAppointStatusInfoAdd', '门诊预约状态信息新增服务'),
                    ('OutPatientAppointStatusInfoUpdate', '门诊预约状态信息更新服务'),
                    ('OutPatientAppointStatusInfoQuery', '门诊预约状态信息查询服务'),
                    ('CheckAppointStatusInfoAdd', '检查预约状态信息新增服务'),
                    ('CheckAppointStatusInfoUpdate', '检查预约状态信息更新服务'),
                    ('CheckAppointStatusInfoQuery', '检查预约状态信息查询服务'),
                    ('OrderFillerStatusInfoUpdate', '医嘱执行状态信息更新服务'),
                    ('OrderFillerStatusInfoQuery', '医嘱执行状态信息查询服务'),
                    ('CheckStatusInfoUpdate', '检查状态信息更新服务'),
                    ('CheckStatusInfoQuery', '检查状态信息查询服务'),
                    ('ExamStatusInfoUpdate', '检验状态信息更新服务'),
                    ('ExamStatusInfoQuery', '检验状态信息查询服务'),
                    ('OperationScheduleInfoAdd', '手术排班信息新增服务'),
                    ('OperationScheduleInfoUpdate', '手术排班信息更新服务'),
                    ('OperationScheduleInfoQuery', '手术排班信息查询服务'),
                    ('OperationStatusInfoUpdate', '手术状态信息更新服务'),
                    ('OperationStatusInfoQuery', '手术状态信息查询服务')
                    ]
    service_code = serializers.ChoiceField(list_service, help_text="请选择对应的服务", required=True)
    content = serializers.CharField(help_text="请输入需要校验的内容", required=True)


class HIPCDASerializer(serializers.Serializer):
    """
    标准CDA序列化
    """
    list_cda = [
        ('C0001', '病历概要'),
        ('C0002', '门急诊病历'),
        ('C0003', '急诊留观病历'),
        ('C0004', '西药处方'),
        ('C0005', '中药处方'),
        ('C0006', '检查报告'),
        ('C0007', '检验报告'),
        ('C0008', '治疗记录'),
        ('C0009', '一般手术记录'),
        ('C0010', '麻醉术前访视记录'),
        ('C0011', '麻醉记录'),
        ('C0012', '麻醉术后访视记录'),
        ('C0013', '输血记录'),
        ('C0014', '待产记录'),
        ('C0015', '阴道分娩记录'),
        ('C0016', '剖宫产记录'),
        ('C0017', '一般护理记录'),
        ('C0018', '病重病危护理记录'),
        ('C0019', '手术护理记录'),
        ('C0020', '生命体征测量记录'),
        ('C0021', '出入量记录'),
        ('C0022', '高值耗材使用记录'),
        ('C0023', '入院评估'),
        ('C0024', '护理计划'),
        ('C0025', '出院评估与指导'),
        ('C0026', '手术知情同意书'),
        ('C0027', '麻醉知情同意书'),
        ('C0028', '输血治疗同意书'),
        ('C0029', '特殊检查及特殊治疗同意书'),
        ('C0030', '病危重通知书'),
        ('C0031', '其他知情告知同意书'),
        ('C0032', '住院病案首页'),
        ('C0033', '中医住院病案首页'),
        ('C0034', '入院记录'),
        ('C0035', '24小时内入出院记录'),
        ('C0036', '24小时内入院死亡记录'),
        ('C0037', '首次病程记录'),
        ('C0038', '日常病程记录'),
        ('C0039', '上级医师查房记录'),
        ('C0040', '疑难病例讨论记录'),
        ('C0041', '交接班记录'),
        ('C0042', '转科记录'),
        ('C0043', '阶段小结'),
        ('C0044', '抢救记录'),
        ('C0045', '会诊记录'),
        ('C0046', '术前小结'),
        ('C0047', '术前讨论'),
        ('C0048', '术后首次病程记录'),
        ('C0049', '出院记录'),
        ('C0050', '死亡记录'),
        ('C0051', '死亡病例讨论记录'),
        ('C0052', '住院医嘱'),
        ('C0053', '出院小结')
    ]
    cda_code = serializers.ChoiceField(list_cda, help_text="请选择对应的CDA文档", required=True)
    content = serializers.CharField(help_text="请输入需要校验的文档内容", required=True)


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        exclude = ["id", ]


class ExamReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExamReport
        exclude = ["id", ]


class ExamResultMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExamResultMain
        exclude = ["id", ]


class ExamResultDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExamResultDetail
        exclude = ["id", ]


class ExamResultDetailASTSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExamResultDetailAST
        exclude = ["id", ]


class CheckReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CheckReport
        exclude = ["id", ]

    def validate_extra_infos(self, value):
        if not any((isinstance(value, dict), value is None)):
            raise serializers.ValidationError(f"extra_infos中的值: '{value}'必须是一个字典类型或者null")
        return value


if __name__ == "__main__":
    pass
