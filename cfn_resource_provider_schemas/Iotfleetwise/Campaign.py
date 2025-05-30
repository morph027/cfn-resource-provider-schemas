SCHEMA = {
  "typeName" : "AWS::IoTFleetWise::Campaign",
  "description" : "Definition of AWS::IoTFleetWise::Campaign Resource Type",
  "definitions" : {
    "Compression" : {
      "type" : "string",
      "enum" : [ "OFF", "SNAPPY" ],
      "default" : "OFF"
    },
    "DataDestinationConfig" : {
      "oneOf" : [ {
        "additionalProperties" : False,
        "type" : "object",
        "title" : "S3Config",
        "properties" : {
          "S3Config" : {
            "$ref" : "#/definitions/S3Config"
          }
        },
        "required" : [ "S3Config" ]
      }, {
        "additionalProperties" : False,
        "type" : "object",
        "title" : "TimestreamConfig",
        "properties" : {
          "TimestreamConfig" : {
            "$ref" : "#/definitions/TimestreamConfig"
          }
        },
        "required" : [ "TimestreamConfig" ]
      }, {
        "type" : "object",
        "title" : "MqttTopicConfig",
        "properties" : {
          "MqttTopicConfig" : {
            "$ref" : "#/definitions/MqttTopicConfig"
          }
        },
        "required" : [ "MqttTopicConfig" ],
        "additionalProperties" : False
      } ]
    },
    "S3Config" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "BucketArn" : {
          "maxLength" : 100,
          "type" : "string",
          "pattern" : "^arn:(aws[a-zA-Z0-9-]*):s3:::.+$",
          "minLength" : 16
        },
        "DataFormat" : {
          "$ref" : "#/definitions/DataFormat"
        },
        "StorageCompressionFormat" : {
          "$ref" : "#/definitions/StorageCompressionFormat"
        },
        "Prefix" : {
          "maxLength" : 512,
          "type" : "string",
          "pattern" : "^[a-zA-Z0-9-_:./!*'()]+$",
          "minLength" : 1
        }
      },
      "required" : [ "BucketArn" ]
    },
    "TimestreamConfig" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "TimestreamTableArn" : {
          "maxLength" : 2048,
          "type" : "string",
          "pattern" : "^arn:(aws[a-zA-Z0-9-]*):timestream:[a-zA-Z0-9-]+:[0-9]{12}:database\\/[a-zA-Z0-9_.-]+\\/table\\/[a-zA-Z0-9_.-]+$",
          "minLength" : 20
        },
        "ExecutionRoleArn" : {
          "maxLength" : 2048,
          "type" : "string",
          "pattern" : "^arn:(aws[a-zA-Z0-9-]*):iam::(\\d{12})?:(role((\\u002F)|(\\u002F[\\u0021-\\u007F]+\\u002F))[\\w+=,.@-]+)$",
          "minLength" : 20
        }
      },
      "required" : [ "TimestreamTableArn", "ExecutionRoleArn" ]
    },
    "MqttTopicConfig" : {
      "type" : "object",
      "properties" : {
        "MqttTopicArn" : {
          "type" : "string",
          "maxLength" : 2048,
          "minLength" : 20,
          "pattern" : "^arn:.*"
        },
        "ExecutionRoleArn" : {
          "type" : "string",
          "maxLength" : 2048,
          "minLength" : 20,
          "pattern" : "^arn:(aws[a-zA-Z0-9-]*):iam::(\\d{12})?:(role((\\u002F)|(\\u002F[\\u0021-\\u007F]+\\u002F))[\\w+=,.@-]+)$"
        }
      },
      "required" : [ "ExecutionRoleArn", "MqttTopicArn" ],
      "additionalProperties" : False
    },
    "UpdateCampaignAction" : {
      "type" : "string",
      "enum" : [ "APPROVE", "SUSPEND", "RESUME", "UPDATE" ]
    },
    "CampaignStatus" : {
      "type" : "string",
      "enum" : [ "CREATING", "WAITING_FOR_APPROVAL", "RUNNING", "SUSPENDED" ]
    },
    "ConditionBasedSignalFetchConfig" : {
      "type" : "object",
      "properties" : {
        "ConditionExpression" : {
          "type" : "string",
          "maxLength" : 2048,
          "minLength" : 1
        },
        "TriggerMode" : {
          "$ref" : "#/definitions/TriggerMode"
        }
      },
      "required" : [ "ConditionExpression", "TriggerMode" ],
      "additionalProperties" : False
    },
    "DiagnosticsMode" : {
      "type" : "string",
      "enum" : [ "OFF", "SEND_ACTIVE_DTCS" ],
      "default" : "OFF"
    },
    "SignalInformation" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "MaxSampleCount" : {
          "maximum" : 4294967295,
          "type" : "number",
          "minimum" : 1
        },
        "Name" : {
          "minLength" : 1,
          "pattern" : "^[\\w|*|-]+(\\.[\\w|*|-]+)*$",
          "type" : "string",
          "maxLength" : 150
        },
        "MinimumSamplingIntervalMs" : {
          "maximum" : 4294967295,
          "type" : "number",
          "minimum" : 0
        },
        "DataPartitionId" : {
          "$ref" : "#/definitions/DataPartitionId"
        }
      },
      "required" : [ "Name" ]
    },
    "SignalFetchConfig" : {
      "oneOf" : [ {
        "type" : "object",
        "title" : "TimeBased",
        "properties" : {
          "TimeBased" : {
            "$ref" : "#/definitions/TimeBasedSignalFetchConfig"
          }
        },
        "required" : [ "TimeBased" ],
        "additionalProperties" : False
      }, {
        "type" : "object",
        "title" : "ConditionBased",
        "properties" : {
          "ConditionBased" : {
            "$ref" : "#/definitions/ConditionBasedSignalFetchConfig"
          }
        },
        "required" : [ "ConditionBased" ],
        "additionalProperties" : False
      } ]
    },
    "SignalFetchInformation" : {
      "type" : "object",
      "properties" : {
        "FullyQualifiedName" : {
          "type" : "string",
          "maxLength" : 150,
          "minLength" : 1,
          "pattern" : "^[a-zA-Z0-9_.]+$"
        },
        "SignalFetchConfig" : {
          "$ref" : "#/definitions/SignalFetchConfig"
        },
        "ConditionLanguageVersion" : {
          "type" : "number",
          "maximum" : 1,
          "minimum" : 1
        },
        "Actions" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "maxLength" : 2048,
            "minLength" : 1
          },
          "maxItems" : 5,
          "minItems" : 1
        }
      },
      "required" : [ "Actions", "FullyQualifiedName", "SignalFetchConfig" ],
      "additionalProperties" : False
    },
    "TimeBasedCollectionScheme" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "PeriodMs" : {
          "maximum" : 86400000,
          "type" : "number",
          "minimum" : 10000
        }
      },
      "required" : [ "PeriodMs" ]
    },
    "TimeBasedSignalFetchConfig" : {
      "type" : "object",
      "properties" : {
        "ExecutionFrequencyMs" : {
          "type" : "number",
          "minimum" : 1
        }
      },
      "required" : [ "ExecutionFrequencyMs" ],
      "additionalProperties" : False
    },
    "SpoolingMode" : {
      "type" : "string",
      "enum" : [ "OFF", "TO_DISK" ],
      "default" : "OFF"
    },
    "TriggerMode" : {
      "type" : "string",
      "enum" : [ "ALWAYS", "RISING_EDGE" ]
    },
    "DataFormat" : {
      "type" : "string",
      "enum" : [ "JSON", "PARQUET" ]
    },
    "StorageCompressionFormat" : {
      "type" : "string",
      "enum" : [ "NONE", "GZIP" ]
    },
    "CollectionScheme" : {
      "oneOf" : [ {
        "additionalProperties" : False,
        "type" : "object",
        "title" : "TimeBasedCollectionScheme",
        "properties" : {
          "TimeBasedCollectionScheme" : {
            "$ref" : "#/definitions/TimeBasedCollectionScheme"
          }
        },
        "required" : [ "TimeBasedCollectionScheme" ]
      }, {
        "additionalProperties" : False,
        "type" : "object",
        "title" : "ConditionBasedCollectionScheme",
        "properties" : {
          "ConditionBasedCollectionScheme" : {
            "$ref" : "#/definitions/ConditionBasedCollectionScheme"
          }
        },
        "required" : [ "ConditionBasedCollectionScheme" ]
      } ]
    },
    "ConditionBasedCollectionScheme" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "MinimumTriggerIntervalMs" : {
          "maximum" : 4294967295,
          "type" : "number",
          "minimum" : 0
        },
        "Expression" : {
          "$ref" : "#/definitions/EventExpression"
        },
        "TriggerMode" : {
          "$ref" : "#/definitions/TriggerMode"
        },
        "ConditionLanguageVersion" : {
          "$ref" : "#/definitions/LanguageVersion"
        }
      },
      "required" : [ "Expression" ]
    },
    "EventExpression" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 2048
    },
    "LanguageVersion" : {
      "type" : "integer",
      "minimum" : 1
    },
    "DataPartition" : {
      "type" : "object",
      "properties" : {
        "Id" : {
          "$ref" : "#/definitions/DataPartitionId"
        },
        "StorageOptions" : {
          "$ref" : "#/definitions/DataPartitionStorageOptions"
        },
        "UploadOptions" : {
          "$ref" : "#/definitions/DataPartitionUploadOptions"
        }
      },
      "required" : [ "Id", "StorageOptions" ],
      "additionalProperties" : False
    },
    "DataPartitionStorageOptions" : {
      "type" : "object",
      "properties" : {
        "MaximumSize" : {
          "$ref" : "#/definitions/StorageMaximumSize"
        },
        "MinimumTimeToLive" : {
          "$ref" : "#/definitions/StorageMinimumTimeToLive"
        },
        "StorageLocation" : {
          "$ref" : "#/definitions/StorageLocation"
        }
      },
      "required" : [ "MaximumSize", "MinimumTimeToLive", "StorageLocation" ],
      "additionalProperties" : False
    },
    "StorageLocation" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 4096
    },
    "StorageMaximumSize" : {
      "type" : "object",
      "properties" : {
        "Unit" : {
          "$ref" : "#/definitions/StorageMaximumSizeUnit"
        },
        "Value" : {
          "$ref" : "#/definitions/StorageMaximumSizeValue"
        }
      },
      "required" : [ "Unit", "Value" ],
      "additionalProperties" : False
    },
    "StorageMaximumSizeUnit" : {
      "type" : "string",
      "enum" : [ "MB", "GB", "TB" ]
    },
    "StorageMaximumSizeValue" : {
      "type" : "integer",
      "minimum" : 1,
      "maximum" : 1073741824
    },
    "StorageMinimumTimeToLive" : {
      "type" : "object",
      "properties" : {
        "Unit" : {
          "$ref" : "#/definitions/StorageMinimumTimeToLiveUnit"
        },
        "Value" : {
          "$ref" : "#/definitions/StorageMinimumTimeToLiveValue"
        }
      },
      "required" : [ "Unit", "Value" ],
      "additionalProperties" : False
    },
    "StorageMinimumTimeToLiveUnit" : {
      "type" : "string",
      "enum" : [ "HOURS", "DAYS", "WEEKS" ]
    },
    "StorageMinimumTimeToLiveValue" : {
      "type" : "integer",
      "minimum" : 1,
      "maximum" : 10000
    },
    "DataPartitionUploadOptions" : {
      "type" : "object",
      "properties" : {
        "Expression" : {
          "$ref" : "#/definitions/EventExpression"
        },
        "ConditionLanguageVersion" : {
          "$ref" : "#/definitions/LanguageVersion"
        }
      },
      "required" : [ "Expression" ],
      "additionalProperties" : False
    },
    "DataPartitionId" : {
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9]+$",
      "minLength" : 1,
      "maxLength" : 128
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "TimePeriod" : {
      "type" : "object",
      "properties" : {
        "Unit" : {
          "$ref" : "#/definitions/TimeUnit"
        },
        "Value" : {
          "type" : "number",
          "minimum" : 1
        }
      },
      "required" : [ "Unit", "Value" ],
      "additionalProperties" : False
    },
    "TimeUnit" : {
      "type" : "string",
      "enum" : [ "MILLISECOND", "SECOND", "MINUTE", "HOUR" ]
    }
  },
  "properties" : {
    "Status" : {
      "$ref" : "#/definitions/CampaignStatus"
    },
    "Action" : {
      "$ref" : "#/definitions/UpdateCampaignAction"
    },
    "CreationTime" : {
      "type" : "string",
      "format" : "date-time"
    },
    "Compression" : {
      "$ref" : "#/definitions/Compression"
    },
    "Description" : {
      "minLength" : 1,
      "pattern" : "^[^\\u0000-\\u001F\\u007F]+$",
      "type" : "string",
      "maxLength" : 2048
    },
    "Priority" : {
      "type" : "integer",
      "minimum" : 0,
      "default" : 0
    },
    "SignalsToCollect" : {
      "minItems" : 0,
      "maxItems" : 1000,
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/SignalInformation"
      }
    },
    "SignalsToFetch" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/SignalFetchInformation"
      },
      "maxItems" : 10,
      "minItems" : 0
    },
    "DataDestinationConfigs" : {
      "minItems" : 1,
      "maxItems" : 1,
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/DataDestinationConfig"
      }
    },
    "StartTime" : {
      "format" : "date-time",
      "type" : "string",
      "default" : "0"
    },
    "Name" : {
      "minLength" : 1,
      "pattern" : "^[a-zA-Z\\d\\-_:]+$",
      "type" : "string",
      "maxLength" : 100
    },
    "ExpiryTime" : {
      "format" : "date-time",
      "type" : "string",
      "default" : "253402214400"
    },
    "LastModificationTime" : {
      "type" : "string",
      "format" : "date-time"
    },
    "SpoolingMode" : {
      "$ref" : "#/definitions/SpoolingMode"
    },
    "SignalCatalogArn" : {
      "type" : "string"
    },
    "PostTriggerCollectionDuration" : {
      "maximum" : 4294967295,
      "type" : "number",
      "minimum" : 0,
      "default" : 0
    },
    "DataExtraDimensions" : {
      "minItems" : 0,
      "maxItems" : 5,
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "minLength" : 1,
        "pattern" : "^[a-zA-Z0-9_.]+$",
        "type" : "string",
        "maxLength" : 150
      }
    },
    "DiagnosticsMode" : {
      "$ref" : "#/definitions/DiagnosticsMode"
    },
    "TargetArn" : {
      "type" : "string"
    },
    "Arn" : {
      "type" : "string"
    },
    "CollectionScheme" : {
      "$ref" : "#/definitions/CollectionScheme"
    },
    "DataPartitions" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/DataPartition"
      },
      "insertionOrder" : True,
      "uniqueItems" : True,
      "maxItems" : 20,
      "minItems" : 0
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "insertionOrder" : False,
      "uniqueItems" : True,
      "maxItems" : 50,
      "minItems" : 0
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "iotfleetwise:UntagResource", "iotfleetwise:TagResource", "iotfleetwise:ListTagsForResource" ]
  },
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Status", "/properties/CreationTime", "/properties/LastModificationTime" ],
  "writeOnlyProperties" : [ "/properties/Action" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/TargetArn", "/properties/SignalCatalogArn", "/properties/PostTriggerCollectionDuration", "/properties/DiagnosticsMode", "/properties/SpoolingMode", "/properties/CollectionScheme", "/properties/Priority", "/properties/Compression", "/properties/StartTime", "/properties/ExpiryTime", "/properties/DataPartitions" ],
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/Name" ],
  "required" : [ "Name", "CollectionScheme", "SignalCatalogArn", "TargetArn" ],
  "handlers" : {
    "read" : {
      "permissions" : [ "iotfleetwise:GetCampaign", "iotfleetwise:ListTagsForResource" ]
    },
    "create" : {
      "permissions" : [ "iotfleetwise:CreateCampaign", "iotfleetwise:GetCampaign", "iotfleetwise:ListTagsForResource", "iotfleetwise:TagResource", "iam:PassRole", "timestream:DescribeEndpoints", "timestream:DescribeTable" ]
    },
    "update" : {
      "permissions" : [ "iotfleetwise:GetCampaign", "iotfleetwise:ListTagsForResource", "iotfleetwise:UpdateCampaign", "iotfleetwise:TagResource", "iotfleetwise:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "iotfleetwise:ListCampaigns", "iotfleetwise:GetCampaign" ]
    },
    "delete" : {
      "permissions" : [ "iotfleetwise:DeleteCampaign", "iotfleetwise:GetCampaign" ]
    }
  }
}