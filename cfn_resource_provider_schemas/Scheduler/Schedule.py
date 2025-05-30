SCHEMA = {
  "typeName" : "AWS::Scheduler::Schedule",
  "description" : "Definition of AWS::Scheduler::Schedule Resource Type",
  "definitions" : {
    "AssignPublicIp" : {
      "type" : "string",
      "description" : "Specifies whether the task's elastic network interface receives a public IP address. You can specify ENABLED only when LaunchType in EcsParameters is set to FARGATE.",
      "enum" : [ "ENABLED", "DISABLED" ]
    },
    "AwsVpcConfiguration" : {
      "type" : "object",
      "description" : "This structure specifies the VPC subnets and security groups for the task, and whether a public IP address is to be used. This structure is relevant only for ECS tasks that use the awsvpc network mode.",
      "properties" : {
        "Subnets" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "maxLength" : 1000,
            "minLength" : 1,
            "description" : "Specifies the subnet associated with the task."
          },
          "maxItems" : 16,
          "minItems" : 1,
          "description" : "Specifies the subnets associated with the task. These subnets must all be in the same VPC. You can specify as many as 16 subnets.",
          "insertionOrder" : False
        },
        "SecurityGroups" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "maxLength" : 1000,
            "minLength" : 1,
            "description" : "Specifies the security group associated with the task."
          },
          "maxItems" : 5,
          "minItems" : 1,
          "description" : "Specifies the security groups associated with the task. These security groups must all be in the same VPC. You can specify as many as five security groups. If you do not specify a security group, the default security group for the VPC is used.",
          "insertionOrder" : False
        },
        "AssignPublicIp" : {
          "$ref" : "#/definitions/AssignPublicIp"
        }
      },
      "required" : [ "Subnets" ],
      "additionalProperties" : False
    },
    "CapacityProviderStrategyItem" : {
      "type" : "object",
      "description" : "The details of a capacity provider strategy.",
      "properties" : {
        "CapacityProvider" : {
          "type" : "string",
          "maxLength" : 255,
          "minLength" : 1,
          "description" : "The short name of the capacity provider."
        },
        "Weight" : {
          "type" : "number",
          "default" : 0,
          "maximum" : 1000,
          "minimum" : 0,
          "description" : "The weight value designates the relative percentage of the total number of tasks launched that should use the specified capacity provider. The weight value is taken into consideration after the base value, if defined, is satisfied."
        },
        "Base" : {
          "type" : "number",
          "default" : 0,
          "maximum" : 100000,
          "minimum" : 0,
          "description" : "The base value designates how many tasks, at a minimum, to run on the specified capacity provider. Only one capacity provider in a capacity provider strategy can have a base defined. If no value is specified, the default value of 0 is used."
        }
      },
      "required" : [ "CapacityProvider" ],
      "additionalProperties" : False
    },
    "DeadLetterConfig" : {
      "type" : "object",
      "description" : "A DeadLetterConfig object that contains information about a dead-letter queue configuration.",
      "properties" : {
        "Arn" : {
          "type" : "string",
          "maxLength" : 1600,
          "minLength" : 1,
          "pattern" : "^arn:aws[a-z-]*:sqs:[a-z0-9\\-]+:\\d{12}:[a-zA-Z0-9\\-_]+$",
          "description" : "The ARN of the SQS queue specified as the target for the dead-letter queue."
        }
      },
      "additionalProperties" : False
    },
    "EcsParameters" : {
      "type" : "object",
      "description" : "The custom parameters to be used when the target is an Amazon ECS task.",
      "properties" : {
        "TaskDefinitionArn" : {
          "type" : "string",
          "maxLength" : 1600,
          "minLength" : 1,
          "description" : "The ARN of the task definition to use if the event target is an Amazon ECS task."
        },
        "TaskCount" : {
          "type" : "number",
          "maximum" : 10,
          "minimum" : 1,
          "description" : "The number of tasks to create based on TaskDefinition. The default is 1."
        },
        "LaunchType" : {
          "$ref" : "#/definitions/LaunchType"
        },
        "NetworkConfiguration" : {
          "$ref" : "#/definitions/NetworkConfiguration"
        },
        "PlatformVersion" : {
          "type" : "string",
          "maxLength" : 64,
          "minLength" : 1,
          "description" : "Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as 1.1.0."
        },
        "Group" : {
          "type" : "string",
          "maxLength" : 255,
          "minLength" : 1,
          "description" : "Specifies an ECS task group for the task. The maximum length is 255 characters."
        },
        "CapacityProviderStrategy" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/CapacityProviderStrategyItem"
          },
          "maxItems" : 6,
          "description" : "The capacity provider strategy to use for the task.",
          "insertionOrder" : False
        },
        "EnableECSManagedTags" : {
          "type" : "boolean",
          "description" : "Specifies whether to enable Amazon ECS managed tags for the task. For more information, see Tagging Your Amazon ECS Resources in the Amazon Elastic Container Service Developer Guide."
        },
        "EnableExecuteCommand" : {
          "type" : "boolean",
          "description" : "Whether or not to enable the execute command functionality for the containers in this task. If True, this enables execute command functionality on all containers in the task."
        },
        "PlacementConstraints" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/PlacementConstraint"
          },
          "maxItems" : 10,
          "description" : "An array of placement constraint objects to use for the task. You can specify up to 10 constraints per task (including constraints in the task definition and those specified at runtime).",
          "insertionOrder" : False
        },
        "PlacementStrategy" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/PlacementStrategy"
          },
          "maxItems" : 5,
          "description" : "The placement strategy objects to use for the task. You can specify a maximum of five strategy rules per task.",
          "insertionOrder" : False
        },
        "PropagateTags" : {
          "$ref" : "#/definitions/PropagateTags"
        },
        "ReferenceId" : {
          "type" : "string",
          "maxLength" : 1024,
          "description" : "The reference ID to use for the task."
        },
        "Tags" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/TagMap"
          },
          "maxItems" : 50,
          "minItems" : 0,
          "description" : "The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. To learn more, see RunTask in the Amazon ECS API Reference.",
          "insertionOrder" : False
        }
      },
      "required" : [ "TaskDefinitionArn" ],
      "additionalProperties" : False
    },
    "EventBridgeParameters" : {
      "type" : "object",
      "description" : "EventBridge PutEvent predefined target type.",
      "properties" : {
        "DetailType" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1,
          "description" : "Free-form string, with a maximum of 128 characters, used to decide what fields to expect in the event detail."
        },
        "Source" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1,
          "pattern" : "^(?=[/\\.\\-_A-Za-z0-9]+)((?!aws\\.).*)|(\\$(\\.[\\w_-]+(\\[(\\d+|\\*)\\])*)*)$",
          "description" : "The source of the event."
        }
      },
      "required" : [ "DetailType", "Source" ],
      "additionalProperties" : False
    },
    "FlexibleTimeWindow" : {
      "type" : "object",
      "description" : "Flexible time window allows configuration of a window within which a schedule can be invoked",
      "properties" : {
        "Mode" : {
          "$ref" : "#/definitions/FlexibleTimeWindowMode"
        },
        "MaximumWindowInMinutes" : {
          "type" : "number",
          "maximum" : 1440,
          "minimum" : 1,
          "description" : "The maximum time window during which a schedule can be invoked."
        }
      },
      "required" : [ "Mode" ],
      "additionalProperties" : False
    },
    "FlexibleTimeWindowMode" : {
      "type" : "string",
      "description" : "Determines whether the schedule is executed within a flexible time window.",
      "enum" : [ "OFF", "FLEXIBLE" ]
    },
    "KinesisParameters" : {
      "type" : "object",
      "description" : "The custom parameter you can use to control the shard to which EventBridge Scheduler sends the event.",
      "properties" : {
        "PartitionKey" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1,
          "description" : "The custom parameter used as the Kinesis partition key. For more information, see Amazon Kinesis Streams Key Concepts in the Amazon Kinesis Streams Developer Guide."
        }
      },
      "required" : [ "PartitionKey" ],
      "additionalProperties" : False
    },
    "LaunchType" : {
      "type" : "string",
      "description" : "Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. The FARGATE value is supported only in the Regions where AWS Fargate with Amazon ECS is supported. For more information, see AWS Fargate on Amazon ECS in the Amazon Elastic Container Service Developer Guide.",
      "enum" : [ "EC2", "FARGATE", "EXTERNAL" ]
    },
    "NetworkConfiguration" : {
      "type" : "object",
      "description" : "This structure specifies the network configuration for an ECS task.",
      "properties" : {
        "AwsvpcConfiguration" : {
          "$ref" : "#/definitions/AwsVpcConfiguration"
        }
      },
      "additionalProperties" : False
    },
    "PlacementConstraint" : {
      "type" : "object",
      "description" : "An object representing a constraint on task placement.",
      "properties" : {
        "Type" : {
          "$ref" : "#/definitions/PlacementConstraintType"
        },
        "Expression" : {
          "type" : "string",
          "maxLength" : 2000,
          "description" : "A cluster query language expression to apply to the constraint. You cannot specify an expression if the constraint type is distinctInstance. To learn more, see Cluster Query Language in the Amazon Elastic Container Service Developer Guide."
        }
      },
      "additionalProperties" : False
    },
    "PlacementConstraintType" : {
      "type" : "string",
      "description" : "The type of constraint. Use distinctInstance to ensure that each task in a particular group is running on a different container instance. Use memberOf to restrict the selection to a group of valid candidates.",
      "enum" : [ "distinctInstance", "memberOf" ]
    },
    "PlacementStrategy" : {
      "type" : "object",
      "description" : "The task placement strategy for a task or service.",
      "properties" : {
        "Type" : {
          "$ref" : "#/definitions/PlacementStrategyType"
        },
        "Field" : {
          "type" : "string",
          "maxLength" : 255,
          "description" : "The field to apply the placement strategy against. For the spread placement strategy, valid values are instanceId (or host, which has the same effect), or any platform or custom attribute that is applied to a container instance, such as attribute:ecs.availability-zone. For the binpack placement strategy, valid values are cpu and memory. For the random placement strategy, this field is not used."
        }
      },
      "additionalProperties" : False
    },
    "PlacementStrategyType" : {
      "type" : "string",
      "description" : "The type of placement strategy. The random placement strategy randomly places tasks on available candidates. The spread placement strategy spreads placement across available candidates evenly based on the field parameter. The binpack strategy places tasks on available candidates that have the least available amount of the resource that is specified with the field parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task).",
      "enum" : [ "random", "spread", "binpack" ]
    },
    "PropagateTags" : {
      "type" : "string",
      "description" : "Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags are not propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the TagResource API action.",
      "enum" : [ "TASK_DEFINITION" ]
    },
    "RetryPolicy" : {
      "type" : "object",
      "description" : "A RetryPolicy object that includes information about the retry policy settings.",
      "properties" : {
        "MaximumEventAgeInSeconds" : {
          "type" : "number",
          "maximum" : 86400,
          "minimum" : 60,
          "description" : "The maximum amount of time, in seconds, to continue to make retry attempts."
        },
        "MaximumRetryAttempts" : {
          "type" : "number",
          "maximum" : 185,
          "minimum" : 0,
          "description" : "The maximum number of retry attempts to make before the request fails. Retry attempts with exponential backoff continue until either the maximum number of attempts is made or until the duration of the MaximumEventAgeInSeconds is reached."
        }
      },
      "additionalProperties" : False
    },
    "SageMakerPipelineParameter" : {
      "type" : "object",
      "description" : "Name/Value pair of a parameter to start execution of a SageMaker Model Building Pipeline.",
      "properties" : {
        "Name" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1,
          "pattern" : "^[A-Za-z0-9\\-_]*$",
          "description" : "Name of parameter to start execution of a SageMaker Model Building Pipeline."
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 1024,
          "minLength" : 1,
          "description" : "Value of parameter to start execution of a SageMaker Model Building Pipeline."
        }
      },
      "required" : [ "Name", "Value" ],
      "additionalProperties" : False
    },
    "SageMakerPipelineParameters" : {
      "type" : "object",
      "description" : "These are custom parameters to use when the target is a SageMaker Model Building Pipeline that starts based on AWS EventBridge Scheduler schedules.",
      "properties" : {
        "PipelineParameterList" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/SageMakerPipelineParameter"
          },
          "maxItems" : 200,
          "minItems" : 0,
          "description" : "List of Parameter names and values for SageMaker Model Building Pipeline execution.",
          "insertionOrder" : False
        }
      },
      "additionalProperties" : False
    },
    "ScheduleState" : {
      "type" : "string",
      "description" : "Specifies whether the schedule is enabled or disabled.",
      "enum" : [ "ENABLED", "DISABLED" ]
    },
    "SqsParameters" : {
      "type" : "object",
      "description" : "Contains the message group ID to use when the target is a FIFO queue. If you specify an SQS FIFO queue as a target, the queue must have content-based deduplication enabled.",
      "properties" : {
        "MessageGroupId" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1,
          "description" : "The FIFO message group ID to use as the target."
        }
      },
      "additionalProperties" : False
    },
    "TagMap" : {
      "type" : "object",
      "patternProperties" : {
        ".+" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1
        }
      },
      "additionalProperties" : False
    },
    "Target" : {
      "type" : "object",
      "description" : "The schedule target.",
      "properties" : {
        "Arn" : {
          "type" : "string",
          "maxLength" : 1600,
          "minLength" : 1,
          "description" : "The Amazon Resource Name (ARN) of the target."
        },
        "RoleArn" : {
          "type" : "string",
          "maxLength" : 1600,
          "minLength" : 1,
          "pattern" : "^arn:aws[a-z-]*:iam::\\d{12}:role\\/[\\w+=,.@\\/-]+$",
          "description" : "The Amazon Resource Name (ARN) of the IAM role to be used for this target when the schedule is triggered."
        },
        "DeadLetterConfig" : {
          "$ref" : "#/definitions/DeadLetterConfig"
        },
        "RetryPolicy" : {
          "$ref" : "#/definitions/RetryPolicy"
        },
        "Input" : {
          "type" : "string",
          "minLength" : 1,
          "description" : "The text, or well-formed JSON, passed to the target. If you are configuring a templated Lambda, AWS Step Functions, or Amazon EventBridge target, the input must be a well-formed JSON. For all other target types, a JSON is not required. If you do not specify anything for this field, EventBridge Scheduler delivers a default notification to the target."
        },
        "EcsParameters" : {
          "$ref" : "#/definitions/EcsParameters"
        },
        "EventBridgeParameters" : {
          "$ref" : "#/definitions/EventBridgeParameters"
        },
        "KinesisParameters" : {
          "$ref" : "#/definitions/KinesisParameters"
        },
        "SageMakerPipelineParameters" : {
          "$ref" : "#/definitions/SageMakerPipelineParameters"
        },
        "SqsParameters" : {
          "$ref" : "#/definitions/SqsParameters"
        }
      },
      "required" : [ "Arn", "RoleArn" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "maxLength" : 1224,
      "minLength" : 1,
      "pattern" : "^arn:aws[a-z-]*:scheduler:[a-z0-9\\-]+:\\d{12}:schedule\\/[0-9a-zA-Z-_.]+\\/[0-9a-zA-Z-_.]+$",
      "description" : "The Amazon Resource Name (ARN) of the schedule."
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 512,
      "minLength" : 0,
      "description" : "The description of the schedule."
    },
    "EndDate" : {
      "type" : "string",
      "description" : "The date, in UTC, before which the schedule can invoke its target. Depending on the schedule's recurrence expression, invocations might stop on, or before, the EndDate you specify.",
      "format" : "date-time"
    },
    "FlexibleTimeWindow" : {
      "$ref" : "#/definitions/FlexibleTimeWindow"
    },
    "GroupName" : {
      "type" : "string",
      "maxLength" : 64,
      "minLength" : 1,
      "pattern" : "^[0-9a-zA-Z-_.]+$",
      "description" : "The name of the schedule group to associate with this schedule. If you omit this, the default schedule group is used."
    },
    "KmsKeyArn" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 1,
      "pattern" : "^arn:aws[a-z-]*:kms:[a-z0-9\\-]+:\\d{12}:(key|alias)\\/[0-9a-zA-Z-_]*$",
      "description" : "The ARN for a KMS Key that will be used to encrypt customer data."
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 64,
      "minLength" : 1,
      "pattern" : "^[0-9a-zA-Z-_.]+$"
    },
    "ScheduleExpression" : {
      "type" : "string",
      "maxLength" : 256,
      "minLength" : 1,
      "description" : "The scheduling expression."
    },
    "ScheduleExpressionTimezone" : {
      "type" : "string",
      "maxLength" : 50,
      "minLength" : 1,
      "description" : "The timezone in which the scheduling expression is evaluated."
    },
    "StartDate" : {
      "type" : "string",
      "description" : "The date, in UTC, after which the schedule can begin invoking its target. Depending on the schedule's recurrence expression, invocations might occur on, or after, the StartDate you specify.",
      "format" : "date-time"
    },
    "State" : {
      "$ref" : "#/definitions/ScheduleState"
    },
    "Target" : {
      "$ref" : "#/definitions/Target"
    }
  },
  "required" : [ "FlexibleTimeWindow", "ScheduleExpression", "Target" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/Name" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "scheduler:CreateSchedule", "scheduler:GetSchedule", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "scheduler:GetSchedule" ]
    },
    "update" : {
      "permissions" : [ "scheduler:UpdateSchedule", "scheduler:GetSchedule", "iam:PassRole" ]
    },
    "delete" : {
      "permissions" : [ "scheduler:DeleteSchedule", "scheduler:GetSchedule" ]
    },
    "list" : {
      "permissions" : [ "scheduler:ListSchedules" ]
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "additionalProperties" : False
}