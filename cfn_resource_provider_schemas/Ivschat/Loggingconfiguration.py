SCHEMA = {
  "typeName" : "AWS::IVSChat::LoggingConfiguration",
  "description" : "Resource type definition for AWS::IVSChat::LoggingConfiguration.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ivschat.git",
  "definitions" : {
    "DestinationConfiguration" : {
      "description" : "Destination configuration for IVS Chat logging.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CloudWatchLogs" : {
          "$ref" : "#/definitions/CloudWatchLogsDestinationConfiguration"
        },
        "Firehose" : {
          "$ref" : "#/definitions/FirehoseDestinationConfiguration"
        },
        "S3" : {
          "$ref" : "#/definitions/S3DestinationConfiguration"
        }
      },
      "required" : [ ]
    },
    "CloudWatchLogsDestinationConfiguration" : {
      "description" : "CloudWatch destination configuration for IVS Chat logging.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "LogGroupName" : {
          "description" : "Name of the Amazon CloudWatch Logs log group where chat activity will be logged.",
          "type" : "string",
          "pattern" : "^[\\.\\-_/#A-Za-z0-9]+$",
          "minLength" : 1,
          "maxLength" : 512
        }
      },
      "required" : [ "LogGroupName" ]
    },
    "FirehoseDestinationConfiguration" : {
      "description" : "Kinesis Firehose destination configuration for IVS Chat logging.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DeliveryStreamName" : {
          "description" : "Name of the Amazon Kinesis Firehose delivery stream where chat activity will be logged.",
          "type" : "string",
          "pattern" : "^[a-zA-Z0-9_.-]+$",
          "minLength" : 1,
          "maxLength" : 64
        }
      },
      "required" : [ "DeliveryStreamName" ]
    },
    "S3DestinationConfiguration" : {
      "description" : "S3 destination configuration for IVS Chat logging.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "BucketName" : {
          "description" : "Name of the Amazon S3 bucket where chat activity will be logged.",
          "type" : "string",
          "pattern" : "^[a-z0-9-.]+$",
          "minLength" : 3,
          "maxLength" : 63
        }
      },
      "required" : [ "BucketName" ]
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
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
      "required" : [ "Key", "Value" ]
    }
  },
  "properties" : {
    "Arn" : {
      "description" : "LoggingConfiguration ARN is automatically generated on creation and assigned as the unique identifier.",
      "type" : "string",
      "pattern" : "^arn:aws:ivschat:[a-z0-9-]+:[0-9]+:logging-configuration/[a-zA-Z0-9-]+$",
      "minLength" : 1,
      "maxLength" : 128
    },
    "Id" : {
      "description" : "The system-generated ID of the logging configuration.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9]+$",
      "minLength" : 12,
      "maxLength" : 12
    },
    "DestinationConfiguration" : {
      "$ref" : "#/definitions/DestinationConfiguration"
    },
    "Name" : {
      "description" : "The name of the logging configuration. The value does not need to be unique.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9-_]*$",
      "minLength" : 0,
      "maxLength" : 128
    },
    "State" : {
      "description" : "The state of the logging configuration. When the state is ACTIVE, the configuration is ready to log chat content.",
      "type" : "string",
      "enum" : [ "CREATING", "CREATE_FAILED", "DELETING", "DELETE_FAILED", "UPDATING", "UPDATING_FAILED", "ACTIVE" ]
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ivschat:TagResource", "ivschat:UntagResource", "ivschat:ListTagsForResource" ]
  },
  "required" : [ "DestinationConfiguration" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Id", "/properties/State" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ivschat:CreateLoggingConfiguration", "ivschat:GetLoggingConfiguration", "logs:CreateLogDelivery", "logs:PutResourcePolicy", "logs:DescribeResourcePolicies", "logs:DescribeLogGroups", "s3:PutBucketPolicy", "s3:GetBucketPolicy", "iam:CreateServiceLinkedRole", "firehose:TagDeliveryStream", "ivschat:TagResource" ]
    },
    "read" : {
      "permissions" : [ "ivschat:GetLoggingConfiguration", "ivschat:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "ivschat:UpdateLoggingConfiguration", "ivschat:GetLoggingConfiguration", "ivschat:TagResource", "ivschat:UntagResource", "ivschat:ListTagsForResource", "logs:CreateLogDelivery", "logs:GetLogDelivery", "logs:UpdateLogDelivery", "logs:DeleteLogDelivery", "logs:ListLogDeliveries", "logs:PutResourcePolicy", "logs:DescribeResourcePolicies", "logs:DescribeLogGroups", "s3:PutBucketPolicy", "s3:GetBucketPolicy", "iam:CreateServiceLinkedRole", "firehose:TagDeliveryStream" ]
    },
    "delete" : {
      "permissions" : [ "ivschat:DeleteLoggingConfiguration", "ivschat:GetLoggingConfiguration", "logs:DeleteLogDelivery", "logs:ListLogDeliveries", "ivschat:UntagResource", "logs:GetLogDelivery" ]
    },
    "list" : {
      "permissions" : [ "ivschat:ListLoggingConfigurations", "ivschat:ListTagsForResource" ]
    }
  }
}