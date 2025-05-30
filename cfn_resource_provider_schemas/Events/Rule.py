SCHEMA = {
  "tagging" : {
    "taggable" : False
  },
  "handlers" : {
    "read" : {
      "permissions" : [ "iam:PassRole", "events:DescribeRule", "events:ListTargetsByRule" ]
    },
    "create" : {
      "permissions" : [ "iam:PassRole", "events:DescribeRule", "events:PutRule", "events:PutTargets" ]
    },
    "update" : {
      "permissions" : [ "iam:PassRole", "events:DescribeRule", "events:PutRule", "events:RemoveTargets", "events:PutTargets" ]
    },
    "list" : {
      "permissions" : [ "events:ListRules" ]
    },
    "delete" : {
      "permissions" : [ "iam:PassRole", "events:DescribeRule", "events:DeleteRule", "events:RemoveTargets", "events:ListTargetsByRule" ]
    }
  },
  "typeName" : "AWS::Events::Rule",
  "readOnlyProperties" : [ "/properties/Arn" ],
  "description" : "Resource Type definition for AWS::Events::Rule",
  "createOnlyProperties" : [ "/properties/Name" ],
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/Arn" ],
  "definitions" : {
    "CapacityProviderStrategyItem" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "CapacityProvider" : {
          "type" : "string"
        },
        "Base" : {
          "type" : "integer"
        },
        "Weight" : {
          "type" : "integer"
        }
      },
      "required" : [ "CapacityProvider" ]
    },
    "HttpParameters" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "PathParameterValues" : {
          "uniqueItems" : True,
          "insertionOrder" : True,
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        },
        "HeaderParameters" : {
          "patternProperties" : {
            "[a-zA-Z0-9]+" : {
              "type" : "string"
            }
          },
          "additionalProperties" : False,
          "type" : "object"
        },
        "QueryStringParameters" : {
          "patternProperties" : {
            "[a-zA-Z0-9]+" : {
              "type" : "string"
            }
          },
          "additionalProperties" : False,
          "type" : "object"
        }
      }
    },
    "DeadLetterConfig" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "Arn" : {
          "type" : "string"
        }
      }
    },
    "RunCommandParameters" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "RunCommandTargets" : {
          "uniqueItems" : True,
          "insertionOrder" : True,
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/RunCommandTarget"
          }
        }
      },
      "required" : [ "RunCommandTargets" ]
    },
    "PlacementStrategy" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "Field" : {
          "type" : "string"
        },
        "Type" : {
          "type" : "string"
        }
      }
    },
    "InputTransformer" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "InputPathsMap" : {
          "patternProperties" : {
            "[a-zA-Z0-9]+" : {
              "type" : "string"
            }
          },
          "additionalProperties" : False,
          "type" : "object"
        },
        "InputTemplate" : {
          "type" : "string"
        }
      },
      "required" : [ "InputTemplate" ]
    },
    "KinesisParameters" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "PartitionKeyPath" : {
          "type" : "string"
        }
      },
      "required" : [ "PartitionKeyPath" ]
    },
    "BatchRetryStrategy" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "Attempts" : {
          "type" : "integer"
        }
      }
    },
    "RedshiftDataParameters" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "StatementName" : {
          "type" : "string"
        },
        "Sqls" : {
          "uniqueItems" : False,
          "insertionOrder" : True,
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        },
        "Database" : {
          "type" : "string"
        },
        "SecretManagerArn" : {
          "type" : "string"
        },
        "DbUser" : {
          "type" : "string"
        },
        "Sql" : {
          "type" : "string"
        },
        "WithEvent" : {
          "type" : "boolean"
        }
      },
      "required" : [ "Database" ]
    },
    "AppSyncParameters" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "GraphQLOperation" : {
          "type" : "string"
        }
      },
      "required" : [ "GraphQLOperation" ]
    },
    "Target" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "InputPath" : {
          "type" : "string"
        },
        "HttpParameters" : {
          "$ref" : "#/definitions/HttpParameters"
        },
        "DeadLetterConfig" : {
          "$ref" : "#/definitions/DeadLetterConfig"
        },
        "RunCommandParameters" : {
          "$ref" : "#/definitions/RunCommandParameters"
        },
        "InputTransformer" : {
          "$ref" : "#/definitions/InputTransformer"
        },
        "KinesisParameters" : {
          "$ref" : "#/definitions/KinesisParameters"
        },
        "RoleArn" : {
          "type" : "string"
        },
        "RedshiftDataParameters" : {
          "$ref" : "#/definitions/RedshiftDataParameters"
        },
        "AppSyncParameters" : {
          "$ref" : "#/definitions/AppSyncParameters"
        },
        "Input" : {
          "type" : "string"
        },
        "SqsParameters" : {
          "$ref" : "#/definitions/SqsParameters"
        },
        "EcsParameters" : {
          "$ref" : "#/definitions/EcsParameters"
        },
        "BatchParameters" : {
          "$ref" : "#/definitions/BatchParameters"
        },
        "Id" : {
          "type" : "string"
        },
        "Arn" : {
          "type" : "string"
        },
        "SageMakerPipelineParameters" : {
          "$ref" : "#/definitions/SageMakerPipelineParameters"
        },
        "RetryPolicy" : {
          "$ref" : "#/definitions/RetryPolicy"
        }
      },
      "required" : [ "Id", "Arn" ]
    },
    "PlacementConstraint" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "Type" : {
          "type" : "string"
        },
        "Expression" : {
          "type" : "string"
        }
      }
    },
    "AwsVpcConfiguration" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "SecurityGroups" : {
          "uniqueItems" : True,
          "insertionOrder" : True,
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        },
        "Subnets" : {
          "uniqueItems" : False,
          "insertionOrder" : True,
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        },
        "AssignPublicIp" : {
          "type" : "string"
        }
      },
      "required" : [ "Subnets" ]
    },
    "SqsParameters" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "MessageGroupId" : {
          "type" : "string"
        }
      },
      "required" : [ "MessageGroupId" ]
    },
    "RunCommandTarget" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "Values" : {
          "uniqueItems" : True,
          "insertionOrder" : True,
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        },
        "Key" : {
          "type" : "string"
        }
      },
      "required" : [ "Values", "Key" ]
    },
    "EcsParameters" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "PlatformVersion" : {
          "type" : "string"
        },
        "Group" : {
          "type" : "string"
        },
        "EnableECSManagedTags" : {
          "type" : "boolean"
        },
        "EnableExecuteCommand" : {
          "type" : "boolean"
        },
        "PlacementConstraints" : {
          "uniqueItems" : True,
          "insertionOrder" : True,
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/PlacementConstraint"
          }
        },
        "PropagateTags" : {
          "type" : "string"
        },
        "TaskCount" : {
          "type" : "integer"
        },
        "PlacementStrategies" : {
          "uniqueItems" : True,
          "insertionOrder" : True,
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/PlacementStrategy"
          }
        },
        "CapacityProviderStrategy" : {
          "uniqueItems" : True,
          "insertionOrder" : True,
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/CapacityProviderStrategyItem"
          }
        },
        "LaunchType" : {
          "type" : "string"
        },
        "ReferenceId" : {
          "type" : "string"
        },
        "TagList" : {
          "uniqueItems" : True,
          "insertionOrder" : True,
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/Tag"
          }
        },
        "NetworkConfiguration" : {
          "$ref" : "#/definitions/NetworkConfiguration"
        },
        "TaskDefinitionArn" : {
          "type" : "string"
        }
      },
      "required" : [ "TaskDefinitionArn" ]
    },
    "BatchParameters" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "ArrayProperties" : {
          "$ref" : "#/definitions/BatchArrayProperties"
        },
        "JobName" : {
          "type" : "string"
        },
        "RetryStrategy" : {
          "$ref" : "#/definitions/BatchRetryStrategy"
        },
        "JobDefinition" : {
          "type" : "string"
        }
      },
      "required" : [ "JobName", "JobDefinition" ]
    },
    "NetworkConfiguration" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "AwsVpcConfiguration" : {
          "$ref" : "#/definitions/AwsVpcConfiguration"
        }
      }
    },
    "Tag" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "Value" : {
          "type" : "string"
        },
        "Key" : {
          "type" : "string"
        }
      }
    },
    "SageMakerPipelineParameters" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "PipelineParameterList" : {
          "uniqueItems" : True,
          "insertionOrder" : True,
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/SageMakerPipelineParameter"
          }
        }
      }
    },
    "RetryPolicy" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "MaximumRetryAttempts" : {
          "type" : "integer"
        },
        "MaximumEventAgeInSeconds" : {
          "type" : "integer"
        }
      }
    },
    "BatchArrayProperties" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "Size" : {
          "type" : "integer"
        }
      }
    },
    "SageMakerPipelineParameter" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "Value" : {
          "type" : "string"
        },
        "Name" : {
          "type" : "string"
        }
      },
      "required" : [ "Value", "Name" ]
    }
  },
  "properties" : {
    "EventBusName" : {
      "description" : "The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.",
      "type" : "string"
    },
    "EventPattern" : {
      "description" : "The event pattern of the rule. For more information, see Events and Event Patterns in the Amazon EventBridge User Guide.",
      "type" : [ "string", "object" ]
    },
    "ScheduleExpression" : {
      "description" : "The scheduling expression. For example, \"cron(0 20 * * ? *)\", \"rate(5 minutes)\". For more information, see Creating an Amazon EventBridge rule that runs on a schedule.",
      "type" : "string"
    },
    "Description" : {
      "description" : "The description of the rule.",
      "type" : "string"
    },
    "State" : {
      "description" : "The state of the rule.",
      "type" : "string",
      "enum" : [ "DISABLED", "ENABLED", "ENABLED_WITH_ALL_CLOUDTRAIL_MANAGEMENT_EVENTS" ]
    },
    "Targets" : {
      "uniqueItems" : True,
      "description" : "Adds the specified targets to the specified rule, or updates the targets if they are already associated with the rule.\nTargets are the resources that are invoked when a rule is triggered.",
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Target"
      }
    },
    "Arn" : {
      "description" : "The ARN of the rule, such as arn:aws:events:us-east-2:123456789012:rule/example.",
      "type" : "string"
    },
    "RoleArn" : {
      "description" : "The Amazon Resource Name (ARN) of the role that is used for target invocation.",
      "type" : "string"
    },
    "Name" : {
      "description" : "The name of the rule.",
      "type" : "string"
    }
  },
  "conditionalCreateOnlyProperties" : [ "/properties/EventBusName" ]
}