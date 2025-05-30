SCHEMA = {
  "typeName" : "AWS::Connect::InstanceStorageConfig",
  "description" : "Resource Type definition for AWS::Connect::InstanceStorageConfig",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-connect",
  "definitions" : {
    "KinesisStreamArn" : {
      "description" : "An ARN is a unique AWS resource identifier.",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z0-9]*:kinesis:[-a-z0-9]*:[0-9]{12}:stream/[-a-zA-Z0-9_.]*$"
    },
    "FirehoseDeliveryStreamArn" : {
      "description" : "An ARN is a unique AWS resource identifier.",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z0-9]*:firehose:[-a-z0-9]*:[0-9]{12}:deliverystream/[-a-zA-Z0-9_.]*$"
    },
    "AssociationId" : {
      "description" : "An associationID is automatically generated when a storage config is associated with an instance",
      "type" : "string",
      "pattern" : "^[-a-z0-9]*$",
      "minLength" : 1,
      "maxLength" : 100
    },
    "InstanceStorageResourceType" : {
      "description" : "Specifies the type of storage resource available for the instance",
      "type" : "string",
      "enum" : [ "CHAT_TRANSCRIPTS", "CALL_RECORDINGS", "SCHEDULED_REPORTS", "MEDIA_STREAMS", "CONTACT_TRACE_RECORDS", "AGENT_EVENTS" ]
    },
    "StorageType" : {
      "description" : "Specifies the storage type to be associated with the instance",
      "type" : "string",
      "enum" : [ "S3", "KINESIS_VIDEO_STREAM", "KINESIS_STREAM", "KINESIS_FIREHOSE" ]
    },
    "BucketName" : {
      "description" : "A name for the S3 Bucket",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 128
    },
    "Hours" : {
      "description" : "Number of hours",
      "type" : "number"
    },
    "Prefix" : {
      "description" : "Prefixes are used to infer logical hierarchy",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 128
    },
    "EncryptionType" : {
      "description" : "Specifies default encryption using AWS KMS-Managed Keys",
      "type" : "string",
      "enum" : [ "KMS" ]
    },
    "KeyId" : {
      "description" : "Specifies the encryption key id",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 128
    },
    "EncryptionConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "EncryptionType" : {
          "$ref" : "#/definitions/EncryptionType"
        },
        "KeyId" : {
          "$ref" : "#/definitions/KeyId"
        }
      },
      "required" : [ "EncryptionType", "KeyId" ]
    },
    "S3Config" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "BucketName" : {
          "$ref" : "#/definitions/BucketName"
        },
        "BucketPrefix" : {
          "$ref" : "#/definitions/Prefix"
        },
        "EncryptionConfig" : {
          "$ref" : "#/definitions/EncryptionConfig"
        }
      },
      "required" : [ "BucketName", "BucketPrefix" ]
    },
    "KinesisVideoStreamConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Prefix" : {
          "$ref" : "#/definitions/Prefix"
        },
        "RetentionPeriodHours" : {
          "$ref" : "#/definitions/Hours"
        },
        "EncryptionConfig" : {
          "$ref" : "#/definitions/EncryptionConfig"
        }
      },
      "required" : [ "Prefix", "RetentionPeriodHours", "EncryptionConfig" ]
    },
    "KinesisStreamConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "StreamArn" : {
          "$ref" : "#/definitions/KinesisStreamArn"
        }
      },
      "required" : [ "StreamArn" ]
    },
    "KinesisFirehoseConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "FirehoseArn" : {
          "$ref" : "#/definitions/FirehoseDeliveryStreamArn"
        }
      },
      "required" : [ "FirehoseArn" ]
    }
  },
  "properties" : {
    "InstanceArn" : {
      "description" : "Connect Instance ID with which the storage config will be associated",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$"
    },
    "ResourceType" : {
      "$ref" : "#/definitions/InstanceStorageResourceType"
    },
    "AssociationId" : {
      "$ref" : "#/definitions/AssociationId"
    },
    "StorageType" : {
      "$ref" : "#/definitions/StorageType"
    },
    "S3Config" : {
      "$ref" : "#/definitions/S3Config"
    },
    "KinesisVideoStreamConfig" : {
      "$ref" : "#/definitions/KinesisVideoStreamConfig"
    },
    "KinesisStreamConfig" : {
      "$ref" : "#/definitions/KinesisStreamConfig"
    },
    "KinesisFirehoseConfig" : {
      "$ref" : "#/definitions/KinesisFirehoseConfig"
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "required" : [ "InstanceArn", "ResourceType", "StorageType" ],
  "additionalProperties" : False,
  "readOnlyProperties" : [ "/properties/AssociationId" ],
  "createOnlyProperties" : [ "/properties/InstanceArn", "/properties/ResourceType" ],
  "primaryIdentifier" : [ "/properties/InstanceArn", "/properties/AssociationId", "/properties/ResourceType" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "connect:AssociateInstanceStorageConfig", "connect:DescribeInstance", "ds:DescribeDirectories", "s3:GetBucketAcl", "s3:GetBucketLocation", "iam:PutRolePolicy", "kinesis:DescribeStream", "kms:DescribeKey", "kms:CreateGrant", "firehose:DescribeDeliveryStream" ]
    },
    "read" : {
      "permissions" : [ "connect:DescribeInstanceStorageConfig", "connect:ListInstanceStorageConfigs", "connect:DescribeInstance", "ds:DescribeDirectories", "s3:GetBucketAcl", "s3:GetBucketLocation" ]
    },
    "update" : {
      "permissions" : [ "connect:UpdateInstanceStorageConfig", "ds:DescribeDirectories", "s3:GetBucketAcl", "s3:GetBucketLocation", "kinesis:DescribeStream", "iam:PutRolePolicy", "kms:DescribeKey", "kms:CreateGrant", "kms:RetireGrant", "firehose:DescribeDeliveryStream" ]
    },
    "delete" : {
      "permissions" : [ "connect:DisassociateInstanceStorageConfig", "connect:DescribeInstance", "s3:GetBucketAcl", "s3:GetBucketLocation", "kms:RetireGrant" ]
    },
    "list" : {
      "permissions" : [ "connect:DescribeInstance", "connect:ListInstanceStorageConfigs", "ds:DescribeDirectories" ]
    }
  }
}