SCHEMA = {
  "typeName" : "AWS::Forecast::Dataset",
  "description" : "Resource Type Definition for AWS::Forecast::Dataset",
  "sourceUrl" : "https://github.com/junlinzw/aws-cloudformation-resource-providers-forecast",
  "taggable" : False,
  "definitions" : {
    "Attributes" : {
      "type" : "array",
      "insertionOrder" : True,
      "items" : {
        "type" : "object",
        "additionalProperties" : False,
        "properties" : {
          "AttributeName" : {
            "description" : "Name of the dataset field",
            "type" : "string",
            "pattern" : "^[a-zA-Z][a-zA-Z0-9_]*"
          },
          "AttributeType" : {
            "description" : "Data type of the field",
            "type" : "string",
            "enum" : [ "string", "integer", "float", "timestamp", "geolocation" ]
          }
        }
      },
      "minItems" : 1,
      "maxItems" : 100
    },
    "KmsKeyArn" : {
      "description" : "KMS key used to encrypt the Dataset data",
      "type" : "string",
      "maxLength" : 256,
      "pattern" : "arn:aws[-a-z]*:kms:.*:key/.*"
    },
    "RoleArn" : {
      "description" : "The ARN of the IAM role that Amazon Forecast can assume to access the AWS KMS key.",
      "type" : "string",
      "maxLength" : 256,
      "pattern" : "^[a-zA-Z0-9\\-\\_\\.\\/\\:]+$"
    },
    "Key" : {
      "type" : "string",
      "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
      "minLength" : 1,
      "maxLength" : 128
    },
    "Value" : {
      "type" : "string",
      "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
      "minLength" : 0,
      "maxLength" : 256
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "maxLength" : 256,
      "pattern" : "^[a-zA-Z0-9\\-\\_\\.\\/\\:]+$"
    },
    "DatasetName" : {
      "description" : "A name for the dataset",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 63,
      "pattern" : "^[a-zA-Z][a-zA-Z0-9_]*"
    },
    "DatasetType" : {
      "description" : "The dataset type",
      "type" : "string",
      "enum" : [ "TARGET_TIME_SERIES", "RELATED_TIME_SERIES", "ITEM_METADATA" ]
    },
    "DataFrequency" : {
      "description" : "Frequency of data collection. This parameter is required for RELATED_TIME_SERIES",
      "type" : "string",
      "pattern" : "^Y|M|W|D|H|30min|15min|10min|5min|1min$"
    },
    "Domain" : {
      "description" : "The domain associated with the dataset",
      "type" : "string",
      "enum" : [ "RETAIL", "CUSTOM", "INVENTORY_PLANNING", "EC2_CAPACITY", "WORK_FORCE", "WEB_TRAFFIC", "METRICS" ]
    },
    "EncryptionConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "KmsKeyArn" : {
          "$ref" : "#/definitions/KmsKeyArn"
        },
        "RoleArn" : {
          "$ref" : "#/definitions/RoleArn"
        }
      }
    },
    "Schema" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Attributes" : {
          "$ref" : "#/definitions/Attributes"
        }
      }
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : True,
      "items" : {
        "description" : "A key-value pair to associate with a resource.",
        "type" : "object",
        "properties" : {
          "Key" : {
            "$ref" : "#/definitions/Key"
          },
          "Value" : {
            "$ref" : "#/definitions/Value"
          }
        },
        "required" : [ "Key", "Value" ],
        "additionalProperties" : False
      },
      "minItems" : 0,
      "maxItems" : 200
    }
  },
  "additionalProperties" : False,
  "required" : [ "DatasetName", "DatasetType", "Domain", "Schema" ],
  "createOnlyProperties" : [ "/properties/DatasetName" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "forecast:CreateDataset" ]
    },
    "read" : {
      "permissions" : [ "forecast:DescribeDataset" ]
    },
    "delete" : {
      "permissions" : [ "forecast:DeleteDataset" ]
    },
    "list" : {
      "permissions" : [ "forecast:ListDatasets" ]
    }
  }
}