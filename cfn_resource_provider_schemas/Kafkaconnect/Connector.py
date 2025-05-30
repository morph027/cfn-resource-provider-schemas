SCHEMA = {
  "typeName" : "AWS::KafkaConnect::Connector",
  "description" : "Resource Type definition for AWS::KafkaConnect::Connector",
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "kafkaconnect:ListTagsForResource", "kafkaconnect:UntagResource", "kafkaconnect:TagResource", "firehose:TagDeliveryStream" ]
  },
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-kafkaconnect.git",
  "properties" : {
    "Capacity" : {
      "$ref" : "#/definitions/Capacity"
    },
    "ConnectorArn" : {
      "description" : "Amazon Resource Name for the created Connector.",
      "type" : "string",
      "pattern" : "arn:(aws|aws-us-gov|aws-cn):kafkaconnect:.*"
    },
    "ConnectorConfiguration" : {
      "description" : "The configuration for the connector.",
      "type" : "object",
      "additionalProperties" : False,
      "patternProperties" : {
        ".*" : {
          "type" : "string"
        }
      }
    },
    "ConnectorDescription" : {
      "description" : "A summary description of the connector.",
      "type" : "string",
      "maxLength" : 1024
    },
    "ConnectorName" : {
      "description" : "The name of the connector.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 128
    },
    "KafkaCluster" : {
      "$ref" : "#/definitions/KafkaCluster"
    },
    "KafkaClusterClientAuthentication" : {
      "$ref" : "#/definitions/KafkaClusterClientAuthentication"
    },
    "KafkaClusterEncryptionInTransit" : {
      "$ref" : "#/definitions/KafkaClusterEncryptionInTransit"
    },
    "KafkaConnectVersion" : {
      "description" : "The version of Kafka Connect. It has to be compatible with both the Kafka cluster's version and the plugins.",
      "type" : "string"
    },
    "LogDelivery" : {
      "$ref" : "#/definitions/LogDelivery"
    },
    "Plugins" : {
      "description" : "List of plugins to use with the connector.",
      "type" : "array",
      "uniqueItems" : True,
      "minItems" : 1,
      "items" : {
        "$ref" : "#/definitions/Plugin"
      },
      "insertionOrder" : False
    },
    "ServiceExecutionRoleArn" : {
      "description" : "The Amazon Resource Name (ARN) of the IAM role used by the connector to access Amazon S3 objects and other external resources.",
      "type" : "string",
      "pattern" : "arn:(aws|aws-us-gov|aws-cn):iam:.*"
    },
    "Tags" : {
      "description" : "A collection of tags associated with a resource",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "WorkerConfiguration" : {
      "$ref" : "#/definitions/WorkerConfiguration"
    }
  },
  "definitions" : {
    "ApacheKafkaCluster" : {
      "description" : "Details of how to connect to an Apache Kafka cluster.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "BootstrapServers" : {
          "description" : "The bootstrap servers string of the Apache Kafka cluster.",
          "type" : "string"
        },
        "Vpc" : {
          "$ref" : "#/definitions/Vpc"
        }
      },
      "required" : [ "BootstrapServers", "Vpc" ]
    },
    "AutoScaling" : {
      "description" : "Details about auto scaling of a connector.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MaxWorkerCount" : {
          "description" : "The maximum number of workers for a connector.",
          "type" : "integer"
        },
        "MinWorkerCount" : {
          "description" : "The minimum number of workers for a connector.",
          "type" : "integer"
        },
        "ScaleInPolicy" : {
          "$ref" : "#/definitions/ScaleInPolicy"
        },
        "ScaleOutPolicy" : {
          "$ref" : "#/definitions/ScaleOutPolicy"
        },
        "McuCount" : {
          "description" : "Specifies how many MSK Connect Units (MCU) as the minimum scaling unit.",
          "type" : "integer",
          "enum" : [ 1, 2, 4, 8 ]
        }
      },
      "required" : [ "MaxWorkerCount", "MinWorkerCount", "ScaleInPolicy", "ScaleOutPolicy", "McuCount" ]
    },
    "Capacity" : {
      "description" : "Information about the capacity allocated to the connector.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AutoScaling" : {
          "$ref" : "#/definitions/AutoScaling"
        },
        "ProvisionedCapacity" : {
          "$ref" : "#/definitions/ProvisionedCapacity"
        }
      },
      "oneOf" : [ {
        "required" : [ "AutoScaling" ]
      }, {
        "required" : [ "ProvisionedCapacity" ]
      } ]
    },
    "CloudWatchLogsLogDelivery" : {
      "description" : "Details about delivering logs to Amazon CloudWatch Logs.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Enabled" : {
          "description" : "Specifies whether the logs get sent to the specified CloudWatch Logs destination.",
          "type" : "boolean"
        },
        "LogGroup" : {
          "description" : "The CloudWatch log group that is the destination for log delivery.",
          "type" : "string"
        }
      },
      "required" : [ "Enabled" ]
    },
    "CustomPlugin" : {
      "description" : "Details about a custom plugin.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CustomPluginArn" : {
          "description" : "The Amazon Resource Name (ARN) of the custom plugin to use.",
          "type" : "string",
          "pattern" : "arn:(aws|aws-us-gov|aws-cn):kafkaconnect:.*"
        },
        "Revision" : {
          "description" : "The revision of the custom plugin to use.",
          "type" : "integer",
          "format" : "int64",
          "minimum" : 1
        }
      },
      "required" : [ "CustomPluginArn", "Revision" ]
    },
    "FirehoseLogDelivery" : {
      "description" : "Details about delivering logs to Amazon Kinesis Data Firehose.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DeliveryStream" : {
          "description" : "The Kinesis Data Firehose delivery stream that is the destination for log delivery.",
          "type" : "string"
        },
        "Enabled" : {
          "description" : "Specifies whether the logs get sent to the specified Kinesis Data Firehose delivery stream.",
          "type" : "boolean"
        }
      },
      "required" : [ "Enabled" ]
    },
    "KafkaCluster" : {
      "description" : "Details of how to connect to the Kafka cluster.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ApacheKafkaCluster" : {
          "$ref" : "#/definitions/ApacheKafkaCluster"
        }
      },
      "required" : [ "ApacheKafkaCluster" ]
    },
    "KafkaClusterClientAuthentication" : {
      "description" : "Details of the client authentication used by the Kafka cluster.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AuthenticationType" : {
          "$ref" : "#/definitions/KafkaClusterClientAuthenticationType"
        }
      },
      "required" : [ "AuthenticationType" ]
    },
    "KafkaClusterClientAuthenticationType" : {
      "description" : "The type of client authentication used to connect to the Kafka cluster. Value NONE means that no client authentication is used.",
      "type" : "string",
      "enum" : [ "NONE", "IAM" ]
    },
    "KafkaClusterEncryptionInTransit" : {
      "description" : "Details of encryption in transit to the Kafka cluster.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "EncryptionType" : {
          "$ref" : "#/definitions/KafkaClusterEncryptionInTransitType"
        }
      },
      "required" : [ "EncryptionType" ]
    },
    "KafkaClusterEncryptionInTransitType" : {
      "description" : "The type of encryption in transit to the Kafka cluster.",
      "type" : "string",
      "enum" : [ "PLAINTEXT", "TLS" ]
    },
    "LogDelivery" : {
      "description" : "Details of what logs are delivered and where they are delivered.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "WorkerLogDelivery" : {
          "$ref" : "#/definitions/WorkerLogDelivery"
        }
      },
      "required" : [ "WorkerLogDelivery" ]
    },
    "Plugin" : {
      "description" : "Details about a Kafka Connect plugin which will be used with the connector.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CustomPlugin" : {
          "$ref" : "#/definitions/CustomPlugin"
        }
      },
      "required" : [ "CustomPlugin" ]
    },
    "ProvisionedCapacity" : {
      "description" : "Details about a fixed capacity allocated to a connector.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "McuCount" : {
          "description" : "Specifies how many MSK Connect Units (MCU) are allocated to the connector.",
          "type" : "integer",
          "enum" : [ 1, 2, 4, 8 ]
        },
        "WorkerCount" : {
          "description" : "Number of workers for a connector.",
          "type" : "integer"
        }
      },
      "required" : [ "WorkerCount" ]
    },
    "S3LogDelivery" : {
      "description" : "Details about delivering logs to Amazon S3.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Bucket" : {
          "description" : "The name of the S3 bucket that is the destination for log delivery.",
          "type" : "string"
        },
        "Enabled" : {
          "description" : "Specifies whether the logs get sent to the specified Amazon S3 destination.",
          "type" : "boolean"
        },
        "Prefix" : {
          "description" : "The S3 prefix that is the destination for log delivery.",
          "type" : "string"
        }
      },
      "required" : [ "Enabled" ]
    },
    "ScaleInPolicy" : {
      "description" : "Information about the scale in policy of the connector.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CpuUtilizationPercentage" : {
          "description" : "Specifies the CPU utilization percentage threshold at which connector scale in should trigger.",
          "type" : "integer",
          "minimum" : 1,
          "maximum" : 100
        }
      },
      "required" : [ "CpuUtilizationPercentage" ]
    },
    "ScaleOutPolicy" : {
      "description" : "Information about the scale out policy of the connector.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CpuUtilizationPercentage" : {
          "description" : "Specifies the CPU utilization percentage threshold at which connector scale out should trigger.",
          "type" : "integer",
          "minimum" : 1,
          "maximum" : 100
        }
      },
      "required" : [ "CpuUtilizationPercentage" ]
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256
        }
      },
      "required" : [ "Value", "Key" ],
      "additionalProperties" : False
    },
    "Vpc" : {
      "description" : "Information about a VPC used with the connector.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SecurityGroups" : {
          "description" : "The AWS security groups to associate with the elastic network interfaces in order to specify what the connector has access to.",
          "type" : "array",
          "uniqueItems" : True,
          "items" : {
            "type" : "string"
          },
          "insertionOrder" : False
        },
        "Subnets" : {
          "description" : "The list of subnets to connect to in the virtual private cloud (VPC). AWS creates elastic network interfaces inside these subnets.",
          "type" : "array",
          "uniqueItems" : True,
          "minItems" : 1,
          "items" : {
            "type" : "string"
          },
          "insertionOrder" : False
        }
      },
      "required" : [ "SecurityGroups", "Subnets" ]
    },
    "WorkerConfiguration" : {
      "description" : "Specifies the worker configuration to use with the connector.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Revision" : {
          "description" : "The revision of the worker configuration to use.",
          "type" : "integer",
          "minimum" : 1,
          "format" : "int64"
        },
        "WorkerConfigurationArn" : {
          "description" : "The Amazon Resource Name (ARN) of the worker configuration to use.",
          "type" : "string",
          "pattern" : "arn:(aws|aws-us-gov|aws-cn):kafkaconnect:.*"
        }
      },
      "required" : [ "Revision", "WorkerConfigurationArn" ]
    },
    "WorkerLogDelivery" : {
      "description" : "Specifies where worker logs are delivered.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CloudWatchLogs" : {
          "$ref" : "#/definitions/CloudWatchLogsLogDelivery"
        },
        "Firehose" : {
          "$ref" : "#/definitions/FirehoseLogDelivery"
        },
        "S3" : {
          "$ref" : "#/definitions/S3LogDelivery"
        }
      }
    }
  },
  "required" : [ "Capacity", "ConnectorConfiguration", "ConnectorName", "KafkaConnectVersion", "KafkaCluster", "KafkaClusterClientAuthentication", "KafkaClusterEncryptionInTransit", "Plugins", "ServiceExecutionRoleArn" ],
  "primaryIdentifier" : [ "/properties/ConnectorArn" ],
  "additionalIdentifiers" : [ [ "/properties/ConnectorName" ] ],
  "readOnlyProperties" : [ "/properties/ConnectorArn" ],
  "replacementStrategy" : "delete_then_create",
  "createOnlyProperties" : [ "/properties/ConnectorDescription", "/properties/ConnectorName", "/properties/KafkaCluster", "/properties/KafkaClusterClientAuthentication", "/properties/KafkaClusterEncryptionInTransit", "/properties/KafkaConnectVersion", "/properties/LogDelivery", "/properties/Plugins", "/properties/ServiceExecutionRoleArn", "/properties/WorkerConfiguration" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "kafkaconnect:CreateConnector", "kafkaconnect:DescribeConnector", "kafkaconnect:TagResource", "kafkaconnect:ListTagsForResource", "iam:CreateServiceLinkedRole", "iam:PassRole", "ec2:CreateNetworkInterface", "ec2:DescribeSecurityGroups", "ec2:DescribeSubnets", "ec2:DescribeVpcs", "logs:CreateLogDelivery", "logs:GetLogDelivery", "logs:ListLogDeliveries", "logs:PutResourcePolicy", "logs:DescribeResourcePolicies", "logs:DescribeLogGroups", "s3:GetBucketPolicy", "s3:PutBucketPolicy", "firehose:TagDeliveryStream" ]
    },
    "read" : {
      "permissions" : [ "kafkaconnect:DescribeConnector", "kafkaconnect:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "kafkaconnect:DeleteConnector", "kafkaconnect:DescribeConnector", "logs:DeleteLogDelivery", "logs:GetLogDelivery", "logs:ListLogDeliveries" ]
    },
    "update" : {
      "permissions" : [ "kafkaconnect:UpdateConnector", "kafkaconnect:DescribeConnector", "kafkaconnect:DescribeConnectorOperation", "kafkaconnect:TagResource", "kafkaconnect:ListTagsForResource", "kafkaconnect:UntagResource", "iam:CreateServiceLinkedRole", "logs:UpdateLogDelivery", "logs:GetLogDelivery", "logs:ListLogDeliveries", "logs:PutResourcePolicy", "logs:DescribeResourcePolicies", "logs:DescribeLogGroups", "s3:GetBucketPolicy", "s3:PutBucketPolicy", "firehose:TagDeliveryStream" ]
    },
    "list" : {
      "permissions" : [ "kafkaconnect:ListConnectors" ]
    }
  }
}