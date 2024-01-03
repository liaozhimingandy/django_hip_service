from import_export import resources
from import_export.fields import Field

from esb_standard.models import DictMain, Dict, DataSet, DataElement


class DictMainModelResource(resources.ModelResource):
    value = Field(attribute='value', column_name=DictMain.value.field.verbose_name)
    comment = Field(attribute='comment', column_name=DictMain.comment.field.verbose_name)

    class Meta:
        model = DictMain
        # fields内的模型字段会被导入导出, exclude内的会被排除在外，如果都不写，默认为模型中的全部字段都要包含。
        fields = ("value", "comment")
        # export_order（自定义） 选项设置导出字段的显式顺序，没在这里规定的就按默认顺序排在后面（不能只写一个）(导入不用管顺序)
        export_order = ("value",)
        # 下面规定联合主键，决定是update还是create，可以避免重复导入相同的记录
        import_id_fields = ('value',)


class DictModelResource(resources.ModelResource):
    value = Field(attribute='value', column_name=Dict.value.field.verbose_name)
    comment = Field(attribute='comment', column_name=Dict.comment.field.verbose_name)
    value_dict = Field(attribute='value_dict', column_name=Dict.value_dict.field.verbose_name)

    class Meta:
        model = Dict
        # fields内的模型字段会被导入导出, exclude内的会被排除在外，如果都不写，默认为模型中的全部字段都要包含。
        fields = ("value", "comment", "value_dict")
        # export_order（自定义） 选项设置导出字段的显式顺序，没在这里规定的就按默认顺序排在后面（不能只写一个）(导入不用管顺序)
        export_order = ("value",)
        # 下面规定联合主键，决定是update还是create，可以避免重复导入相同的记录
        import_id_fields = ('value',)


class DataSetModelResource(resources.ModelResource):
    value = Field(attribute='value', column_name=DataSet.value.field.verbose_name)
    comment = Field(attribute='comment', column_name=DataSet.comment.field.verbose_name)

    class Meta:
        model = DataSet
        # fields内的模型字段会被导入导出, exclude内的会被排除在外，如果都不写，默认为模型中的全部字段都要包含。
        fields = ("value", "comment")
        # export_order（自定义） 选项设置导出字段的显式顺序，没在这里规定的就按默认顺序排在后面（不能只写一个）(导入不用管顺序)
        export_order = ("value",)
        # 下面规定联合主键，决定是update还是create，可以避免重复导入相同的记录
        import_id_fields = ('value',)


class DataElementModelResource(resources.ModelResource):
    hd_code = Field(attribute='value', column_name=DataElement.hd_code.field.verbose_name)
    de_code = Field(attribute='de_code', column_name=DataElement.de_code.field.verbose_name)
    de_en_code = Field(attribute='de_en_code', column_name=DataElement.de_en_code.field.verbose_name)
    de_name = Field(attribute='de_name', column_name=DataElement.de_name.field.verbose_name)
    definition = Field(attribute='definition', column_name=DataElement.definition.field.verbose_name)
    data_type = Field(attribute='data_type', column_name=DataElement.data_type.field.verbose_name)
    expression = Field(attribute='expression', column_name=DataElement.expression.field.verbose_name)
    allowable_value = Field(attribute='allowable_value', column_name=DataElement.allowable_value.field.verbose_name)
    length = Field(attribute='length', column_name=DataElement.length.field.verbose_name)
    data_set = Field(attribute='data_set', column_name=DataElement.data_set.field.verbose_name)

    class Meta:
        model = DataElement
        # fields内的模型字段会被导入导出, exclude内的会被排除在外，如果都不写，默认为模型中的全部字段都要包含。
        fields = ("hd_code", "de_code", "de_en_code", "de_name", "definition", "data_type", "expression",
                  "allowable_value", "length", "data_set")
        # export_order（自定义） 选项设置导出字段的显式顺序，没在这里规定的就按默认顺序排在后面（不能只写一个）(导入不用管顺序)
        export_order = ("hd_code", "de_code", "de_en_code",)
        # 下面规定联合主键，决定是update还是create，可以避免重复导入相同的记录
        import_id_fields = ('de_en_code',)
