SCHEMA = {
  "typeName" : "AWS::S3::StorageLens",
  "description" : "The AWS::S3::StorageLens resource is an Amazon S3 resource type that you can use to create Storage Lens configurations.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-s3-storagelens",
  "definitions" : {
    "Id" : {
      "description" : "The ID that identifies the Amazon S3 Storage Lens configuration.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 64,
      "pattern" : "^[a-zA-Z0-9\\-_.]+$"
    },
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) of the specified resource.",
      "type" : "string"
    },
    "BucketsAndRegions" : {
      "description" : "S3 buckets and Regions to include/exclude in the Amazon S3 Storage Lens configuration.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Buckets" : {
          "type" : "array",
          "insertionOrder" : False,
          "uniqueItems" : True,
          "items" : {
            "$ref" : "#/definitions/Arn"
          }
        },
        "Regions" : {
          "type" : "array",
          "insertionOrder" : False,
          "uniqueItems" : True,
          "items" : {
            "type" : "string",
            "description" : "An AWS Region."
          }
        }
      }
    },
    "AwsOrg" : {
      "description" : "The AWS Organizations ARN to use in the Amazon S3 Storage Lens configuration.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Arn" : {
          "$ref" : "#/definitions/Arn"
        }
      },
      "required" : [ "Arn" ]
    },
    "ActivityMetrics" : {
      "description" : "Enables activity metrics.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "IsEnabled" : {
          "description" : "Specifies whether activity metrics are enabled or disabled.",
          "type" : "boolean"
        }
      }
    },
    "AdvancedCostOptimizationMetrics" : {
      "description" : "Enables advanced cost optimization metrics.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "IsEnabled" : {
          "description" : "Specifies whether advanced cost optimization metrics are enabled or disabled.",
          "type" : "boolean"
        }
      }
    },
    "AdvancedDataProtectionMetrics" : {
      "description" : "Enables advanced data protection metrics.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "IsEnabled" : {
          "description" : "Specifies whether advanced data protection metrics are enabled or disabled.",
          "type" : "boolean"
        }
      }
    },
    "DetailedStatusCodesMetrics" : {
      "description" : "Enables detailed status codes metrics.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "IsEnabled" : {
          "description" : "Specifies whether detailed status codes metrics are enabled or disabled.",
          "type" : "boolean"
        }
      }
    },
    "SelectionCriteria" : {
      "description" : "Selection criteria for prefix-level metrics.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MaxDepth" : {
          "description" : "Max depth of prefixes of S3 key that Amazon S3 Storage Lens will analyze.",
          "type" : "integer"
        },
        "Delimiter" : {
          "description" : "Delimiter to divide S3 key into hierarchy of prefixes.",
          "type" : "string"
        },
        "MinStorageBytesPercentage" : {
          "description" : "The minimum storage bytes threshold for the prefixes to be included in the analysis.",
          "type" : "number"
        }
      }
    },
    "PrefixLevelStorageMetrics" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "IsEnabled" : {
          "description" : "Specifies whether prefix-level storage metrics are enabled or disabled.",
          "type" : "boolean"
        },
        "SelectionCriteria" : {
          "$ref" : "#/definitions/SelectionCriteria"
        }
      }
    },
    "PrefixLevel" : {
      "description" : "Prefix-level metrics configurations.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "StorageMetrics" : {
          "$ref" : "#/definitions/PrefixLevelStorageMetrics"
        }
      },
      "required" : [ "StorageMetrics" ]
    },
    "BucketLevel" : {
      "description" : "Bucket-level metrics configurations.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ActivityMetrics" : {
          "$ref" : "#/definitions/ActivityMetrics"
        },
        "AdvancedCostOptimizationMetrics" : {
          "$ref" : "#/definitions/AdvancedCostOptimizationMetrics"
        },
        "AdvancedDataProtectionMetrics" : {
          "$ref" : "#/definitions/AdvancedDataProtectionMetrics"
        },
        "DetailedStatusCodesMetrics" : {
          "$ref" : "#/definitions/DetailedStatusCodesMetrics"
        },
        "PrefixLevel" : {
          "$ref" : "#/definitions/PrefixLevel"
        }
      }
    },
    "StorageLensGroupArn" : {
      "description" : "The ARN for the Amazon S3 Storage Lens Group configuration.",
      "type" : "string"
    },
    "StorageLensGroupSelectionCriteria" : {
      "description" : "Selection criteria for Storage Lens Group level metrics",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Include" : {
          "type" : "array",
          "insertionOrder" : False,
          "uniqueItems" : True,
          "items" : {
            "$ref" : "#/definitions/StorageLensGroupArn"
          }
        },
        "Exclude" : {
          "type" : "array",
          "insertionOrder" : False,
          "uniqueItems" : True,
          "items" : {
            "$ref" : "#/definitions/StorageLensGroupArn"
          }
        }
      }
    },
    "StorageLensGroupLevel" : {
      "description" : "Specifies the details of Amazon S3 Storage Lens Group configuration.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "StorageLensGroupSelectionCriteria" : {
          "$ref" : "#/definitions/StorageLensGroupSelectionCriteria"
        }
      }
    },
    "AccountLevel" : {
      "description" : "Account-level metrics configurations.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ActivityMetrics" : {
          "$ref" : "#/definitions/ActivityMetrics"
        },
        "AdvancedCostOptimizationMetrics" : {
          "$ref" : "#/definitions/AdvancedCostOptimizationMetrics"
        },
        "AdvancedDataProtectionMetrics" : {
          "$ref" : "#/definitions/AdvancedDataProtectionMetrics"
        },
        "DetailedStatusCodesMetrics" : {
          "$ref" : "#/definitions/DetailedStatusCodesMetrics"
        },
        "BucketLevel" : {
          "$ref" : "#/definitions/BucketLevel"
        },
        "StorageLensGroupLevel" : {
          "$ref" : "#/definitions/StorageLensGroupLevel"
        }
      },
      "required" : [ "BucketLevel" ]
    },
    "SSEKMS" : {
      "description" : "AWS KMS server-side encryption.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "KeyId" : {
          "description" : "The ARN of the KMS key to use for encryption.",
          "type" : "string"
        }
      },
      "required" : [ "KeyId" ]
    },
    "Encryption" : {
      "description" : "Configures the server-side encryption for Amazon S3 Storage Lens report files with either S3-managed keys (SSE-S3) or KMS-managed keys (SSE-KMS).",
      "type" : "object",
      "oneOf" : [ {
        "additionalProperties" : False,
        "properties" : {
          "SSES3" : {
            "description" : "S3 default server-side encryption.",
            "type" : "object",
            "additionalProperties" : False
          }
        },
        "required" : [ "SSES3" ]
      }, {
        "additionalProperties" : False,
        "properties" : {
          "SSEKMS" : {
            "$ref" : "#/definitions/SSEKMS"
          }
        },
        "required" : [ "SSEKMS" ]
      } ]
    },
    "S3BucketDestination" : {
      "description" : "S3 bucket destination settings for the Amazon S3 Storage Lens metrics export.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "OutputSchemaVersion" : {
          "description" : "The version of the output schema to use when exporting Amazon S3 Storage Lens metrics.",
          "type" : "string",
          "enum" : [ "V_1" ]
        },
        "Format" : {
          "description" : "Specifies the file format to use when exporting Amazon S3 Storage Lens metrics export.",
          "type" : "string",
          "enum" : [ "CSV", "Parquet" ]
        },
        "AccountId" : {
          "description" : "The AWS account ID that owns the destination S3 bucket.",
          "type" : "string"
        },
        "Arn" : {
          "description" : "The ARN of the bucket to which Amazon S3 Storage Lens exports will be placed.",
          "type" : "string",
          "relationshipRef" : {
            "typeName" : "AWS::S3::Bucket",
            "propertyPath" : "/properties/Arn"
          }
        },
        "Prefix" : {
          "description" : "The prefix to use for Amazon S3 Storage Lens export.",
          "type" : "string"
        },
        "Encryption" : {
          "$ref" : "#/definitions/Encryption"
        }
      },
      "required" : [ "OutputSchemaVersion", "Format", "AccountId", "Arn" ]
    },
    "CloudWatchMetrics" : {
      "description" : "CloudWatch metrics settings for the Amazon S3 Storage Lens metrics export.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "IsEnabled" : {
          "description" : "Specifies whether CloudWatch metrics are enabled or disabled.",
          "type" : "boolean"
        }
      },
      "required" : [ "IsEnabled" ]
    },
    "DataExport" : {
      "description" : "Specifies how Amazon S3 Storage Lens metrics should be exported.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "S3BucketDestination" : {
          "$ref" : "#/definitions/S3BucketDestination"
        },
        "CloudWatchMetrics" : {
          "$ref" : "#/definitions/CloudWatchMetrics"
        }
      }
    },
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 127,
          "pattern" : "^(?!aws:.*)[a-zA-Z0-9\\s\\_\\.\\/\\=\\+\\-\\@\\:]+$"
        },
        "Value" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 255,
          "pattern" : "^(?!aws:.*)[a-zA-Z0-9\\s\\_\\.\\/\\=\\+\\-\\@\\:]+$"
        }
      },
      "required" : [ "Key", "Value" ]
    },
    "StorageLensConfiguration" : {
      "description" : "Specifies the details of Amazon S3 Storage Lens configuration.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Id" : {
          "$ref" : "#/definitions/Id"
        },
        "Include" : {
          "$ref" : "#/definitions/BucketsAndRegions"
        },
        "Exclude" : {
          "$ref" : "#/definitions/BucketsAndRegions"
        },
        "AwsOrg" : {
          "$ref" : "#/definitions/AwsOrg"
        },
        "AccountLevel" : {
          "$ref" : "#/definitions/AccountLevel"
        },
        "DataExport" : {
          "$ref" : "#/definitions/DataExport"
        },
        "IsEnabled" : {
          "description" : "Specifies whether the Amazon S3 Storage Lens configuration is enabled or disabled.",
          "type" : "boolean"
        },
        "StorageLensArn" : {
          "description" : "The ARN for the Amazon S3 Storage Lens configuration.",
          "type" : "string"
        }
      },
      "required" : [ "Id", "AccountLevel", "IsEnabled" ]
    }
  },
  "properties" : {
    "StorageLensConfiguration" : {
      "$ref" : "#/definitions/StorageLensConfiguration"
    },
    "Tags" : {
      "description" : "A set of tags (key-value pairs) for this Amazon S3 Storage Lens configuration.",
      "type" : "array",
      "insertionOrder" : False,
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "maxItems" : 50
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags"
  },
  "required" : [ "StorageLensConfiguration" ],
  "readOnlyProperties" : [ "/properties/StorageLensConfiguration/StorageLensArn" ],
  "createOnlyProperties" : [ "/properties/StorageLensConfiguration/Id" ],
  "primaryIdentifier" : [ "/properties/StorageLensConfiguration/Id" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "s3:PutStorageLensConfiguration", "s3:PutStorageLensConfigurationTagging", "s3:GetStorageLensConfiguration", "s3:GetStorageLensConfigurationTagging", "organizations:DescribeOrganization", "organizations:ListAccounts", "organizations:ListAWSServiceAccessForOrganization", "organizations:ListDelegatedAdministrators", "iam:CreateServiceLinkedRole" ]
    },
    "read" : {
      "permissions" : [ "s3:GetStorageLensConfiguration", "s3:GetStorageLensConfigurationTagging" ]
    },
    "update" : {
      "permissions" : [ "s3:PutStorageLensConfiguration", "s3:PutStorageLensConfigurationTagging", "s3:GetStorageLensConfiguration", "s3:GetStorageLensConfigurationTagging", "organizations:DescribeOrganization", "organizations:ListAccounts", "organizations:ListAWSServiceAccessForOrganization", "organizations:ListDelegatedAdministrators", "iam:CreateServiceLinkedRole" ]
    },
    "delete" : {
      "permissions" : [ "s3:DeleteStorageLensConfiguration", "s3:DeleteStorageLensConfigurationTagging" ]
    },
    "list" : {
      "permissions" : [ "s3:ListStorageLensConfigurations" ]
    }
  }
}