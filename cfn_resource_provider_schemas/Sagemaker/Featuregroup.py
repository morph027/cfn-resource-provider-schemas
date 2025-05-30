SCHEMA = {
  "typeName" : "AWS::SageMaker::FeatureGroup",
  "description" : "Resource Type definition for AWS::SageMaker::FeatureGroup",
  "additionalProperties" : False,
  "properties" : {
    "FeatureGroupName" : {
      "type" : "string",
      "description" : "The Name of the FeatureGroup.",
      "minLength" : 1,
      "maxLength" : 64,
      "pattern" : "^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}"
    },
    "RecordIdentifierFeatureName" : {
      "type" : "string",
      "description" : "The Record Identifier Feature Name.",
      "minLength" : 1,
      "maxLength" : 64,
      "pattern" : "^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}"
    },
    "EventTimeFeatureName" : {
      "type" : "string",
      "description" : "The Event Time Feature Name.",
      "minLength" : 1,
      "maxLength" : 64,
      "pattern" : "^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}"
    },
    "FeatureDefinitions" : {
      "type" : "array",
      "description" : "An Array of Feature Definition",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "minItems" : 1,
      "maxItems" : 2500,
      "items" : {
        "$ref" : "#/definitions/FeatureDefinition"
      }
    },
    "OnlineStoreConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SecurityConfig" : {
          "$ref" : "#/definitions/OnlineStoreSecurityConfig"
        },
        "EnableOnlineStore" : {
          "type" : "boolean"
        },
        "StorageType" : {
          "$ref" : "#/definitions/StorageType"
        },
        "TtlDuration" : {
          "$ref" : "#/definitions/TtlDuration"
        }
      }
    },
    "OfflineStoreConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "S3StorageConfig" : {
          "$ref" : "#/definitions/S3StorageConfig"
        },
        "DisableGlueTableCreation" : {
          "type" : "boolean"
        },
        "DataCatalogConfig" : {
          "$ref" : "#/definitions/DataCatalogConfig"
        },
        "TableFormat" : {
          "$ref" : "#/definitions/TableFormat"
        }
      },
      "required" : [ "S3StorageConfig" ]
    },
    "ThroughputConfig" : {
      "$ref" : "#/definitions/ThroughputConfig"
    },
    "RoleArn" : {
      "type" : "string",
      "description" : "Role Arn",
      "minLength" : 20,
      "maxLength" : 2048,
      "pattern" : "^arn:aws[a-z\\-]*:iam::\\d{12}:role/?[a-zA-Z_0-9+=,.@\\-_/]+$"
    },
    "Description" : {
      "type" : "string",
      "description" : "Description about the FeatureGroup.",
      "maxLength" : 128
    },
    "CreationTime" : {
      "description" : "A timestamp of FeatureGroup creation time.",
      "type" : "string"
    },
    "FeatureGroupStatus" : {
      "description" : "The status of the feature group.",
      "type" : "string"
    },
    "Tags" : {
      "type" : "array",
      "description" : "An array of key-value pair to apply to this resource.",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "maxItems" : 50,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "definitions" : {
    "FeatureDefinition" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "FeatureName" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 64,
          "pattern" : "^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}"
        },
        "FeatureType" : {
          "type" : "string",
          "enum" : [ "Integral", "Fractional", "String" ]
        }
      },
      "required" : [ "FeatureName", "FeatureType" ]
    },
    "KmsKeyId" : {
      "type" : "string",
      "maxLength" : 2048
    },
    "StorageType" : {
      "type" : "string",
      "enum" : [ "Standard", "InMemory" ]
    },
    "TtlDuration" : {
      "type" : "object",
      "description" : "TTL configuration of the feature group",
      "additionalProperties" : False,
      "properties" : {
        "Unit" : {
          "$ref" : "#/definitions/Unit"
        },
        "Value" : {
          "$ref" : "#/definitions/Value"
        }
      }
    },
    "Unit" : {
      "type" : "string",
      "description" : "Unit of ttl configuration",
      "enum" : [ "Seconds", "Minutes", "Hours", "Days", "Weeks" ]
    },
    "Value" : {
      "type" : "integer",
      "description" : "Value of ttl configuration"
    },
    "OnlineStoreSecurityConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "KmsKeyId" : {
          "$ref" : "#/definitions/KmsKeyId"
        }
      }
    },
    "S3StorageConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "S3Uri" : {
          "type" : "string",
          "maxLength" : 1024,
          "pattern" : "^(https|s3)://([^/]+)/?(.*)$"
        },
        "KmsKeyId" : {
          "$ref" : "#/definitions/KmsKeyId"
        }
      },
      "required" : [ "S3Uri" ]
    },
    "DataCatalogConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "TableName" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 255,
          "pattern" : "[\\u0020-\\uD7FF\\uE000-\\uFFFD\\uD800\\uDC00-\\uDBFF\\uDFFF\t]*"
        },
        "Catalog" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 255,
          "pattern" : "[\\u0020-\\uD7FF\\uE000-\\uFFFD\\uD800\\uDC00-\\uDBFF\\uDFFF\t]*"
        },
        "Database" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 255,
          "pattern" : "[\\u0020-\\uD7FF\\uE000-\\uFFFD\\uD800\\uDC00-\\uDBFF\\uDFFF\t]*"
        }
      },
      "required" : [ "TableName", "Catalog", "Database" ]
    },
    "TableFormat" : {
      "type" : "string",
      "description" : "Format for the offline store feature group. Iceberg is the optimal format for feature groups shared between offline and online stores.",
      "enum" : [ "Iceberg", "Glue" ]
    },
    "ThroughputMode" : {
      "type" : "string",
      "description" : "Throughput mode configuration of the feature group",
      "enum" : [ "OnDemand", "Provisioned" ]
    },
    "ThroughputConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ThroughputMode" : {
          "$ref" : "#/definitions/ThroughputMode"
        },
        "ProvisionedReadCapacityUnits" : {
          "type" : "integer",
          "description" : "For provisioned feature groups with online store enabled, this indicates the read throughput you are billed for and can consume without throttling."
        },
        "ProvisionedWriteCapacityUnits" : {
          "type" : "integer",
          "description" : "For provisioned feature groups, this indicates the write throughput you are billed for and can consume without throttling."
        }
      },
      "required" : [ "ThroughputMode" ]
    },
    "Tag" : {
      "type" : "object",
      "description" : "A key-value pair to associate with a resource.",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "type" : "string"
        },
        "Key" : {
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "required" : [ "FeatureGroupName", "RecordIdentifierFeatureName", "EventTimeFeatureName", "FeatureDefinitions" ],
  "createOnlyProperties" : [ "/properties/FeatureGroupName", "/properties/RecordIdentifierFeatureName", "/properties/EventTimeFeatureName", "/properties/OnlineStoreConfig/SecurityConfig", "/properties/OnlineStoreConfig/EnableOnlineStore", "/properties/OnlineStoreConfig/StorageType", "/properties/OfflineStoreConfig", "/properties/RoleArn", "/properties/Description", "/properties/Tags" ],
  "primaryIdentifier" : [ "/properties/FeatureGroupName" ],
  "readOnlyProperties" : [ "/properties/CreationTime", "/properties/FeatureGroupStatus" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:PassRole", "kms:CreateGrant", "kms:DescribeKey", "glue:CreateTable", "glue:GetTable", "glue:CreateDatabase", "glue:GetDatabase", "sagemaker:CreateFeatureGroup", "sagemaker:DescribeFeatureGroup", "sagemaker:AddTags", "sagemaker:ListTags" ]
    },
    "update" : {
      "permissions" : [ "sagemaker:UpdateFeatureGroup", "sagemaker:DescribeFeatureGroup", "sagemaker:AddTags", "sagemaker:ListTags", "sagemaker:DeleteTags" ]
    },
    "read" : {
      "permissions" : [ "sagemaker:DescribeFeatureGroup", "sagemaker:ListTags" ]
    },
    "delete" : {
      "permissions" : [ "sagemaker:DeleteFeatureGroup", "sagemaker:DescribeFeatureGroup" ]
    },
    "list" : {
      "permissions" : [ "sagemaker:ListFeatureGroups" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "sagemaker:AddTags", "sagemaker:ListTags", "sagemaker:DeleteTags" ]
  }
}