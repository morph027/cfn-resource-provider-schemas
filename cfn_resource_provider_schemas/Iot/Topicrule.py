SCHEMA = {
  "typeName" : "AWS::IoT::TopicRule",
  "description" : "Resource Type definition for AWS::IoT::TopicRule",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "additionalProperties" : False,
  "properties" : {
    "Arn" : {
      "type" : "string"
    },
    "RuleName" : {
      "type" : "string"
    },
    "TopicRulePayload" : {
      "$ref" : "#/definitions/TopicRulePayload"
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "definitions" : {
    "TopicRulePayload" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "RuleDisabled" : {
          "type" : "boolean"
        },
        "ErrorAction" : {
          "$ref" : "#/definitions/Action"
        },
        "Description" : {
          "type" : "string"
        },
        "AwsIotSqlVersion" : {
          "type" : "string"
        },
        "Actions" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/Action"
          }
        },
        "Sql" : {
          "type" : "string"
        }
      },
      "required" : [ "Actions", "Sql" ]
    },
    "Action" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CloudwatchAlarm" : {
          "$ref" : "#/definitions/CloudwatchAlarmAction"
        },
        "CloudwatchLogs" : {
          "$ref" : "#/definitions/CloudwatchLogsAction"
        },
        "CloudwatchMetric" : {
          "$ref" : "#/definitions/CloudwatchMetricAction"
        },
        "DynamoDB" : {
          "$ref" : "#/definitions/DynamoDBAction"
        },
        "DynamoDBv2" : {
          "$ref" : "#/definitions/DynamoDBv2Action"
        },
        "Elasticsearch" : {
          "$ref" : "#/definitions/ElasticsearchAction"
        },
        "Firehose" : {
          "$ref" : "#/definitions/FirehoseAction"
        },
        "Http" : {
          "$ref" : "#/definitions/HttpAction"
        },
        "IotAnalytics" : {
          "$ref" : "#/definitions/IotAnalyticsAction"
        },
        "IotEvents" : {
          "$ref" : "#/definitions/IotEventsAction"
        },
        "IotSiteWise" : {
          "$ref" : "#/definitions/IotSiteWiseAction"
        },
        "Kafka" : {
          "$ref" : "#/definitions/KafkaAction"
        },
        "Kinesis" : {
          "$ref" : "#/definitions/KinesisAction"
        },
        "Lambda" : {
          "$ref" : "#/definitions/LambdaAction"
        },
        "Location" : {
          "$ref" : "#/definitions/LocationAction"
        },
        "OpenSearch" : {
          "$ref" : "#/definitions/OpenSearchAction"
        },
        "Republish" : {
          "$ref" : "#/definitions/RepublishAction"
        },
        "S3" : {
          "$ref" : "#/definitions/S3Action"
        },
        "Sns" : {
          "$ref" : "#/definitions/SnsAction"
        },
        "Sqs" : {
          "$ref" : "#/definitions/SqsAction"
        },
        "StepFunctions" : {
          "$ref" : "#/definitions/StepFunctionsAction"
        },
        "Timestream" : {
          "$ref" : "#/definitions/TimestreamAction"
        }
      }
    },
    "CloudwatchAlarmAction" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "StateValue" : {
          "type" : "string"
        },
        "AlarmName" : {
          "type" : "string"
        },
        "StateReason" : {
          "type" : "string"
        },
        "RoleArn" : {
          "type" : "string"
        }
      },
      "required" : [ "AlarmName", "StateReason", "StateValue", "RoleArn" ]
    },
    "CloudwatchLogsAction" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "LogGroupName" : {
          "type" : "string"
        },
        "RoleArn" : {
          "type" : "string"
        },
        "BatchMode" : {
          "type" : "boolean"
        }
      },
      "required" : [ "LogGroupName", "RoleArn" ]
    },
    "CloudwatchMetricAction" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MetricName" : {
          "type" : "string"
        },
        "MetricValue" : {
          "type" : "string"
        },
        "MetricNamespace" : {
          "type" : "string"
        },
        "MetricUnit" : {
          "type" : "string"
        },
        "RoleArn" : {
          "type" : "string"
        },
        "MetricTimestamp" : {
          "type" : "string"
        }
      },
      "required" : [ "MetricName", "MetricValue", "MetricNamespace", "MetricUnit", "RoleArn" ]
    },
    "DynamoDBAction" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "TableName" : {
          "type" : "string"
        },
        "PayloadField" : {
          "type" : "string"
        },
        "RangeKeyField" : {
          "type" : "string"
        },
        "HashKeyField" : {
          "type" : "string"
        },
        "RangeKeyValue" : {
          "type" : "string"
        },
        "RangeKeyType" : {
          "type" : "string"
        },
        "HashKeyType" : {
          "type" : "string"
        },
        "HashKeyValue" : {
          "type" : "string"
        },
        "RoleArn" : {
          "type" : "string"
        }
      },
      "required" : [ "TableName", "HashKeyField", "HashKeyValue", "RoleArn" ]
    },
    "DynamoDBv2Action" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "PutItem" : {
          "$ref" : "#/definitions/PutItemInput"
        },
        "RoleArn" : {
          "type" : "string"
        }
      }
    },
    "PutItemInput" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "TableName" : {
          "type" : "string"
        }
      },
      "required" : [ "TableName" ]
    },
    "ElasticsearchAction" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Type" : {
          "type" : "string"
        },
        "Index" : {
          "type" : "string"
        },
        "Id" : {
          "type" : "string"
        },
        "Endpoint" : {
          "type" : "string"
        },
        "RoleArn" : {
          "type" : "string"
        }
      },
      "required" : [ "Type", "Endpoint", "Index", "Id", "RoleArn" ]
    },
    "FirehoseAction" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DeliveryStreamName" : {
          "type" : "string"
        },
        "RoleArn" : {
          "type" : "string"
        },
        "Separator" : {
          "type" : "string"
        },
        "BatchMode" : {
          "type" : "boolean"
        }
      },
      "required" : [ "DeliveryStreamName", "RoleArn" ]
    },
    "HttpAction" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ConfirmationUrl" : {
          "type" : "string"
        },
        "Headers" : {
          "type" : "array",
          "uniqueItems" : True,
          "items" : {
            "$ref" : "#/definitions/HttpActionHeader"
          }
        },
        "Url" : {
          "type" : "string"
        },
        "Auth" : {
          "$ref" : "#/definitions/HttpAuthorization"
        }
      },
      "required" : [ "Url" ]
    },
    "HttpActionHeader" : {
      "type" : "object",
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
    },
    "HttpAuthorization" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Sigv4" : {
          "$ref" : "#/definitions/SigV4Authorization"
        }
      }
    },
    "SigV4Authorization" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ServiceName" : {
          "type" : "string"
        },
        "SigningRegion" : {
          "type" : "string"
        },
        "RoleArn" : {
          "type" : "string"
        }
      },
      "required" : [ "ServiceName", "SigningRegion", "RoleArn" ]
    },
    "IotAnalyticsAction" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "RoleArn" : {
          "type" : "string"
        },
        "ChannelName" : {
          "type" : "string"
        },
        "BatchMode" : {
          "type" : "boolean"
        }
      },
      "required" : [ "ChannelName", "RoleArn" ]
    },
    "IotEventsAction" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "InputName" : {
          "type" : "string"
        },
        "RoleArn" : {
          "type" : "string"
        },
        "MessageId" : {
          "type" : "string"
        },
        "BatchMode" : {
          "type" : "boolean"
        }
      },
      "required" : [ "InputName", "RoleArn" ]
    },
    "IotSiteWiseAction" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "RoleArn" : {
          "type" : "string"
        },
        "PutAssetPropertyValueEntries" : {
          "type" : "array",
          "uniqueItems" : True,
          "items" : {
            "$ref" : "#/definitions/PutAssetPropertyValueEntry"
          }
        }
      },
      "required" : [ "PutAssetPropertyValueEntries", "RoleArn" ]
    },
    "PutAssetPropertyValueEntry" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "PropertyAlias" : {
          "type" : "string"
        },
        "PropertyValues" : {
          "type" : "array",
          "uniqueItems" : True,
          "items" : {
            "$ref" : "#/definitions/AssetPropertyValue"
          }
        },
        "AssetId" : {
          "type" : "string"
        },
        "EntryId" : {
          "type" : "string"
        },
        "PropertyId" : {
          "type" : "string"
        }
      },
      "required" : [ "PropertyValues" ]
    },
    "AssetPropertyValue" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "$ref" : "#/definitions/AssetPropertyVariant"
        },
        "Timestamp" : {
          "$ref" : "#/definitions/AssetPropertyTimestamp"
        },
        "Quality" : {
          "type" : "string"
        }
      },
      "required" : [ "Value", "Timestamp" ]
    },
    "AssetPropertyVariant" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "StringValue" : {
          "type" : "string"
        },
        "DoubleValue" : {
          "type" : "string"
        },
        "BooleanValue" : {
          "type" : "string"
        },
        "IntegerValue" : {
          "type" : "string"
        }
      }
    },
    "AssetPropertyTimestamp" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "TimeInSeconds" : {
          "type" : "string"
        },
        "OffsetInNanos" : {
          "type" : "string"
        }
      },
      "required" : [ "TimeInSeconds" ]
    },
    "KafkaAction" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DestinationArn" : {
          "type" : "string"
        },
        "Topic" : {
          "type" : "string"
        },
        "Key" : {
          "type" : "string"
        },
        "Partition" : {
          "type" : "string"
        },
        "ClientProperties" : {
          "type" : "object",
          "additionalProperties" : False,
          "patternProperties" : {
            ".*" : {
              "type" : "string"
            }
          },
          "minProperties" : 1
        },
        "Headers" : {
          "type" : "array",
          "uniqueItems" : True,
          "items" : {
            "$ref" : "#/definitions/KafkaActionHeader"
          }
        }
      },
      "required" : [ "DestinationArn", "Topic", "ClientProperties" ]
    },
    "KafkaActionHeader" : {
      "type" : "object",
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
    },
    "KinesisAction" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "PartitionKey" : {
          "type" : "string"
        },
        "StreamName" : {
          "type" : "string"
        },
        "RoleArn" : {
          "type" : "string"
        }
      },
      "required" : [ "StreamName", "RoleArn" ]
    },
    "LambdaAction" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "FunctionArn" : {
          "type" : "string"
        }
      }
    },
    "LocationAction" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "RoleArn" : {
          "type" : "string"
        },
        "TrackerName" : {
          "type" : "string"
        },
        "DeviceId" : {
          "type" : "string"
        },
        "Latitude" : {
          "type" : "string"
        },
        "Longitude" : {
          "type" : "string"
        },
        "Timestamp" : {
          "$ref" : "#/definitions/Timestamp"
        }
      },
      "required" : [ "RoleArn", "TrackerName", "DeviceId", "Latitude", "Longitude" ]
    },
    "Timestamp" : {
      "type" : "object",
      "properties" : {
        "Value" : {
          "type" : "string"
        },
        "Unit" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False,
      "required" : [ "Value" ]
    },
    "OpenSearchAction" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Type" : {
          "type" : "string"
        },
        "Index" : {
          "type" : "string"
        },
        "Id" : {
          "type" : "string"
        },
        "Endpoint" : {
          "type" : "string"
        },
        "RoleArn" : {
          "type" : "string"
        }
      },
      "required" : [ "Type", "Endpoint", "Index", "Id", "RoleArn" ]
    },
    "RepublishAction" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Qos" : {
          "type" : "integer"
        },
        "Topic" : {
          "type" : "string"
        },
        "RoleArn" : {
          "type" : "string"
        },
        "Headers" : {
          "$ref" : "#/definitions/RepublishActionHeaders"
        }
      },
      "required" : [ "Topic", "RoleArn" ]
    },
    "RepublishActionHeaders" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "PayloadFormatIndicator" : {
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 1024
        },
        "ContentType" : {
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 1024
        },
        "ResponseTopic" : {
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 1024
        },
        "CorrelationData" : {
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 1024
        },
        "MessageExpiry" : {
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 1024
        },
        "UserProperties" : {
          "$ref" : "#/definitions/UserProperties"
        }
      }
    },
    "UserProperties" : {
      "type" : "array",
      "minItems" : 1,
      "maxItems" : 100,
      "items" : {
        "$ref" : "#/definitions/UserProperty"
      }
    },
    "UserProperty" : {
      "type" : "object",
      "additionalProperties" : False,
      "required" : [ "Key", "Value" ],
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 1024
        },
        "Value" : {
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 1024
        }
      }
    },
    "S3Action" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "BucketName" : {
          "type" : "string"
        },
        "Key" : {
          "type" : "string"
        },
        "RoleArn" : {
          "type" : "string"
        },
        "CannedAcl" : {
          "$ref" : "#/definitions/CannedAccessControlList"
        }
      },
      "required" : [ "BucketName", "Key", "RoleArn" ]
    },
    "CannedAccessControlList" : {
      "type" : "string",
      "enum" : [ "private", "public-read", "public-read-write", "aws-exec-read", "authenticated-read", "bucket-owner-read", "bucket-owner-full-control", "log-delivery-write" ]
    },
    "SnsAction" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "TargetArn" : {
          "type" : "string"
        },
        "MessageFormat" : {
          "type" : "string"
        },
        "RoleArn" : {
          "type" : "string"
        }
      },
      "required" : [ "TargetArn", "RoleArn" ]
    },
    "StepFunctionsAction" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ExecutionNamePrefix" : {
          "type" : "string"
        },
        "StateMachineName" : {
          "type" : "string"
        },
        "RoleArn" : {
          "type" : "string"
        }
      },
      "required" : [ "StateMachineName", "RoleArn" ]
    },
    "SqsAction" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "RoleArn" : {
          "type" : "string"
        },
        "UseBase64" : {
          "type" : "boolean"
        },
        "QueueUrl" : {
          "type" : "string"
        }
      },
      "required" : [ "RoleArn", "QueueUrl" ]
    },
    "TimestreamAction" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "RoleArn" : {
          "type" : "string"
        },
        "DatabaseName" : {
          "type" : "string"
        },
        "TableName" : {
          "type" : "string"
        },
        "Dimensions" : {
          "$ref" : "#/definitions/TimestreamDimensionsList"
        },
        "Timestamp" : {
          "$ref" : "#/definitions/TimestreamTimestamp"
        }
      },
      "required" : [ "RoleArn", "DatabaseName", "TableName", "Dimensions" ]
    },
    "TimestreamDimensionsList" : {
      "type" : "array",
      "minItems" : 1,
      "maxItems" : 128,
      "items" : {
        "$ref" : "#/definitions/TimestreamDimension"
      }
    },
    "TimestreamDimension" : {
      "type" : "object",
      "properties" : {
        "Name" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False,
      "required" : [ "Name", "Value" ]
    },
    "TimestreamTimestamp" : {
      "type" : "object",
      "properties" : {
        "Value" : {
          "type" : "string"
        },
        "Unit" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False,
      "required" : [ "Value", "Unit" ]
    },
    "RoleArn" : {
      "type" : "string"
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False,
      "required" : [ "Key", "Value" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "iot:UntagResource", "iot:TagResource", "iot:ListTagsForResource" ]
  },
  "required" : [ "TopicRulePayload" ],
  "createOnlyProperties" : [ "/properties/RuleName" ],
  "primaryIdentifier" : [ "/properties/RuleName" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:PassRole", "iot:CreateTopicRule", "iot:GetTopicRule", "iot:TagResource", "iot:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "iot:GetTopicRule", "iot:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "iam:PassRole", "iot:GetTopicRule", "iot:ListTagsForResource", "iot:ReplaceTopicRule", "iot:TagResource", "iot:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "iot:GetTopicRule", "iot:DeleteTopicRule" ]
    },
    "list" : {
      "permissions" : [ "iot:ListTopicRules" ]
    }
  }
}