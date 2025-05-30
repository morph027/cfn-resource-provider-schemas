SCHEMA = {
  "typeName" : "AWS::LookoutMetrics::AnomalyDetector",
  "description" : "An Amazon Lookout for Metrics Detector",
  "sourceUrl" : "https://docs.aws.amazon.com/lookoutmetrics/latest/dev/lookoutmetrics-welcome.html",
  "definitions" : {
    "Arn" : {
      "type" : "string",
      "maxLength" : 256,
      "pattern" : "arn:([a-z\\d-]+):.*:.*:.*:.+"
    },
    "ColumnName" : {
      "description" : "Name of a column in the data.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 63,
      "pattern" : "^[a-zA-Z0-9][a-zA-Z0-9\\-_]*"
    },
    "Charset" : {
      "type" : "string",
      "maxLength" : 63,
      "pattern" : "^[a-zA-Z0-9][a-zA-Z0-9\\-_]*"
    },
    "CsvFormatDescriptor" : {
      "type" : "object",
      "properties" : {
        "FileCompression" : {
          "type" : "string",
          "enum" : [ "NONE", "GZIP" ]
        },
        "Charset" : {
          "$ref" : "#/definitions/Charset"
        },
        "Delimiter" : {
          "type" : "string",
          "maxLength" : 1,
          "pattern" : "[^\\r\\n]"
        },
        "HeaderList" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/ColumnName"
          }
        },
        "QuoteSymbol" : {
          "type" : "string",
          "maxLength" : 1,
          "pattern" : "[^\\r\\n]|^$"
        },
        "ContainsHeader" : {
          "type" : "boolean"
        }
      },
      "additionalProperties" : False
    },
    "JsonFormatDescriptor" : {
      "type" : "object",
      "properties" : {
        "FileCompression" : {
          "type" : "string",
          "enum" : [ "NONE", "GZIP" ]
        },
        "Charset" : {
          "$ref" : "#/definitions/Charset"
        }
      },
      "additionalProperties" : False
    },
    "FileFormatDescriptor" : {
      "type" : "object",
      "properties" : {
        "CsvFormatDescriptor" : {
          "$ref" : "#/definitions/CsvFormatDescriptor"
        },
        "JsonFormatDescriptor" : {
          "$ref" : "#/definitions/JsonFormatDescriptor"
        }
      },
      "additionalProperties" : False
    },
    "S3SourceConfig" : {
      "type" : "object",
      "properties" : {
        "RoleArn" : {
          "$ref" : "#/definitions/Arn"
        },
        "TemplatedPathList" : {
          "type" : "array",
          "minItems" : 1,
          "maxItems" : 1,
          "items" : {
            "type" : "string",
            "maxLength" : 1024,
            "pattern" : "^s3://[a-zA-Z0-9_\\-\\/ {}=]+$"
          }
        },
        "HistoricalDataPathList" : {
          "type" : "array",
          "minItems" : 1,
          "maxItems" : 1,
          "items" : {
            "type" : "string",
            "maxLength" : 1024,
            "pattern" : "^s3://[a-z0-9].+$"
          }
        },
        "FileFormatDescriptor" : {
          "$ref" : "#/definitions/FileFormatDescriptor"
        }
      },
      "additionalProperties" : False,
      "required" : [ "RoleArn", "FileFormatDescriptor" ]
    },
    "AppFlowConfig" : {
      "type" : "object",
      "properties" : {
        "RoleArn" : {
          "$ref" : "#/definitions/Arn"
        },
        "FlowName" : {
          "type" : "string",
          "maxLength" : 256,
          "pattern" : "[a-zA-Z0-9][\\w!@#.-]+"
        }
      },
      "required" : [ "RoleArn", "FlowName" ],
      "additionalProperties" : False
    },
    "CloudwatchConfig" : {
      "type" : "object",
      "properties" : {
        "RoleArn" : {
          "$ref" : "#/definitions/Arn"
        }
      },
      "required" : [ "RoleArn" ],
      "additionalProperties" : False
    },
    "DatabaseHost" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 253,
      "pattern" : ".*\\S.*"
    },
    "DatabasePort" : {
      "type" : "integer",
      "minimum" : 1,
      "maximum" : 65535
    },
    "TableName" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 100,
      "pattern" : "^[a-zA-Z][a-zA-Z0-9_]*$"
    },
    "SubnetIdList" : {
      "type" : "array",
      "items" : {
        "type" : "string",
        "maxLength" : 255,
        "pattern" : "[\\-0-9a-zA-Z]+"
      }
    },
    "SecurityGroupIdList" : {
      "type" : "array",
      "items" : {
        "type" : "string",
        "minLength" : 1,
        "maxLength" : 255,
        "pattern" : "[-0-9a-zA-Z]+"
      }
    },
    "VpcConfiguration" : {
      "type" : "object",
      "properties" : {
        "SubnetIdList" : {
          "$ref" : "#/definitions/SubnetIdList"
        },
        "SecurityGroupIdList" : {
          "$ref" : "#/definitions/SecurityGroupIdList"
        }
      },
      "required" : [ "SubnetIdList", "SecurityGroupIdList" ],
      "additionalProperties" : False
    },
    "SecretManagerArn" : {
      "type" : "string",
      "maxLength" : 256,
      "pattern" : "arn:([a-z\\d-]+):.*:.*:secret:AmazonLookoutMetrics-.+"
    },
    "RDSSourceConfig" : {
      "type" : "object",
      "properties" : {
        "DBInstanceIdentifier" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 63,
          "pattern" : "^[a-zA-Z](?!.*--)(?!.*-$)[0-9a-zA-Z\\-]*$"
        },
        "DatabaseHost" : {
          "$ref" : "#/definitions/DatabaseHost"
        },
        "DatabasePort" : {
          "$ref" : "#/definitions/DatabasePort"
        },
        "SecretManagerArn" : {
          "$ref" : "#/definitions/SecretManagerArn"
        },
        "DatabaseName" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 64,
          "pattern" : "[a-zA-Z0-9_]+"
        },
        "TableName" : {
          "$ref" : "#/definitions/TableName"
        },
        "RoleArn" : {
          "$ref" : "#/definitions/Arn"
        },
        "VpcConfiguration" : {
          "$ref" : "#/definitions/VpcConfiguration"
        }
      },
      "required" : [ "DBInstanceIdentifier", "DatabaseHost", "DatabasePort", "SecretManagerArn", "DatabaseName", "TableName", "RoleArn", "VpcConfiguration" ],
      "additionalProperties" : False
    },
    "RedshiftSourceConfig" : {
      "type" : "object",
      "properties" : {
        "ClusterIdentifier" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 63,
          "pattern" : "^[a-z](?!.*--)(?!.*-$)[0-9a-z\\-]*$"
        },
        "DatabaseHost" : {
          "$ref" : "#/definitions/DatabaseHost"
        },
        "DatabasePort" : {
          "$ref" : "#/definitions/DatabasePort"
        },
        "SecretManagerArn" : {
          "$ref" : "#/definitions/SecretManagerArn"
        },
        "DatabaseName" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 100,
          "pattern" : "[a-z0-9]+"
        },
        "TableName" : {
          "$ref" : "#/definitions/TableName"
        },
        "RoleArn" : {
          "$ref" : "#/definitions/Arn"
        },
        "VpcConfiguration" : {
          "$ref" : "#/definitions/VpcConfiguration"
        }
      },
      "required" : [ "ClusterIdentifier", "DatabaseHost", "DatabasePort", "SecretManagerArn", "DatabaseName", "TableName", "RoleArn", "VpcConfiguration" ],
      "additionalProperties" : False
    },
    "MetricSource" : {
      "type" : "object",
      "properties" : {
        "S3SourceConfig" : {
          "$ref" : "#/definitions/S3SourceConfig"
        },
        "RDSSourceConfig" : {
          "$ref" : "#/definitions/RDSSourceConfig"
        },
        "RedshiftSourceConfig" : {
          "$ref" : "#/definitions/RedshiftSourceConfig"
        },
        "CloudwatchConfig" : {
          "$ref" : "#/definitions/CloudwatchConfig"
        },
        "AppFlowConfig" : {
          "$ref" : "#/definitions/AppFlowConfig"
        }
      },
      "additionalProperties" : False
    },
    "TimestampColumn" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ColumnName" : {
          "$ref" : "#/definitions/ColumnName"
        },
        "ColumnFormat" : {
          "description" : "A timestamp format for the timestamps in the dataset",
          "type" : "string",
          "maxLength" : 63,
          "pattern" : ".*\\S.*"
        }
      }
    },
    "Metric" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MetricName" : {
          "$ref" : "#/definitions/ColumnName"
        },
        "AggregationFunction" : {
          "description" : "Operator used to aggregate metric values",
          "type" : "string",
          "enum" : [ "AVG", "SUM" ]
        },
        "Namespace" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 255,
          "pattern" : "[^:].*"
        }
      },
      "required" : [ "MetricName", "AggregationFunction" ]
    },
    "MetricSet" : {
      "type" : "object",
      "properties" : {
        "MetricSetName" : {
          "description" : "The name of the MetricSet.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 63,
          "pattern" : "^[a-zA-Z0-9][a-zA-Z0-9\\-_]*"
        },
        "MetricSetDescription" : {
          "description" : "A description for the MetricSet.",
          "type" : "string",
          "maxLength" : 256,
          "pattern" : ".*\\S.*"
        },
        "MetricSource" : {
          "$ref" : "#/definitions/MetricSource"
        },
        "MetricList" : {
          "description" : "Metrics captured by this MetricSet.",
          "type" : "array",
          "insertionOrder" : False,
          "minItems" : 1,
          "items" : {
            "$ref" : "#/definitions/Metric"
          }
        },
        "Offset" : {
          "description" : "Offset, in seconds, between the frequency interval and the time at which the metrics are available.",
          "type" : "integer",
          "minimum" : 0,
          "maximum" : 432000
        },
        "TimestampColumn" : {
          "$ref" : "#/definitions/TimestampColumn"
        },
        "DimensionList" : {
          "description" : "Dimensions for this MetricSet.",
          "type" : "array",
          "insertionOrder" : False,
          "minItems" : 0,
          "items" : {
            "$ref" : "#/definitions/ColumnName"
          }
        },
        "MetricSetFrequency" : {
          "description" : "A frequency period to aggregate the data",
          "type" : "string",
          "enum" : [ "PT5M", "PT10M", "PT1H", "P1D" ]
        },
        "Timezone" : {
          "type" : "string",
          "maxLength" : 60,
          "pattern" : ".*\\S.*"
        }
      },
      "required" : [ "MetricSetName", "MetricList", "MetricSource" ],
      "additionalProperties" : False
    },
    "AnomalyDetectorFrequency" : {
      "description" : "Frequency of anomaly detection",
      "type" : "string",
      "enum" : [ "PT5M", "PT10M", "PT1H", "P1D" ]
    },
    "AnomalyDetectorConfig" : {
      "type" : "object",
      "properties" : {
        "AnomalyDetectorFrequency" : {
          "description" : "Frequency of anomaly detection",
          "$ref" : "#/definitions/AnomalyDetectorFrequency"
        }
      },
      "required" : [ "AnomalyDetectorFrequency" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "$ref" : "#/definitions/Arn"
    },
    "AnomalyDetectorName" : {
      "description" : "Name for the Amazon Lookout for Metrics Anomaly Detector",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 63,
      "pattern" : "^[a-zA-Z0-9][a-zA-Z0-9\\-_]*"
    },
    "AnomalyDetectorDescription" : {
      "description" : "A description for the AnomalyDetector.",
      "type" : "string",
      "maxLength" : 256,
      "pattern" : ".*\\S.*"
    },
    "AnomalyDetectorConfig" : {
      "description" : "Configuration options for the AnomalyDetector",
      "$ref" : "#/definitions/AnomalyDetectorConfig"
    },
    "MetricSetList" : {
      "description" : "List of metric sets for anomaly detection",
      "type" : "array",
      "minItems" : 1,
      "maxItems" : 1,
      "items" : {
        "$ref" : "#/definitions/MetricSet"
      }
    },
    "KmsKeyArn" : {
      "description" : "KMS key used to encrypt the AnomalyDetector data",
      "type" : "string",
      "minLength" : 20,
      "maxLength" : 2048,
      "pattern" : "arn:aws.*:kms:.*:[0-9]{12}:key/.*"
    }
  },
  "additionalProperties" : False,
  "required" : [ "AnomalyDetectorConfig", "MetricSetList" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/AnomalyDetectorName", "/properties/MetricSource" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "lookoutmetrics:CreateAnomalyDetector", "lookoutmetrics:DeleteAnomalyDetector", "lookoutmetrics:CreateMetricSet", "iam:PassRole" ],
      "timeoutInMinutes" : 15
    },
    "read" : {
      "permissions" : [ "lookoutmetrics:DescribeAnomalyDetector", "lookoutmetrics:DescribeMetricSet", "lookoutmetrics:ListMetricSets" ],
      "timeoutInMinutes" : 15
    },
    "update" : {
      "permissions" : [ "lookoutmetrics:UpdateAnomalyDetector", "lookoutmetrics:UpdateMetricSet" ],
      "timeoutInMinutes" : 15
    },
    "delete" : {
      "permissions" : [ "lookoutmetrics:DescribeAnomalyDetector", "lookoutmetrics:DeleteAnomalyDetector" ],
      "timeoutInMinutes" : 15
    },
    "list" : {
      "permissions" : [ "lookoutmetrics:ListAnomalyDetectors" ],
      "timeoutInMinutes" : 15
    }
  }
}