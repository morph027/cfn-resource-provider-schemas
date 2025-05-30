SCHEMA = {
  "typeName" : "AWS::QuickSight::Topic",
  "description" : "Definition of the AWS::QuickSight::Topic Resource Type.",
  "definitions" : {
    "AggregationFunctionParameters" : {
      "type" : "object",
      "patternProperties" : {
        ".+" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        }
      },
      "additionalProperties" : False
    },
    "AuthorSpecifiedAggregation" : {
      "type" : "string",
      "enum" : [ "COUNT", "DISTINCT_COUNT", "MIN", "MAX", "MEDIAN", "SUM", "AVERAGE", "STDEV", "STDEVP", "VAR", "VARP", "PERCENTILE" ]
    },
    "CategoryFilterFunction" : {
      "type" : "string",
      "enum" : [ "EXACT", "CONTAINS" ]
    },
    "CategoryFilterType" : {
      "type" : "string",
      "enum" : [ "CUSTOM_FILTER", "CUSTOM_FILTER_LIST", "FILTER_LIST" ]
    },
    "CellValueSynonym" : {
      "type" : "object",
      "properties" : {
        "CellValue" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "Synonyms" : {
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        }
      },
      "additionalProperties" : False
    },
    "CollectiveConstant" : {
      "type" : "object",
      "properties" : {
        "ValueList" : {
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        }
      },
      "additionalProperties" : False
    },
    "ColumnDataRole" : {
      "type" : "string",
      "enum" : [ "DIMENSION", "MEASURE" ]
    },
    "ColumnOrderingType" : {
      "type" : "string",
      "enum" : [ "GREATER_IS_BETTER", "LESSER_IS_BETTER", "SPECIFIED" ]
    },
    "ComparativeOrder" : {
      "type" : "object",
      "properties" : {
        "UseOrdering" : {
          "$ref" : "#/definitions/ColumnOrderingType"
        },
        "SpecifedOrder" : {
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        },
        "TreatUndefinedSpecifiedValues" : {
          "$ref" : "#/definitions/UndefinedSpecifiedValueType"
        }
      },
      "additionalProperties" : False
    },
    "ConstantType" : {
      "type" : "string",
      "enum" : [ "SINGULAR", "RANGE", "COLLECTIVE" ]
    },
    "DataAggregation" : {
      "type" : "object",
      "properties" : {
        "DatasetRowDateGranularity" : {
          "$ref" : "#/definitions/TopicTimeGranularity"
        },
        "DefaultDateColumnName" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        }
      },
      "additionalProperties" : False
    },
    "DatasetMetadata" : {
      "type" : "object",
      "properties" : {
        "DatasetArn" : {
          "type" : "string"
        },
        "DatasetName" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "DatasetDescription" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "DataAggregation" : {
          "$ref" : "#/definitions/DataAggregation"
        },
        "Filters" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/TopicFilter"
          }
        },
        "Columns" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/TopicColumn"
          }
        },
        "CalculatedFields" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/TopicCalculatedField"
          }
        },
        "NamedEntities" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/TopicNamedEntity"
          }
        }
      },
      "required" : [ "DatasetArn" ],
      "additionalProperties" : False
    },
    "DefaultAggregation" : {
      "type" : "string",
      "enum" : [ "SUM", "MAX", "MIN", "COUNT", "DISTINCT_COUNT", "AVERAGE", "MEDIAN", "STDEV", "STDEVP", "VAR", "VARP" ]
    },
    "DefaultFormatting" : {
      "type" : "object",
      "properties" : {
        "DisplayFormat" : {
          "$ref" : "#/definitions/DisplayFormat"
        },
        "DisplayFormatOptions" : {
          "$ref" : "#/definitions/DisplayFormatOptions"
        }
      },
      "additionalProperties" : False
    },
    "DisplayFormat" : {
      "type" : "string",
      "enum" : [ "AUTO", "PERCENT", "CURRENCY", "NUMBER", "DATE", "STRING" ]
    },
    "DisplayFormatOptions" : {
      "type" : "object",
      "properties" : {
        "UseBlankCellFormat" : {
          "type" : "boolean",
          "default" : False
        },
        "BlankCellFormat" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "DateFormat" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "DecimalSeparator" : {
          "$ref" : "#/definitions/TopicNumericSeparatorSymbol"
        },
        "GroupingSeparator" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "UseGrouping" : {
          "type" : "boolean",
          "default" : False
        },
        "FractionDigits" : {
          "type" : "number",
          "default" : 0
        },
        "Prefix" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "Suffix" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "UnitScaler" : {
          "$ref" : "#/definitions/NumberScale"
        },
        "NegativeFormat" : {
          "$ref" : "#/definitions/NegativeFormat"
        },
        "CurrencySymbol" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        }
      },
      "additionalProperties" : False
    },
    "FilterClass" : {
      "type" : "string",
      "enum" : [ "ENFORCED_VALUE_FILTER", "CONDITIONAL_VALUE_FILTER", "NAMED_VALUE_FILTER" ]
    },
    "NamedEntityAggType" : {
      "type" : "string",
      "enum" : [ "SUM", "MIN", "MAX", "COUNT", "AVERAGE", "DISTINCT_COUNT", "STDEV", "STDEVP", "VAR", "VARP", "PERCENTILE", "MEDIAN", "CUSTOM" ]
    },
    "NamedEntityDefinition" : {
      "type" : "object",
      "properties" : {
        "FieldName" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "PropertyName" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "PropertyRole" : {
          "$ref" : "#/definitions/PropertyRole"
        },
        "PropertyUsage" : {
          "$ref" : "#/definitions/PropertyUsage"
        },
        "Metric" : {
          "$ref" : "#/definitions/NamedEntityDefinitionMetric"
        }
      },
      "additionalProperties" : False
    },
    "NamedEntityDefinitionMetric" : {
      "type" : "object",
      "properties" : {
        "Aggregation" : {
          "$ref" : "#/definitions/NamedEntityAggType"
        },
        "AggregationFunctionParameters" : {
          "$ref" : "#/definitions/AggregationFunctionParameters"
        }
      },
      "additionalProperties" : False
    },
    "NamedFilterAggType" : {
      "type" : "string",
      "enum" : [ "NO_AGGREGATION", "SUM", "AVERAGE", "COUNT", "DISTINCT_COUNT", "MAX", "MEDIAN", "MIN", "STDEV", "STDEVP", "VAR", "VARP" ]
    },
    "NamedFilterType" : {
      "type" : "string",
      "enum" : [ "CATEGORY_FILTER", "NUMERIC_EQUALITY_FILTER", "NUMERIC_RANGE_FILTER", "DATE_RANGE_FILTER", "RELATIVE_DATE_FILTER" ]
    },
    "NegativeFormat" : {
      "type" : "object",
      "properties" : {
        "Prefix" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "Suffix" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        }
      },
      "additionalProperties" : False
    },
    "NumberScale" : {
      "type" : "string",
      "enum" : [ "NONE", "AUTO", "THOUSANDS", "MILLIONS", "BILLIONS", "TRILLIONS", "LAKHS", "CRORES" ]
    },
    "PropertyRole" : {
      "type" : "string",
      "enum" : [ "PRIMARY", "ID" ]
    },
    "PropertyUsage" : {
      "type" : "string",
      "enum" : [ "INHERIT", "DIMENSION", "MEASURE" ]
    },
    "RangeConstant" : {
      "type" : "object",
      "properties" : {
        "Minimum" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "Maximum" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        }
      },
      "additionalProperties" : False
    },
    "SemanticEntityType" : {
      "type" : "object",
      "properties" : {
        "TypeName" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "SubTypeName" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "TypeParameters" : {
          "$ref" : "#/definitions/TypeParameters"
        }
      },
      "additionalProperties" : False
    },
    "SemanticType" : {
      "type" : "object",
      "properties" : {
        "TypeName" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "SubTypeName" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "TypeParameters" : {
          "$ref" : "#/definitions/TypeParameters"
        },
        "TruthyCellValue" : {
          "type" : "string"
        },
        "TruthyCellValueSynonyms" : {
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        },
        "FalseyCellValue" : {
          "type" : "string"
        },
        "FalseyCellValueSynonyms" : {
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        }
      },
      "additionalProperties" : False
    },
    "TopicCalculatedField" : {
      "type" : "object",
      "properties" : {
        "CalculatedFieldName" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "CalculatedFieldDescription" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "Expression" : {
          "type" : "string",
          "maxLength" : 4096,
          "minLength" : 1
        },
        "CalculatedFieldSynonyms" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "maxLength" : 256,
            "minLength" : 0
          }
        },
        "IsIncludedInTopic" : {
          "type" : "boolean",
          "default" : False
        },
        "DisableIndexing" : {
          "type" : "boolean"
        },
        "ColumnDataRole" : {
          "$ref" : "#/definitions/ColumnDataRole"
        },
        "TimeGranularity" : {
          "$ref" : "#/definitions/TopicTimeGranularity"
        },
        "DefaultFormatting" : {
          "$ref" : "#/definitions/DefaultFormatting"
        },
        "Aggregation" : {
          "$ref" : "#/definitions/DefaultAggregation"
        },
        "ComparativeOrder" : {
          "$ref" : "#/definitions/ComparativeOrder"
        },
        "SemanticType" : {
          "$ref" : "#/definitions/SemanticType"
        },
        "AllowedAggregations" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/AuthorSpecifiedAggregation"
          }
        },
        "NotAllowedAggregations" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/AuthorSpecifiedAggregation"
          }
        },
        "NeverAggregateInFilter" : {
          "type" : "boolean",
          "default" : False
        },
        "CellValueSynonyms" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/CellValueSynonym"
          }
        },
        "NonAdditive" : {
          "type" : "boolean",
          "default" : False
        }
      },
      "required" : [ "CalculatedFieldName", "Expression" ],
      "additionalProperties" : False
    },
    "TopicCategoryFilter" : {
      "type" : "object",
      "properties" : {
        "CategoryFilterFunction" : {
          "$ref" : "#/definitions/CategoryFilterFunction"
        },
        "CategoryFilterType" : {
          "$ref" : "#/definitions/CategoryFilterType"
        },
        "Constant" : {
          "$ref" : "#/definitions/TopicCategoryFilterConstant"
        },
        "Inverse" : {
          "type" : "boolean",
          "default" : False
        }
      },
      "additionalProperties" : False
    },
    "TopicCategoryFilterConstant" : {
      "type" : "object",
      "properties" : {
        "ConstantType" : {
          "$ref" : "#/definitions/ConstantType"
        },
        "SingularConstant" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "CollectiveConstant" : {
          "$ref" : "#/definitions/CollectiveConstant"
        }
      },
      "additionalProperties" : False
    },
    "TopicColumn" : {
      "type" : "object",
      "properties" : {
        "ColumnName" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "ColumnFriendlyName" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "ColumnDescription" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "ColumnSynonyms" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "maxLength" : 256,
            "minLength" : 0
          }
        },
        "ColumnDataRole" : {
          "$ref" : "#/definitions/ColumnDataRole"
        },
        "Aggregation" : {
          "$ref" : "#/definitions/DefaultAggregation"
        },
        "IsIncludedInTopic" : {
          "type" : "boolean",
          "default" : False
        },
        "DisableIndexing" : {
          "type" : "boolean"
        },
        "ComparativeOrder" : {
          "$ref" : "#/definitions/ComparativeOrder"
        },
        "SemanticType" : {
          "$ref" : "#/definitions/SemanticType"
        },
        "TimeGranularity" : {
          "$ref" : "#/definitions/TopicTimeGranularity"
        },
        "AllowedAggregations" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/AuthorSpecifiedAggregation"
          }
        },
        "NotAllowedAggregations" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/AuthorSpecifiedAggregation"
          }
        },
        "DefaultFormatting" : {
          "$ref" : "#/definitions/DefaultFormatting"
        },
        "NeverAggregateInFilter" : {
          "type" : "boolean",
          "default" : False
        },
        "CellValueSynonyms" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/CellValueSynonym"
          }
        },
        "NonAdditive" : {
          "type" : "boolean",
          "default" : False
        }
      },
      "required" : [ "ColumnName" ],
      "additionalProperties" : False
    },
    "TopicConfigOptions" : {
      "type" : "object",
      "description" : "Model for configuration of a Topic",
      "properties" : {
        "QBusinessInsightsEnabled" : {
          "type" : "boolean"
        }
      },
      "additionalProperties" : False
    },
    "TopicDateRangeFilter" : {
      "type" : "object",
      "properties" : {
        "Inclusive" : {
          "type" : "boolean",
          "default" : False
        },
        "Constant" : {
          "$ref" : "#/definitions/TopicRangeFilterConstant"
        }
      },
      "additionalProperties" : False
    },
    "TopicDetails" : {
      "type" : "object",
      "properties" : {
        "Name" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1
        },
        "Description" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "UserExperienceVersion" : {
          "$ref" : "#/definitions/TopicUserExperienceVersion"
        },
        "DataSets" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/DatasetMetadata"
          }
        },
        "ConfigOptions" : {
          "$ref" : "#/definitions/TopicConfigOptions"
        }
      },
      "additionalProperties" : False
    },
    "TopicFilter" : {
      "type" : "object",
      "properties" : {
        "FilterDescription" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "FilterClass" : {
          "$ref" : "#/definitions/FilterClass"
        },
        "FilterName" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "FilterSynonyms" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "maxLength" : 256,
            "minLength" : 0
          }
        },
        "OperandFieldName" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "FilterType" : {
          "$ref" : "#/definitions/NamedFilterType"
        },
        "CategoryFilter" : {
          "$ref" : "#/definitions/TopicCategoryFilter"
        },
        "NumericEqualityFilter" : {
          "$ref" : "#/definitions/TopicNumericEqualityFilter"
        },
        "NumericRangeFilter" : {
          "$ref" : "#/definitions/TopicNumericRangeFilter"
        },
        "DateRangeFilter" : {
          "$ref" : "#/definitions/TopicDateRangeFilter"
        },
        "RelativeDateFilter" : {
          "$ref" : "#/definitions/TopicRelativeDateFilter"
        }
      },
      "required" : [ "FilterName", "OperandFieldName" ],
      "additionalProperties" : False
    },
    "TopicNamedEntity" : {
      "type" : "object",
      "properties" : {
        "EntityName" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "EntityDescription" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        },
        "EntitySynonyms" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "maxLength" : 256,
            "minLength" : 0
          }
        },
        "SemanticEntityType" : {
          "$ref" : "#/definitions/SemanticEntityType"
        },
        "Definition" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/NamedEntityDefinition"
          }
        }
      },
      "required" : [ "EntityName" ],
      "additionalProperties" : False
    },
    "TopicNumericEqualityFilter" : {
      "type" : "object",
      "properties" : {
        "Constant" : {
          "$ref" : "#/definitions/TopicSingularFilterConstant"
        },
        "Aggregation" : {
          "$ref" : "#/definitions/NamedFilterAggType"
        }
      },
      "additionalProperties" : False
    },
    "TopicNumericRangeFilter" : {
      "type" : "object",
      "properties" : {
        "Inclusive" : {
          "type" : "boolean",
          "default" : False
        },
        "Constant" : {
          "$ref" : "#/definitions/TopicRangeFilterConstant"
        },
        "Aggregation" : {
          "$ref" : "#/definitions/NamedFilterAggType"
        }
      },
      "additionalProperties" : False
    },
    "TopicNumericSeparatorSymbol" : {
      "type" : "string",
      "enum" : [ "COMMA", "DOT" ]
    },
    "TopicRangeFilterConstant" : {
      "type" : "object",
      "properties" : {
        "ConstantType" : {
          "$ref" : "#/definitions/ConstantType"
        },
        "RangeConstant" : {
          "$ref" : "#/definitions/RangeConstant"
        }
      },
      "additionalProperties" : False
    },
    "TopicRelativeDateFilter" : {
      "type" : "object",
      "properties" : {
        "TimeGranularity" : {
          "$ref" : "#/definitions/TopicTimeGranularity"
        },
        "RelativeDateFilterFunction" : {
          "$ref" : "#/definitions/TopicRelativeDateFilterFunction"
        },
        "Constant" : {
          "$ref" : "#/definitions/TopicSingularFilterConstant"
        }
      },
      "additionalProperties" : False
    },
    "TopicRelativeDateFilterFunction" : {
      "type" : "string",
      "enum" : [ "PREVIOUS", "THIS", "LAST", "NEXT", "NOW" ]
    },
    "TopicSingularFilterConstant" : {
      "type" : "object",
      "properties" : {
        "ConstantType" : {
          "$ref" : "#/definitions/ConstantType"
        },
        "SingularConstant" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        }
      },
      "additionalProperties" : False
    },
    "TopicTimeGranularity" : {
      "type" : "string",
      "enum" : [ "SECOND", "MINUTE", "HOUR", "DAY", "WEEK", "MONTH", "QUARTER", "YEAR" ]
    },
    "TopicUserExperienceVersion" : {
      "type" : "string",
      "enum" : [ "LEGACY", "NEW_READER_EXPERIENCE" ]
    },
    "TypeParameters" : {
      "type" : "object",
      "patternProperties" : {
        ".+" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        }
      },
      "additionalProperties" : False
    },
    "UndefinedSpecifiedValueType" : {
      "type" : "string",
      "enum" : [ "LEAST", "MOST" ]
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string"
    },
    "AwsAccountId" : {
      "type" : "string",
      "maxLength" : 12,
      "minLength" : 12,
      "pattern" : "^[0-9]{12}$"
    },
    "ConfigOptions" : {
      "$ref" : "#/definitions/TopicConfigOptions"
    },
    "DataSets" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/DatasetMetadata"
      }
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 256,
      "minLength" : 0
    },
    "FolderArns" : {
      "type" : "array",
      "items" : {
        "type" : "string"
      },
      "maxItems" : 20,
      "minItems" : 0
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 128,
      "minLength" : 1
    },
    "TopicId" : {
      "type" : "string",
      "maxLength" : 256,
      "minLength" : 0,
      "pattern" : "^[A-Za-z0-9-_.\\\\+]*$"
    },
    "UserExperienceVersion" : {
      "$ref" : "#/definitions/TopicUserExperienceVersion"
    }
  },
  "readOnlyProperties" : [ "/properties/Arn" ],
  "writeOnlyProperties" : [ "/properties/FolderArns" ],
  "createOnlyProperties" : [ "/properties/AwsAccountId", "/properties/FolderArns", "/properties/TopicId" ],
  "primaryIdentifier" : [ "/properties/AwsAccountId", "/properties/TopicId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "quicksight:CreateTopic", "quicksight:PassDataSet", "quicksight:DescribeTopicRefresh" ]
    },
    "read" : {
      "permissions" : [ "quicksight:DescribeTopic" ]
    },
    "update" : {
      "permissions" : [ "quicksight:UpdateTopic", "quicksight:PassDataSet", "quicksight:DescribeTopicRefresh" ]
    },
    "delete" : {
      "permissions" : [ "quicksight:DeleteTopic" ]
    },
    "list" : {
      "permissions" : [ "quicksight:ListTopics" ]
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  }
}